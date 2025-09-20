"""
Test cases for String Calculator following TDD approach.

Step 4: Custom delimiters with //[delimiter]\n[numbers...] format
"""

import pytest


class TestStringCalculator:
    """Test suite for StringCalculator class following TDD principles."""
    
    def setup_method(self):
        """Set up fresh calculator instance before each test."""
        from src.string_calculator import StringCalculator
        self.calculator = StringCalculator()
    
    # ===== STEPS 1-3: COMPLETED ✅ =====
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
    
    def test_multiple_numbers_comma_separated(self):
        """Test: Handle unlimited amount of numbers with commas"""
        assert self.calculator.add("1,2,3") == 6
        assert self.calculator.add("1,2,3,4") == 10
        assert self.calculator.add("1,2,3,4,5") == 15
        assert self.calculator.add("10,20,30") == 60
        assert self.calculator.add("1,0,2,0,3") == 6
        assert self.calculator.add("1,1,1,1,1,1,1,1,1,1") == 10
    
    def test_newline_delimiters(self):
        """Test: Allow newlines as delimiters (along with commas)"""
        assert self.calculator.add("1\n2,3") == 6
        assert self.calculator.add("1\n2\n3") == 6
        assert self.calculator.add("1,2\n3,4\n5") == 15
        assert self.calculator.add("10\n20") == 30
        assert self.calculator.add("5\n") == 5
    
    def test_delimiter_edge_cases(self):
        """Test edge cases for delimiter handling"""
        assert self.calculator.add("1,,2") == 3
        assert self.calculator.add("1\n\n2") == 3
        assert self.calculator.add(",1,2,") == 3
        assert self.calculator.add("\n1\n2\n") == 3
        assert self.calculator.add(" 1 , 2 ") == 3
        assert self.calculator.add("1\n 2 \n 3") == 6
        assert self.calculator.add("1,\n2,3\n,4") == 10
    
    # ===== STEP 4: CUSTOM DELIMITERS (NEW - RED PHASE) =====
    def test_custom_single_character_delimiters(self):
        """
        RED PHASE - TDD Cycle 6
        
        Test: Custom single character delimiters with //[delimiter]\\n[numbers...] format
        Examples: "//;\\n1;2" -> 3, "//*\\n1*2*3" -> 6
        
        Expected: WILL FAIL - custom delimiter parsing not implemented yet
        """
        # Basic semicolon delimiter
        result = self.calculator.add("//;\n1;2")
        assert result == 3, "Custom delimiter '//;\\n1;2' should return 3"
        
        # Asterisk delimiter
        result = self.calculator.add("//*\n1*2*3")
        assert result == 6, "Custom delimiter '//*\\n1*2*3' should return 6"
        
        # Pipe delimiter
        result = self.calculator.add("//|\n1|2|3|4")
        assert result == 10, "Custom delimiter '//|\\n1|2|3|4' should return 10"
        
        # Hash delimiter
        result = self.calculator.add("//#\n5#5#5")
        assert result == 15, "Custom delimiter '//#\\n5#5#5' should return 15"
        
        # Percent delimiter
        result = self.calculator.add("//%\n10%20%30")
        assert result == 60, "Custom delimiter '//%\\n10%20%30' should return 60"
        
        # Edge case: single number with custom delimiter
        result = self.calculator.add("//;\n5")
        assert result == 5, "Single number with custom delimiter '//;\\n5' should return 5"
	
	    # ===== STEP 4B: MULTI-CHARACTER CUSTOM DELIMITERS (NEW - RED PHASE) =====
    def test_custom_multi_character_delimiters(self):
        """
        RED PHASE - TDD Cycle 7
        
        Test: Custom multi-character delimiters with //[delimiter]\\n[numbers...] format
        Examples: "//[***]\\n1***2***3" -> 6, "//[sep]\\n1sep2sep3" -> 6
        
        Expected: WILL FAIL - multi-character delimiter parsing not implemented yet
        """
        # Three asterisks delimiter
        result = self.calculator.add("//[***]\n1***2***3")
        assert result == 6, "Multi-char delimiter '//[***]\\n1***2***3' should return 6"
        
        # Word delimiter
        result = self.calculator.add("//[sep]\n1sep2sep3")
        assert result == 6, "Word delimiter '//[sep]\\n1sep2sep3' should return 6"
        
        # Complex delimiter
        result = self.calculator.add("//[::]\n10::20::30")
        assert result == 60, "Complex delimiter '//[:::]\\n10::20::30' should return 60"
        
        # Single number with multi-char delimiter
        result = self.calculator.add("//[***]\n42")
        assert result == 42, "Single number '//[***]\\n42' should return 42"
        
        # Longer delimiter
        result = self.calculator.add("//[DELIM]\n1DELIM2DELIM3DELIM4")
        assert result == 10, "Long delimiter should work correctly"

