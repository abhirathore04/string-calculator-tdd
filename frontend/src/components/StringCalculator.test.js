/**
 * Fixed Frontend Tests for String Calculator Component
 */

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import StringCalculator from './StringCalculator';

// Mock axios properly for Jest
jest.mock('axios', () => ({
  post: jest.fn(() => Promise.resolve({
    data: {
      success: true,
      result: 6,
      input: '1,2,3'
    }
  }))
}));

const axios = require('axios');

describe('StringCalculator Frontend', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders calculator interface correctly', () => {
    render(<StringCalculator />);
    
    expect(screen.getByText(/String Calculator/)).toBeInTheDocument();
    expect(screen.getByText(/Numbers Input/)).toBeInTheDocument();
    expect(screen.getByText(/Calculate Sum/)).toBeInTheDocument();
    expect(screen.getByText(/Clear/)).toBeInTheDocument();
  });

  test('handles successful calculation', async () => {
    const mockResponse = {
      data: {
        success: true,
        result: 6,
        input: '1,2,3'
      }
    };
    axios.post.mockResolvedValue(mockResponse);

    render(<StringCalculator />);
    
    const input = screen.getByRole('textbox');
    const calculateButton = screen.getByText(/Calculate Sum/);

    fireEvent.change(input, { target: { value: '1,2,3' } });
    fireEvent.click(calculateButton);

    // Use data-testid to target specific result element
    await waitFor(() => {
      const resultElement = screen.getByTestId('result');
      expect(resultElement).toHaveTextContent('6');
    });

    expect(axios.post).toHaveBeenCalledWith(
      'http://localhost:5000/api/add',
      { numbers: '1,2,3' },
      expect.objectContaining({
        headers: { 'Content-Type': 'application/json' },
        timeout: 5000
      })
    );
  });

  test('handles API errors gracefully', async () => {
    const mockError = {
      response: {
        data: {
          error: 'Server error',
          success: false
        }
      }
    };
    axios.post.mockRejectedValue(mockError);

    render(<StringCalculator />);
    
    const calculateButton = screen.getByText(/Calculate Sum/);
    fireEvent.click(calculateButton);

    await waitFor(() => {
      expect(screen.getByText(/Server error/)).toBeInTheDocument();
    });
  });

  test('clear functionality works', () => {
    render(<StringCalculator />);
    
    const input = screen.getByRole('textbox');
    const clearButton = screen.getByText(/Clear/);

    fireEvent.change(input, { target: { value: '1,2,3' } });
    expect(input.value).toBe('1,2,3');

    fireEvent.click(clearButton);
    expect(input.value).toBe('');
  });

  test('example buttons work', () => {
    render(<StringCalculator />);
    
    const input = screen.getByRole('textbox');
    const commaExample = screen.getByText(/Comma: 1,2,3/);

    fireEvent.click(commaExample);
    expect(input.value).toBe('1,2,3');
  });

  test('renders all feature sections', () => {
    render(<StringCalculator />);
    
    expect(screen.getByText(/Quick Examples/)).toBeInTheDocument();
    expect(screen.getByText(/Software Craftsmanship Features/)).toBeInTheDocument();
    expect(screen.getByText(/Test-Driven Development/)).toBeInTheDocument();
    expect(screen.getByText(/Clean Architecture/)).toBeInTheDocument();
  });
});
