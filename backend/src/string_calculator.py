"""
String Calculator implementation following TDD principles.

REFACTOR PHASE - TDD Cycle 5: Clean, maintainable implementation.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Supported Features:
    - Empty string returns 0
    - Single number returns the number itself
    - Multiple numbers with comma and/or newline delimiters
    - Handles whitespace gracefully
    - Unlimited amount of numbers
    """
    
    # Supported delimiters
    DEFAULT_DELIMITERS = [',', '\n']
    
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
            >>> calc.add("1,2,3")
            6
            >>> calc.add("1\\n2\\n3")
            6
            >>> calc.add("1\\n2,3")
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
        # Normalize all delimiters to commas for easier processing
        normalized = self._normalize_delimiters(numbers)
        
        # Split by comma and convert to integers
        parts = normalized.split(',')
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
    
    def _normalize_delimiters(self, numbers: str) -> str:
        """
        Convert all supported delimiters to commas for uniform processing.
        
        Args:
            numbers: Input string with mixed delimiters
            
        Returns:
            String with all delimiters normalized to commas
        """
        normalized = numbers
        
        # Replace all supported delimiters with commas
        for delimiter in self.DEFAULT_DELIMITERS:
            if delimiter != ',':  # Don't replace commas with commas
                normalized = normalized.replace(delimiter, ',')
        
        return normalized
