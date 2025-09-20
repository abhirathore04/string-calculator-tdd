"""
Test cases for String Calculator following TDD approach.

Step 3: Multiple numbers and newline delimiters
"""

import pytest


class TestStringCalculator:
    """Test suite for StringCalculator class following TDD principles."""
    
    def setup_method(self):
        """Set up fresh calculator instance before each test."""
        from src.string_calculator import StringCalculator
        self.calculator = StringCalculator()
    
    # ===== STEP 1 & 2: COMPLETED ✅ =====
    def test_empty_string_returns_zero(self):
        """Test: Empty string should return 0"""
        assert self.calculator.add("") == 0
    
    def test_single_number_returns_itself(self):
        """Test: Single number returns itself"""
        assert self.calculator.add("1") == 1
        assert self.calculator.add("5") == 5
        assert self.calculator.add("42") == 42
        assert self.calculator.add("0") == 0
        assert self.calculator.add("123") == 123
    
    def test_two_numbers_comma_separated(self):
        """Test: Two numbers with comma return their sum"""
        assert self.calculator.add("1,2") == 3
        assert self.calculator.add("5,7") == 12
        assert self.calculator.add("10,20") == 30
    
    # ===== STEP 3A: MULTIPLE NUMBERS (NEW - RED PHASE) =====
    def test_multiple_numbers_comma_separated(self):
        """
        RED PHASE - TDD Cycle 4
        
        Test: Handle unlimited amount of numbers
        Examples: "1,2,3" -> 6, "1,2,3,4,5" -> 15
        
        Expected: WILL FAIL - unlimited numbers not implemented yet
        """
        # Test 3 numbers
        result = self.calculator.add("1,2,3")
        assert result == 6, "Three numbers '1,2,3' should return 6"
        
        # Test 4 numbers
        result = self.calculator.add("1,2,3,4")
        assert result == 10, "Four numbers '1,2,3,4' should return 10"
        
        # Test 5 numbers
        result = self.calculator.add("1,2,3,4,5")
        assert result == 15, "Five numbers '1,2,3,4,5' should return 15"
        
        # Test with larger numbers
        result = self.calculator.add("10,20,30")
        assert result == 60, "Larger numbers '10,20,30' should return 60"
        
        # Test with zeros mixed in
        result = self.calculator.add("1,0,2,0,3")
        assert result == 6, "Numbers with zeros '1,0,2,0,3' should return 6"
        
        # Test many numbers
        result = self.calculator.add("1,1,1,1,1,1,1,1,1,1")
        assert result == 10, "Ten ones should return 10"
