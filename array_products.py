import math
from fractions import Fraction

class Calculator:
    """
    A robust calculator that can perform various mathematical operations.

    Attributes:
        None

    Methods:
        add(x, y): Returns the sum of x and y.
        subtract(x, y): Returns the difference of x and y.
        multiply(x, y): Returns the product of x and y.
        divide(x, y): Returns the quotient of x and y.
        power(x, y): Returns x raised to the power of y.
        root(x, y): Returns the y-th root of x.
        sin(x): Returns the sine of x.
        cos(x): Returns the cosine of x.
        tan(x): Returns the tangent of x.
        log(x): Returns the natural logarithm of x.
        exp(x): Returns e raised to the power of x.
    """

    def add(self, x: complex, y: complex) -> complex:
        """
        Returns the sum of x and y.

        Args:
            x (complex): The first number.
            y (complex): The second number.

        Returns:
            complex: The sum of x and y.
        """
        return x + y

    def subtract(self, x: complex, y: complex) -> complex:
        """
        Returns the difference of x and y.

        Args:
            x (complex): The first number.
            y (complex): The second number.

        Returns:
            complex: The difference of x and y.
        """
        return x - y

    def multiply(self, x: complex, y: complex) -> complex:
        """
        Returns the product of x and y.

        Args:
            x (complex): The first number.
            y (complex): The second number.

        Returns:
            complex: The product of x and y.
        """
        return x * y

    def divide(self, x: complex, y: complex) -> complex:
        """
        Returns the quotient of x and y.

        Args:
            x (complex): The first number.
            y (complex): The second number.

        Returns:
            complex: The quotient of x and y.

        Raises:
            ZeroDivisionError: If y is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return x / y

    def power(self, x: complex, y: complex) -> complex:
        """
        Returns x raised to the power of y.

        Args:
            x (complex): The base number.
            y (complex): The exponent.

        Returns:
            complex: x raised to the power of y.
        """
        return x ** y

    def root(self, x: complex, y: complex) -> complex:
        """
        Returns the y-th root of x.

        Args:
            x (complex): The base number.
            y (complex): The root.

        Returns:
            complex: The y-th root of x.
        """
        return x ** (1 / y)

    def sin(self, x: complex) -> complex:
        """
        Returns the sine of x.

        Args:
            x (complex): The angle in radians.

        Returns:
            complex: The sine of x.
        """
        return math.sin(x)

    def cos(self, x: complex) -> complex:
        """
        Returns the cosine of x.

        Args:
            x (complex): The angle in radians.

        Returns:
            complex: The cosine of x.
        """
        return math.cos(x)

    def tan(self, x: complex) -> complex:
        """
        Returns the tangent of x.

        Args:
            x (complex): The angle in radians.

        Returns:
            complex: The tangent of x.
        """
        return math.tan(x)

    def log(self, x: complex) -> complex:
        """
        Returns the natural logarithm of x.

        Args:
            x (complex): The number.

        Returns:
            complex: The natural logarithm of x.
        """
        return math.log(x)

    def exp(self, x: complex) -> complex:
        """
        Returns e raised to the power of x.

        Args:
            x (complex): The exponent.

        Returns:
            complex: e raised to the power of x.
        """
        return math.exp(x)

    def fraction(self, x: str) -> Fraction:
        """
        Returns the fraction representation of x.

        Args:
            x (str): The fraction as a string (e.g. "1/2").

        Returns:
            Fraction: The fraction representation of x.
        """
        return Fraction(x)

    def decimal(self, x: complex) -> float:
        """
        Returns the decimal representation of x.

        Args:
            x (complex): The number.

        Returns:
            float: The decimal representation of x.
        """
        return float(x)

def main():
    calc = Calculator()

    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("11. Exponential")
        print("12. Fraction")
        print("13. Decimal")
        print("14. Quit")

        choice = input("Enter your choice (1-14): ")

        if choice == "1":
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            print(calc.add(num1, num2))
        elif choice == "2":
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            print(calc.subtract(num1, num2))
        elif choice == "3":
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            print(calc.multiply(num1, num2))
        elif choice == "4":
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            print(calc.divide(num1, num2))
        elif choice == "5":
            num1 = complex(input("Enter base number: "))
            num2 = complex(input("Enter exponent: "))
            print(calc.power(num1, num2))
        elif choice == "6":
            num1 = complex(input("Enter base number: "))
            num2 = complex(input("Enter root: "))
            print(calc.root(num1, num2))
        elif choice == "7":
            num = complex(input("Enter angle in radians: "))
            print(calc.sin(num))
        elif choice == "8":
            num = complex(input("Enter angle in radians: "))
            print(calc.cos(num))
        elif choice == "9":
            num = complex(input("Enter angle in radians: "))
            print(calc.tan(num))
        elif choice == "10":
            num = complex(input("Enter number: "))
            print(calc.log(num))
        elif choice == "11":
            num = complex(input("Enter exponent: "))
            print(calc.exp(num))
        elif choice == "12":
            num = input("Enter fraction (e.g. 1/2): ")
            print(calc.fraction(num))
        elif choice == "13":
            num = complex(input("Enter number: "))
            print(calc.decimal(num))
        elif choice == "14":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()