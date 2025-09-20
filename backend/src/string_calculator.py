"""
String Calculator implementation following TDD principles.

GREEN PHASE - TDD Cycle 8: Add multiple custom delimiter support.
"""
import re


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Complete Feature Set:
    - Empty string returns 0
    - Single number returns the number itself
    - Multiple numbers with default delimiters (comma, newline)
    - Custom single character delimiters: //[delimiter]\\n[numbers...]
    - Custom multi-character delimiters: //[delimiter]\\n[numbers...]
    - Multiple custom delimiters: //[delim1][delim2]\\n[numbers...] ✅ (GREEN phase)
    """
    
    # Default supported delimiters
    DEFAULT_DELIMITERS = [',', '\n']
    
    # Custom delimiter patterns
    SINGLE_CHAR_DELIMITER_PATTERN = r"^//(.)\n(.*)$"
    MULTIPLE_DELIMITERS_PATTERN = r"^//((?:\[.+?\])+)\n(.*)$"
    BRACKET_DELIMITER_EXTRACT = r"\[(.+?)\]"
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string with comprehensive delimiter support.
        
        Args:
            numbers: String containing numbers separated by delimiters
            
        Returns:
            Sum of all valid numbers
            
        Examples:
            >>> calc = StringCalculator()
            >>> calc.add("//;\\n1;2")
            3
            >>> calc.add("//[***]\\n1***2***3")
            6
            >>> calc.add("//[*][%]\\n1*2%3")
            6
        """
        if not numbers:
            return 0
        
        delimiters, numbers_part = self._extract_delimiters_and_numbers(numbers)
        number_list = self._parse_numbers_with_delimiters(numbers_part, delimiters)
        
        return sum(number_list)
    
    def _extract_delimiters_and_numbers(self, input_string: str) -> tuple[list[str], str]:
        """
        Extract delimiters and numbers part from input string.
        
        Args:
            input_string: Full input that may contain custom delimiter definition
            
        Returns:
            Tuple of (delimiters_list, numbers_string)
        """
        # GREEN PHASE: Check for multiple bracket-enclosed delimiters first
        multiple_match = re.match(self.MULTIPLE_DELIMITERS_PATTERN, input_string, re.DOTALL)
        if multiple_match:
            delimiter_section = multiple_match.group(1)
            numbers_part = multiple_match.group(2)
            
            # Extract all delimiters from bracket format
            delimiters = re.findall(self.BRACKET_DELIMITER_EXTRACT, delimiter_section)
            if delimiters:
                return delimiters, numbers_part
        
        # Check for single character delimiter (no brackets)
        single_match = re.match(self.SINGLE_CHAR_DELIMITER_PATTERN, input_string, re.DOTALL)
        if single_match:
            custom_delimiter = single_match.group(1)
            numbers_part = single_match.group(2)
            return [custom_delimiter], numbers_part
        
        # No custom delimiter, use defaults
        return self.DEFAULT_DELIMITERS.copy(), input_string
    
    def _parse_numbers_with_delimiters(self, numbers_str: str, delimiters: list[str]) -> list[int]:
        """Parse numbers from string using provided delimiters."""
        if not numbers_str:
            return []
        
        # Create regex pattern from all delimiters
        escaped_delimiters = [re.escape(delimiter) for delimiter in delimiters]
        pattern = '|'.join(escaped_delimiters)
        
        # Split using regex and parse numbers
        parts = re.split(pattern, numbers_str)
        result = []
        
        for part in parts:
            cleaned_part = part.strip()
            if cleaned_part:
                try:
                    result.append(int(cleaned_part))
                except ValueError:
                    continue
        
        return result
