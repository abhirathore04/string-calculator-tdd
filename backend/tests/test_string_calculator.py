"""
Test cases for String Calculator following TDD approach.

This demonstrates professional TDD implementation:
- RED: Write failing test first
- GREEN: Write minimal code to pass
- REFACTOR: Improve code while keeping tests green
"""

import pytest


class TestStringCalculator:
    """Test suite for StringCalculator class following TDD principles."""
    
    def setup_method(self):
        """Set up fresh calculator instance before each test."""
        from src.string_calculator import StringCalculator
        self.calculator = StringCalculator()
    
    # Step 1: Empty String (COMPLETED)
    def test_empty_string_returns_zero(self):
        """
        Test: Empty string should return 0
        Status: ✅ PASSING (from Step 1)
        """
        result = self.calculator.add("")
        assert result == 0, "Empty string should return 0"
    
    # Step 2: Single Numbers (NEW - RED PHASE)
    def test_single_number_returns_itself(self):
        """
        RED PHASE - TDD Cycle 2
        
        Test: Single number string should return the number as integer
        Examples: "1" -> 1, "5" -> 5, "42" -> 42
        
        Expected: WILL FAIL - single number parsing not implemented yet
        """
        # Test basic single digits
        result = self.calculator.add("1")
        assert result == 1, "Single number '1' should return 1"
        
        result = self.calculator.add("5")
        assert result == 5, "Single number '5' should return 5"
        
        # Test multi-digit number
        result = self.calculator.add("42")
        assert result == 42, "Single number '42' should return 42"
        
        # Test edge case: zero
        result = self.calculator.add("0")
        assert result == 0, "Single number '0' should return 0"
        
        # Test larger number
        result = self.calculator.add("123")
        assert result == 123, "Single number '123' should return 123"
