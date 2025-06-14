def safe_divide(numerator, denominator):
    """Perform division with error handling for non-numeric inputs and division by zero."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
import sys
from robust_division_calculator import safe_divide

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Extract numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call safe_divide and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
import unittest
from bank_account import BankAccount
from io import StringIO
import sys

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up a new BankAccount instance before each test."""
        self.account = BankAccount(100)

    def test_deposit_positive_amount(self):
        """Test depositing a positive amount."""
        self.account.deposit(50)
        self.assertEqual(self.account._account_balance, 150.0)

    def test_deposit_zero_or_negative(self):
        """Test that depositing zero or negative does not change balance."""
        initial_balance = self.account._account_balance
        self.account.deposit(0)
        self.assertEqual(self.account._account_balance, initial_balance)
        self.account.deposit(-50)
        self.assertEqual(self.account._account_balance, initial_balance)

    def test_withdraw_sufficient_funds(self):
        """Test withdrawing with sufficient funds."""
        result = self.account.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.account._account_balance, 50.0)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing with insufficient funds."""
        result = self.account.withdraw(150)
        self.assertFalse(result)
        self.assertEqual(self.account._account_balance, 100.0)

    def test_withdraw_zero_or_negative(self):
        """Test that withdrawing zero or negative does not change balance."""
        initial_balance = self.account._account_balance
        result = self.account.withdraw(0)
        self.assertFalse(result)
        self.assertEqual(self.account._account_balance, initial_balance)
        result = self.account.withdraw(-50)
        self.assertFalse(result)
        self.assertEqual(self.account._account_balance, initial_balance)

    def test_display_balance(self):
        """Test display_balance outputs correct format."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.display_balance()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Current Balance: $100.00")

if __name__ == "__main__":
    unittest.main()
    import unittest
from robust_division_calculator import safe_divide

class TestSafeDivide(unittest.TestCase):
    def test_normal_division(self):
        """Test normal division cases."""
        self.assertEqual(safe_divide("10", "5"), "The result of the division is 2.0")
        self.assertEqual(safe_divide("7.5", "2.5"), "The result of the division is 3.0")
        self.assertEqual(safe_divide("-10", "5"), "The result of the division is -2.0")

    def test_division_by_zero(self):
        """Test division by zero."""
        self.assertEqual(safe_divide("10", "0"), "Error: Cannot divide by zero.")

    def test_non_numeric_input(self):
        """Test non-numeric inputs."""
        self.assertEqual(safe_divide("ten", "5"), "Error: Please enter numeric values only.")
        self.assertEqual(safe_divide("10", "abc"), "Error: Please enter numeric values only.")
        self.assertEqual(safe_divide("", "5"), "Error: Please enter numeric values only.")

if __name__ == "__main__":
    unittest.main()
