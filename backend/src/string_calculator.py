"""
String Calculator implementation following TDD principles.

GREEN PHASE - TDD Cycle 3: Add two numbers with comma delimiter.
"""


class StringCalculator:
    """
    A calculator that performs operations on numbers provided as strings.
    
    Features (TDD-implemented):
    - Empty string returns 0 ✅
    - Single number returns the number itself ✅
    - Two numbers with comma return their sum ✅ (GREEN phase)
    """
    
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
            >>> calc.add("10, 20")
            30
        """
        if not numbers:
            return 0
        
        number_list = self._parse_numbers(numbers)
        return sum(number_list)
    
    def _parse_numbers(self, numbers: str) -> list[int]:
        """
        Parse numbers from input string based on supported formats.
        
        Args:
            numbers: Input string containing numbers
            
        Returns:
            List of integers parsed from the string
        """
        # GREEN PHASE: Handle comma-separated numbers
        if ',' in numbers:
            # Split by comma and convert each part to integer
            parts = numbers.split(',')
            result = []
            
            for part in parts:
                # Strip whitespace and convert to integer
                cleaned_part = part.strip()
                if cleaned_part:  # Skip empty parts
                    try:
                        result.append(int(cleaned_part))
                    except ValueError:
                        # Skip invalid numbers for now
                        continue
            
            return result
        else:
            # Handle single number (existing functionality)
            try:
                return [int(numbers.strip())]
            except ValueError:
                return []
