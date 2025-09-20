"""
String Calculator implementation following TDD principles.

GREEN PHASE: Minimal implementation to pass the first test.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Current implementation: Minimal code to pass empty string test.
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string.
        
        Args:
            numbers: String containing numbers
            
        Returns:
            Sum of numbers
            
        Current implementation: Only handles empty string
        """
        if numbers == "":
            return 0
        
        # This is intentionally minimal for GREEN phase
        # We'll expand this as we add more tests
        return 0  # Placeholder for future implementation
