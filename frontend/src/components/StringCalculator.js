
import React, { useState, useCallback } from 'react';
import axios from 'axios';
import './StringCalculator.css';

const StringCalculator = () => {
  // State management
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // API configuration
  const API_BASE_URL = 'http://localhost:5000';

  // Calculate function with comprehensive error handling
  const handleCalculate = useCallback(async () => {
    // Reset states
    setError('');
    setIsLoading(true);

    try {
      // Make API request to Flask backend
      const response = await axios.post(`${API_BASE_URL}/api/add`, {
        numbers: input
      }, {
        headers: { 
          'Content-Type': 'application/json' 
        },
        timeout: 5000 // 5 second timeout
      });

      if (response.data.success) {
        const calculationResult = response.data.result;
        setResult(calculationResult);

        // Add to calculation history
        const historyEntry = {
          id: Date.now(),
          input: input,
          result: calculationResult,
          timestamp: new Date().toLocaleString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
          })
        };
        setHistory(prev => [historyEntry, ...prev.slice(0, 9)]); // Keep last 10 entries
      } else {
        throw new Error(response.data.error || 'Calculation failed');
      }

    } catch (err) {
      console.error('Calculation error:', err);
      
      // Comprehensive error handling
      if (err.response?.data?.error) {
        setError(err.response.data.error);
      } else if (err.code === 'ECONNABORTED') {
        setError('Request timeout. Please try again.');
      } else if (err.code === 'ERR_NETWORK') {
        setError('Cannot connect to server. Please ensure the backend is running on http://localhost:5000');
      } else if (err.response?.status === 400) {
        setError('Invalid input format. Please check your numbers and delimiters.');
      } else if (err.response?.status === 500) {
        setError('Server error. Please try again or contact support.');
      } else {
        setError(err.message || 'An unexpected error occurred');
      }
      
      setResult(null);
    } finally {
      setIsLoading(false);
    }
  }, [input]);

  // Clear function
  const handleClear = useCallback(() => {
    setInput('');
    setResult(null);
    setError('');
  }, []);

  // Clear history function
  const handleClearHistory = useCallback(() => {
    setHistory([]);
  }, []);

  // Load example function
  const loadExample = useCallback((value) => {
    setInput(value);
    setError('');
    setResult(null);
  }, []);

  // Handle Enter key press
  const handleKeyPress = useCallback((e) => {
    if (e.key === 'Enter' && !isLoading) {
      e.preventDefault();
      handleCalculate();
    }
  }, [handleCalculate, isLoading]);

  // Example inputs for all supported formats
  const examples = [
    { 
      label: 'Empty String', 
      value: '',
      description: 'Returns 0 for empty input'
    },
    { 
      label: 'Single: 42', 
      value: '42',
      description: 'Single number returns itself'
    },
    { 
      label: 'Comma: 1,2,3', 
      value: '1,2,3',
      description: 'Comma-separated numbers'
    },
    { 
      label: 'Newline: 1\\n2\\n3', 
      value: '1\n2\n3',
      description: 'Newline-separated numbers'
    },
    { 
      label: 'Mixed: 1\\n2,3', 
      value: '1\n2,3',
      description: 'Mixed comma and newline delimiters'
    },
    { 
      label: 'Custom: //;\\n1;2;3', 
      value: '//;\n1;2;3',
      description: 'Custom single-character delimiter'
    },
    { 
      label: 'Multi-char: //[***]\\n1***2***3', 
      value: '//[***]\n1***2***3',
      description: 'Multi-character custom delimiter'
    },
    { 
      label: 'Multiple: //[*][%]\\n1*2%3', 
      value: '//[*][%]\n1*2%3',
      description: 'Multiple custom delimiters'
    }
  ];

  return (
    <div className="calculator-container">
      <div className="calculator-card">
    
        <header className="calculator-header">
          <h1>String Calculator</h1>
          <p>TDD Implementation</p>
        
        </header>

        {/* Input Section */}
        <div className="input-section">
          <label htmlFor="numbers-input" className="input-label">
            Numbers Input:
          </label>
          <textarea
            id="numbers-input"
            className="numbers-input"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder={`Enter numbers with delimiters...\n\nExamples:\n"1,2,3" → comma separated\n"1\\n2\\n3" → newline separated  \n"//;\\n1;2;3" → custom delimiter\n"//[***]\\n1***2***3" → multi-char delimiter\n"//[*][%]\\n1*2%3" → multiple delimiters`}
            rows={6}
            disabled={isLoading}
          />
        </div>

        {/* Button Section */}
        <div className="button-section">
          <button 
            className="calculate-btn" 
            onClick={handleCalculate}
            disabled={isLoading}
            title="Calculate the sum of numbers"
          >
            {isLoading ? '🔄 Calculating...' : '➕ Calculate Sum'}
          </button>
          <button 
            className="clear-btn" 
            onClick={handleClear}
            disabled={isLoading}
            title="Clear input and result"
          >
            🧹 Clear
          </button>
        </div>

        {/* Error Display */}
        {error && (
          <div className="error-message" role="alert">
            <span className="error-icon">⚠️</span>
            <div>
              <strong>Error:</strong> {error}
              <div style={{ fontSize: '0.9em', marginTop: '8px', opacity: 0.8 }}>
                💡 Tip: Make sure your backend is running and check the input format.
              </div>
            </div>
          </div>
        )}

        {/* Result Display */}
        {result !== null && !error && (
          <div className="result-section">
            <h2 className="result-label">✅ Calculation Result</h2>
            <div className="result-value" data-testid="result">
              {result}
            </div>
            <div style={{ marginTop: '12px', fontSize: '0.9rem', color: '#2F855A' }}>
              🎉 Successfully calculated 
            </div>
          </div>
        )}

        {/* Quick Examples Section */}
        <div className="examples-section">
          <h3>📋 Quick Examples - Click to Load:</h3>
          <div className="examples-grid">
            {examples.map((example, index) => (
              <button
                key={index}
                className="example-btn"
                onClick={() => loadExample(example.value)}
                disabled={isLoading}
                title={example.description}
              >
                <div style={{ fontWeight: '600' }}>{example.label}</div>
                <div style={{ fontSize: '0.8rem', opacity: 0.7, marginTop: '4px' }}>
                  {example.description}
                </div>
              </button>
            ))}
          </div>
        </div>

     
        <div className="features-section">
          <h3>🚀Our Software Craftsmanship Features:</h3>
          <div className="features-grid">
            <div className="feature-item">
              <strong>Test-Driven Development:</strong > Built using strict TDD methodology with comprehensive test coverage and Red-Green-Refactor cycles
            </div>
            <div className="feature-item">
              <strong>Clean Architecture:</strong> Professional separation of concerns with maintainable, extensible code structure
            </div>
            <div className="feature-item">
              <strong>All Delimiter Formats:</strong> Empty strings, single numbers, comma/newline delimiters, custom single & multi-character, multiple delimiters
            </div>
            <div className="feature-item">
              <strong>Enterprise Error Handling:</strong> Comprehensive validation, negative number detection, and graceful failure recovery
            </div>
            <div className="feature-item">
              <strong>Full-Stack Excellence:</strong> React frontend with Python Flask backend, RESTful API integration, real-time communication
            </div>
            <div className="feature-item">
              <strong>Professional UX:</strong> Responsive design, accessibility features, loading states, calculation history, and intuitive interface
            </div>
          </div>
        </div>
      </div>

      {/* History Section */}
      {history.length > 0 && (
        <div className="history-section">
          <div className="history-header">
            <h3>📚 Calculation History</h3>
            <button 
              className="clear-history-btn"
              onClick={handleClearHistory}
              title="Clear calculation history"
            >
              🗑️ Clear History
            </button>
          </div>
          <div className="history-list py-4">
            {history.map((entry) => (
              <div key={entry.id} className="history-item">
                <div className="history-input">
                  <strong>Input:</strong> 
                  <code>"{entry.input || '(empty string)'}"</code>
                </div>
                <div className="history-result">
                  <strong>Result:</strong> 
                  <span className="result-highlight">{entry.result}</span>
                </div>
                <div className="history-timestamp">
                  🕒 {entry.timestamp}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
        {/* Footer Section */}  
      <footer style={{ 
        textAlign: 'center', 
        marginTop: '40px', 
        padding: '20px',
        color: 'rgba(255, 255, 255, 0.8)',
        fontSize: '0.9rem'
      }}>
        <div>
          Built with ❤️ using <strong>Software Craftsmanship</strong> principles
        </div>
        <div style={{ marginTop: '8px', fontSize: '0.8rem', opacity: 0.7 }}>
          TDD • Clean Code • Professional Excellence • Software Development
        </div>
      </footer>
    </div>
  );
};

export default StringCalculator;
