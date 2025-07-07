import math

class Calculator:
    """
    A robust calculator that can perform various mathematical operations.
    """

    def __init__(self):
        self.history = []

    def add(self, num1: float, num2: float) -> float:
        """
        Adds two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The result of the addition.
        """
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result