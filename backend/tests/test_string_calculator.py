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
    
    # ===== STEP 3A: MULTIPLE NUMBERS ✅ =====
    def test_multiple_numbers_comma_separated(self):
        """Test: Handle unlimited amount of numbers with commas"""
        assert self.calculator.add("1,2,3") == 6
        assert self.calculator.add("1,2,3,4") == 10
        assert self.calculator.add("1,2,3,4,5") == 15
        assert self.calculator.add("10,20,30") == 60
        assert self.calculator.add("1,0,2,0,3") == 6
        assert self.calculator.add("1,1,1,1,1,1,1,1,1,1") == 10
    
    # ===== STEP 3B: NEWLINE DELIMITERS (NEW - RED PHASE) =====
    def test_newline_delimiters(self):
        """
        RED PHASE - TDD Cycle 5
        
        Test: Allow newlines as delimiters (along with commas)
        Examples: "1\\n2,3" -> 6, "1\\n2\\n3" -> 6
        
        Expected: WILL FAIL - newline parsing not implemented yet
        """
        # Basic newline + comma combination
        result = self.calculator.add("1\n2,3")
        assert result == 6, "Mixed delimiters '1\\n2,3' should return 6"
        
        # Pure newline delimiters
        result = self.calculator.add("1\n2\n3")
        assert result == 6, "Newline delimiters '1\\n2\\n3' should return 6"
        
        # More complex combinations
        result = self.calculator.add("1,2\n3,4\n5")
        assert result == 15, "Complex mix '1,2\\n3,4\\n5' should return 15"
        
        # Newline with two numbers
        result = self.calculator.add("10\n20")
        assert result == 30, "Two numbers with newline '10\\n20' should return 30"
        
        # Single number with newline at end (edge case)
        result = self.calculator.add("5\n")
        assert result == 5, "Number with trailing newline '5\\n' should return 5"
