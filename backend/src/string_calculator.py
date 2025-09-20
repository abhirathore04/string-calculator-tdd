"""
String Calculator implementation following TDD principles.

GREEN PHASE - TDD Cycle 2: Minimal implementation for single numbers.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Current Features (TDD-driven):
    - Empty string returns 0 ✅ (Step 1)
    - Single number returns the number itself ✅ (Step 2 - GREEN phase)
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string with various delimiter support.
        
        Args:
            numbers: String containing numbers separated by delimiters
            
        Returns:
            Sum of all valid numbers
            
        Current Implementation:
        - Empty string: returns 0
        - Single number: returns the number as integer
        
        Examples:
            >>> calc = StringCalculator()
            >>> calc.add("")
            0
            >>> calc.add("1")
            1
            >>> calc.add("42")
            42
        """
        # Handle empty string (Step 1)
        if not numbers:
            return 0
        
        # GREEN PHASE: Handle single number (Step 2)
        # Minimal implementation to pass current tests
        try:
            # Convert entire string to integer
            return int(numbers)
        except ValueError:
            # If conversion fails, return 0 for now
            # Future: Handle multiple numbers with delimiters
            return 0
