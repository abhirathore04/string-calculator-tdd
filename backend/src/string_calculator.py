"""
String Calculator implementation following TDD principles.

REFACTOR PHASE - TDD Cycle 2: Improved structure for future expansion.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Features (TDD-implemented):
    - Empty string returns 0 ✅
    - Single number returns the number itself ✅
    - Future: Multiple numbers, custom delimiters
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string with various delimiter support.
        
        Args:
            numbers: String containing numbers separated by delimiters
            
        Returns:
            Sum of all valid numbers
            
        Raises:
            ValueError: If number format is invalid (future implementation)
            
        Examples:
            >>> calc = StringCalculator()
            >>> calc.add("")
            0
            >>> calc.add("1")
            1
            >>> calc.add("42")
            42
        """
        # Handle empty string
        if not numbers:
            return 0
        
        # Parse numbers from input string
        number_list = self._parse_numbers(numbers)
        
        # Return sum of all parsed numbers
        return sum(number_list)
    
    def _parse_numbers(self, numbers: str) -> list[int]:
        """
        Parse numbers from input string based on supported formats.
        
        Args:
            numbers: Input string containing numbers
            
        Returns:
            List of integers parsed from the string
            
        Current Implementation:
        - Single number: ["42"] from "42"
        - Future: Multiple numbers with delimiters
        """
        # REFACTOR: Extract parsing logic for better separation of concerns
        # Current: Handle single number only
        try:
            return [int(numbers.strip())]
        except ValueError:
            # Future: Handle parsing errors appropriately
            return []
