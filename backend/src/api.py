"""
Flask REST API for String Calculator.

GREEN PHASE - TDD Cycle 9: REST API implementation.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import sys
import os

# Fix relative import issue for direct execution
if __name__ == '__main__':
    # Add parent directory to path for direct execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from src.string_calculator import StringCalculator
    from src.exceptions import NegativeNumberError
else:
    # Use relative imports for pytest
    from .string_calculator import StringCalculator
    from .exceptions import NegativeNumberError

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Create calculator instance
calculator = StringCalculator()


@app.route('/api/add', methods=['POST'])
def add_numbers():
    """
    Add numbers endpoint for String Calculator.
    
    Expected JSON input:
    {
        "numbers": "1,2,3"  // String with numbers and delimiters
    }
    
    JSON output:
    {
        "result": 6,        // Sum of numbers
        "input": "1,2,3",   // Original input
        "success": true     // Success status
    }
    """
    try:
        # Validate request content type
        if not request.is_json:
            return jsonify({
                'error': 'Content-Type must be application/json',
                'success': False
            }), 400
        
        # Get JSON data
        data = request.get_json()
        
        # Validate required field
        if 'numbers' not in data:
            return jsonify({
                'error': 'Missing required field: numbers',
                'success': False
            }), 400
        
        numbers_input = data['numbers']
        
        # Calculate result using our String Calculator
        result = calculator.add(numbers_input)
        
        # Return success response
        return jsonify({
            'result': result,
            'input': numbers_input,
            'success': True
        }), 200
        
    except NegativeNumberError as e:
        # Handle negative numbers error
        return jsonify({
            'error': str(e),
            'success': False
        }), 400
        
    except Exception as e:
        # Handle unexpected errors
        app.logger.error(f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
        return jsonify({
            'error': 'Internal server error',
            'success': False
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'String Calculator API',
        'version': '1.0.0'
    }), 200


@app.route('/', methods=['GET'])
def root():
    """Root endpoint with API information."""
    return jsonify({
        'message': 'String Calculator API',
        'version': '1.0.0',
        'endpoints': {
            'POST /api/add': 'Add numbers with various delimiters',
            'GET /api/health': 'Health check',
            'GET /': 'This information'
        },
        'examples': {
            'basic': 'POST {"numbers": "1,2,3"} -> {"result": 6}',
            'custom_delimiter': 'POST {"numbers": "//;\\n1;2;3"} -> {"result": 6}',
            'multi_char': 'POST {"numbers": "//[***]\\n1***2***3"} -> {"result": 6}',
            'multiple_delimiters': 'POST {"numbers": "//[*][%]\\n1*2%3"} -> {"result": 6}'
        }
    }), 200


if __name__ == '__main__':
    print("🚀 Starting String Calculator API Server...")
    print("📍 Server running at: http://localhost:5000")
    print("🏥 Health check: http://localhost:5000/api/health")
    print("📚 API docs: http://localhost:5000/")
    print("🔗 Frontend should run at: http://localhost:3000")
    print("\n🧮 String Calculator API is ready!")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
