"""
Test cases for String Calculator following TDD approach.

Complete Step 2 test coverage: Empty, Single, Two Numbers
"""

import pytest


class TestStringCalculator:
    """Test suite for StringCalculator class following TDD principles."""
    
    def setup_method(self):
        """Set up fresh calculator instance before each test."""
        from src.string_calculator import StringCalculator
        self.calculator = StringCalculator()
    
    # Step 1: Empty String ✅
    def test_empty_string_returns_zero(self):
        """Test: Empty string should return 0"""
        result = self.calculator.add("")
        assert result == 0, "Empty string should return 0"
    
    # Step 2a: Single Numbers ✅
    def test_single_number_returns_itself(self):
        """Test: Single number string should return the number as integer"""
        assert self.calculator.add("1") == 1
        assert self.calculator.add("5") == 5
        assert self.calculator.add("42") == 42
        assert self.calculator.add("0") == 0
        assert self.calculator.add("123") == 123
    
    # Step 2b: Two Numbers (NEW - RED PHASE)
    def test_two_numbers_comma_separated(self):
        """
        RED PHASE - TDD Cycle 3
        
        Test: Two numbers separated by comma should return their sum
        Examples: "1,2" -> 3, "5,7" -> 12, "10,20" -> 30
        
        Expected: WILL FAIL - comma delimiter parsing not implemented yet
        """
        # Basic two-number addition
        result = self.calculator.add("1,2")
        assert result == 3, "Two numbers '1,2' should return 3"
        
        result = self.calculator.add("5,7")
        assert result == 12, "Two numbers '5,7' should return 12"
        
        result = self.calculator.add("10,20")
        assert result == 30, "Two numbers '10,20' should return 30"
        
        # Edge cases
        result = self.calculator.add("0,0")
        assert result == 0, "Two zeros '0,0' should return 0"
        
        result = self.calculator.add("100,200")
        assert result == 300, "Larger numbers '100,200' should return 300"
        
        # Test with spaces (should handle gracefully)
        result = self.calculator.add("1, 2")
        assert result == 3, "Numbers with spaces '1, 2' should return 3"
