"""
String Calculator implementation following TDD principles.

REFACTOR PHASE - TDD Cycle 3: Clean, maintainable implementation.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Supported Features:
    - Empty string returns 0
    - Single number returns the number itself
    - Multiple numbers separated by comma return their sum
    - Handles whitespace around delimiters gracefully
    """
    
    # Supported delimiters (prepared for future expansion)
    DEFAULT_DELIMITERS = [',']
    
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
            >>> calc.add("1")
            1
            >>> calc.add("1,2")
            3
            >>> calc.add("1, 2, 3")
            6
        """
        if not numbers:
            return 0
        
        number_list = self._parse_numbers(numbers)
        return sum(number_list)
    
    def _parse_numbers(self, numbers: str) -> list[int]:
        """
        Parse numbers from input string using supported delimiters.
        
        Args:
            numbers: Input string containing numbers
            
        Returns:
            List of integers parsed from string
        """
        # Check if any supported delimiter is present
        has_delimiter = any(delimiter in numbers for delimiter in self.DEFAULT_DELIMITERS)
        
        if has_delimiter:
            return self._parse_multiple_numbers(numbers)
        else:
            return self._parse_single_number(numbers)
    
    def _parse_multiple_numbers(self, numbers: str) -> list[int]:
        """
        Parse multiple numbers separated by supported delimiters.
        
        Args:
            numbers: String with delimiter-separated numbers
            
        Returns:
            List of parsed integers
        """
        # For now, handle comma delimiter only
        parts = numbers.split(',')
        result = []
        
        for part in parts:
            cleaned_part = part.strip()
            if cleaned_part:
                try:
                    result.append(int(cleaned_part))
                except ValueError:
                    # Skip invalid numbers gracefully
                    continue
        
        return result
    
    def _parse_single_number(self, numbers: str) -> list[int]:
        """
        Parse a single number from string.
        
        Args:
            numbers: String containing single number
            
        Returns:
            List with single integer or empty list if invalid
        """
        try:
            return [int(numbers.strip())]
        except ValueError:
            return []
