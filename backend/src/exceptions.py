"""Custom exceptions for String Calculator."""


class StringCalculatorError(Exception):
    """Base exception for String Calculator errors."""
    pass


class NegativeNumberError(StringCalculatorError):
    """Exception raised when negative numbers are provided."""
    
    def __init__(self, negatives: list[int]) -> None:
        """Initialize with list of negative numbers."""
        self.negatives = negatives
        negative_list = ", ".join(map(str, negatives))
        super().__init__(f"negative numbers not allowed: {negative_list}")


class InvalidDelimiterError(StringCalculatorError):
    """Exception raised when delimiter format is invalid."""
    pass
