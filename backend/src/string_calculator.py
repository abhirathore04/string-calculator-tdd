"""
String Calculator implementation following TDD principles.

REFACTOR PHASE - TDD Cycle 6: Clean, maintainable custom delimiter implementation.
"""
import re


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Supported Features:
    - Empty string returns 0
    - Single number returns the number itself
    - Multiple numbers with default delimiters (comma, newline)
    - Custom single character delimiters: //[delimiter]\\n[numbers...]
    - Handles whitespace and edge cases gracefully
    """
    
    # Default supported delimiters
    DEFAULT_DELIMITERS = [',', '\n']
    
    # Custom delimiter pattern
    CUSTOM_DELIMITER_PATTERN = r"^//(.)\n(.*)$"
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string with various delimiter support.
        
        Args:
            numbers: String containing numbers separated by delimiters
            
        Returns:
            Sum of all valid numbers
            
        Examples:
            >>> calc = StringCalculator()
            >>> calc.add("")
            0
            >>> calc.add("1,2,3")
            6
            >>> calc.add("1\\n2\\n3")
            6
            >>> calc.add("//;\\n1;2")
            3
            >>> calc.add("//*\\n1*2*3")
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
        # Check for custom delimiter format using regex
        match = re.match(self.CUSTOM_DELIMITER_PATTERN, input_string, re.DOTALL)
        
        if match:
            custom_delimiter = match.group(1)
            numbers_part = match.group(2)
            return [custom_delimiter], numbers_part
        
        # No custom delimiter, use defaults
        return self.DEFAULT_DELIMITERS.copy(), input_string
    
    def _parse_numbers_with_delimiters(self, numbers_str: str, delimiters: list[str]) -> list[int]:
        """
        Parse numbers from string using provided delimiters.
        
        Args:
            numbers_str: String containing numbers
            delimiters: List of delimiter strings
            
        Returns:
            List of parsed integers
        """
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
