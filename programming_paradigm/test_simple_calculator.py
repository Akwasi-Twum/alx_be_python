import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "2 + 3 should equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "-1 + 1 should equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "0 + 0 should equal 0")
        self.assertEqual(self.calc.add(-5, -3), -8, "-5 + -3 should equal -8")
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "2.5 + 3.5 should equal 6.0")

    def test_subtract(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "5 - 3 should equal 2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "-1 - 1 should equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "0 - 0 should equal 0")
        self.assertEqual(self.calc.subtract(-5, -3), -2, "-5 - -3 should equal -2")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "5.5 - 2.5 should equal 3.0")

    def test_multiply(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "2 * 3 should equal 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "-2 * 3 should equal -6")
        self.assertEqual(self.calc.multiply(0, 100), 0, "0 * 100 should equal 0")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "-2 * -3 should equal 6")
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0, "2.5 * 2.0 should equal 5.0")

    def test_divide(self):
        """Test the divide method with normal and edge cases."""
        self.assertEqual(self.calc.divide(10, 5), 2.0, "10 / 5 should equal 2.0")
        self.assertEqual(self.calc.divide(-10, 5), -2.0, "-10 / 5 should equal -2.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "0 / 5 should equal 0.0")
        self.assertEqual(self.calc

If any test fails, `unittest` will provide details about the failure, including the assertion message (e.g., `"2 + 3 should equal 5"`).

---

### Integration with Previous Tasks

The project includes three tasks so far:
1. **Task 0: Create a Simple Bank Account Class** (OOP and command-line interaction)
   - Files: `bank_account.py`, `main-0.py`
   - Focus: Encapsulation, class methods, command-line arguments
2. **Task 1: Robust Division Calculator** (exception handling)
   - Files: `robust_division_calculator.py`, `main.py`
   - Focus: `try-except`, `ValueError`, `ZeroDivisionError`
3. **Task 2: Writing Unit Tests for a Simple Calculator Class** (unit testing)
   - Files: `simple_calculator.py` (provided), `test_simple_calculator.py`
   - Focus: Unit testing with `unittest`, edge cases

The unit tests for Task 2 align with the project objective of writing basic unit tests using `unittest`. The tests provided above cover normal and edge cases, fulfilling the requirement to “think like a tester.”

---

### Submission Guidance

To prepare for the project deadline (June 16, 2025, 12:00 AM):
1. **File Structure**:
   - Place the following files in the `programming_paradigm` directory of your `alx_be_python` GitHub repository:
     - `bank_account.py`
     - `main-0.py`
     - `robust_division_calculator.py`
     - `main.py`
     - `simple_calculator.py` (provided)
     - `test_simple_calculator.py`
   - If unit tests for Tasks 0 and 1 are required, include:
     - `test_bank_account.py` (from previous response)
     - `test_robust_division_calculator.py` (from previous response)

2. **Test Locally**:
   - **Task 0**:
     ```bash
     python main-0.py deposit:50
     python main-0.py withdraw:20
     python main-0.py withdraw:150
     python main-0.py display
     ```
   - **Task 1**:
     ```bash
     python main.py 10 5
     python main.py 10 0
     python main.py ten  student: 5
     ```
   - **Task 2**:
     ```bash
     python -m unittest test_simple_calculator.py
     ```
   - Optionally, test Tasks 0 and 1 with their unit test scripts:
     ```bash
     python -m unittest test_bank_account.py
     python -m unittest test_robust_division_calculator.py
     ```

3. **Check PEP 8 Compliance**:
   ```bash
   pycodestyle bank_account.py main-0.py robust_division_calculator.py main.py simple_calculator.py test_simple_calculator.py
# simple_calculator.py (modified)
class DivisionByZeroError(Exception):
    pass

class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b
   
def test_divide(self):
    self.assertEqual(self.calc.divide(10, 5), 2.0, "10 / 5 should equal 2.0")
    self.assertEqual(self.calc.divide(-10, 5), -2.0, "-10 / 5 should equal -2.0")
    self.assertEqual(self.calc.divide(0, 5), 0.0, "0 / 5 should equal 0.0")
    self.assertEqual(self.calc.divide(7.5, 2.5), 3.0, "7.5 / 2.5 should equal 3.0")
    self.assertEqual(self.calc.divide(-6, -3), 2.0, "-6 / -3 should equal 2.0")
    with self.assertRaises(DivisionByZeroError):
        self.calc.divide(10, 0)
