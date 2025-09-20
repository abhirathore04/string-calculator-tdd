"""
String Calculator implementation following TDD principles.

GREEN PHASE - TDD Cycle 5: Add newline delimiter support.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Features:
    - Empty string returns 0 ✅
    - Single number returns the number itself ✅
    - Multiple numbers with comma return their sum ✅
    - Multiple numbers with newline delimiter ✅ (GREEN phase)
    - Mixed comma and newline delimiters ✅ (GREEN phase)
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string with various delimiter support.
        
        Args:
            numbers: String containing numbers separated by commas and/or newlines
            
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
            >>> calc.add("1,2,3")
            6
            >>> calc.add("1\\n2,3")
            6
            >>> calc.add("1\\n2\\n3")
            6
        """
        # Handle empty string
        if not numbers:
            return 0
        
        # GREEN PHASE: Handle both comma and newline delimiters
        # Replace newlines with commas first, then split by comma
        normalized = numbers.replace('\n', ',')
        
        # Split by comma and sum all parts
        parts = normalized.split(',')
        total = 0
        
        for part in parts:
            cleaned_part = part.strip()
            if cleaned_part:  # Skip empty parts
                total += int(cleaned_part)
        
        return total
