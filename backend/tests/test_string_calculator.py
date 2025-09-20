"""
Test cases for String Calculator following TDD approach.

This file demonstrates the Red-Green-Refactor cycle:
- RED: Write a failing test first
- GREEN: Write minimal code to pass the test
- REFACTOR: Improve code while keeping tests green
"""

import pytest


class TestStringCalculator:
    """Test suite for StringCalculator class."""
    
    def test_empty_string_returns_zero(self):
        """
        RED PHASE: First failing test
        
        Test: Empty string should return 0
        Status: WILL FAIL - StringCalculator doesn't exist yet
        """
        from src.string_calculator import StringCalculator
        
        calculator = StringCalculator()
        result = calculator.add("")
        
        assert result == 0, "Empty string should return 0"
