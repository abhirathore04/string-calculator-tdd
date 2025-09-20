"""
String Calculator implementation following TDD principles.

GREEN PHASE - TDD Cycle 6: Add custom delimiter support.
"""
import re


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Features:
    - Empty string returns 0 ✅
    - Single number returns the number itself ✅
    - Multiple numbers with comma and/or newline delimiters ✅
    - Custom single character delimiters: //[delimiter]\\n[numbers...] ✅ (GREEN phase)
    """
    
    # Default delimiters
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
        
        # GREEN PHASE: Parse custom delimiters
        delimiters, numbers_part = self._parse_delimiters_and_numbers(numbers)
        number_list = self._parse_numbers(numbers_part, delimiters)
        
        return sum(number_list)
    
    def _parse_delimiters_and_numbers(self, numbers: str) -> tuple[list[str], str]:
        """
        Parse custom delimiters and extract the numbers part.
        
        Args:
            numbers: Full input string that may contain custom delimiter definition
            
        Returns:
            Tuple of (delimiters_list, numbers_string)
        """
        # GREEN PHASE: Check for custom delimiter format //[delimiter]\n
        if numbers.startswith("//"):
            # Find the newline that separates delimiter definition from numbers
            if '\n' in numbers:
                delimiter_line, numbers_part = numbers.split('\n', 1)
                # Extract delimiter (everything after //)
                custom_delimiter = delimiter_line[2:]  # Remove //
                if custom_delimiter:
                    return [custom_delimiter], numbers_part
        
        # No custom delimiter found, use defaults
        return self.DEFAULT_DELIMITERS.copy(), numbers
    
    def _parse_numbers(self, numbers_str: str, delimiters: list[str]) -> list[int]:
        """
        Parse numbers from string using provided delimiters.
        
        Args:
            numbers_str: String containing numbers
            delimiters: List of delimiter strings to use for splitting
            
        Returns:
            List of integers parsed from string
        """
        if not numbers_str:
            return []
        
        # Normalize all delimiters to commas for easier processing
        normalized = self._normalize_delimiters(numbers_str, delimiters)
        
        # Split by comma and convert to integers
        parts = normalized.split(',')
        result = []
        
        for part in parts:
            cleaned_part = part.strip()
            if cleaned_part:
                try:
                    result.append(int(cleaned_part))
                except ValueError:
                    continue
        
        return result
    
    def _normalize_delimiters(self, numbers: str, delimiters: list[str]) -> str:
        """
        Convert all provided delimiters to commas for uniform processing.
        
        Args:
            numbers: Input string with mixed delimiters
            delimiters: List of delimiters to normalize
            
        Returns:
            String with all delimiters normalized to commas
        """
        normalized = numbers
        
        # Replace all delimiters with commas
        for delimiter in delimiters:
            if delimiter != ',':  # Don't replace commas with commas
                normalized = normalized.replace(delimiter, ',')
        
        return normalized
