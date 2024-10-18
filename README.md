# Decotest Python Package

Decotest is a simple and flexible Python testing framework that allows users to create unit tests with various assertions using decorators. This package is designed to streamline the process of writing and organizing tests while offering a clean and readable syntax.
Features

    Multiple assertion types (==, !=, <, >, in, is, and, or, etc.)
    Easy test registration with decorators
    Clean and structured test output
    Simple function-based testing
    Supports passing arguments to test functions

---

# Installation

To use the Decotest package, download or clone the repository into your project directory:

```bash
git clone https://github.com/your-username/decotest.git
```

Then, import the Decotest class into your script:

```python
from decotest import Decotest
```

# Usage
Basic Example

```python
from decotest import Decotest

# Initialize the Decotest instance
DECO_TEST = Decotest()

@DECO_TEST.unittest(name="Test addition")
@DECO_TEST.assert_eq(2)
def addition(x, y):
    return x + y

@DECO_TEST.unittest(name="Test exact number")
@DECO_TEST.assert_eq(30)
def number_2(x):
    return x

@DECO_TEST.unittest(name="Test if value is in list")
@DECO_TEST.assert_in(3)
def number_list():
    return [0, 5, 0]

if __name__ == "__main__":
    addition(1, 1)      # This will test if 1 + 1 == 2
    number_2(30)        # This will test if the number equals 30
    number_list()       # This will test if 3 is in the list [0, 5, 0]
    DECO_TEST.run_all_tests()
```

# In the above example:

    The @DECO_TEST.unittest decorator registers the test with a custom name.
    The @DECO_TEST.assert_?? decorators assert that the test function's return value matches a specific condition.

# Adding Tests

To add a new test:

    Define your function with its parameters.
    Use the @DECO_TEST.unittest(name="Test name") decorator to give the test a name.
    Apply the appropriate assertion decorator like assert_eq, assert_in, assert_gt, etc.

# Running Tests

All tests are executed using the DECO_TEST.run_all_tests() method, which will output the result of each test in the console.

# Assertions

Decotest provides several types of assertions, allowing flexible and expressive testing:
Equality Assertions

    assert_eq(expected_value) : Checks if the result is equal to expected_value.
    assert_neq(expected_value) : Checks if the result is not equal to expected_value.

Comparison Assertions

    assert_lt(expected_value) : Checks if the result is less than expected_value.
    assert_le(expected_value) : Checks if the result is less than or equal to expected_value.
    assert_gt(expected_value) : Checks if the result is greater than expected_value.
    assert_ge(expected_value) : Checks if the result is greater than or equal to expected_value.

Membership Assertions

    assert_in(expected_value) : Checks if expected_value is present in the result (works with iterables).
    assert_not_in(expected_value) : Checks if expected_value is not present in the result.

Identity Assertions

    assert_is(expected_value) : Checks if the result is the same object as expected_value (using is).
    assert_is_not(expected_value) : Checks if the result is not the same object as expected_value (using is not).

Logical Assertions

    assert_and(expected_value) : Checks if both expected_value and the result are True.
    assert_or(expected_value) : Checks if either expected_value or the result is True.

# Test Output

Each test provides the following output format:

```diff

+----+----+=====================
| PASS |    | Test addition
+----+----+=====================
| BAD |    | Test exact number

```
Test exact number: 30, expected value 30

    PASS: The test passed.
    BAD: The test failed, with a detailed comparison of expected and actual values.

# API Documentation
Decotest
Methods:

    unittest(name: str): Registers the function as a unit test with a custom name.

    Parameters:
        name: A string representing the name of the test.

    run_all_tests(): Runs all registered tests and outputs the results in a formatted table.

    Assertion Generators:
        assert_eq(expected_value)
        assert_neq(expected_value)
        assert_lt(expected_value)
        assert_le(expected_value)
        assert_gt(expected_value)
        assert_ge(expected_value)
        assert_in(expected_value)
        assert_not_in(expected_value)
        assert_is(expected_value)
        assert_is_not(expected_value)
        assert_and(expected_value)
        assert_or(expected_value)

Each assertion method compares the result of a test function against the expected_value.
Example

Here is an example of how you can define and run tests with the Decotest framework:

```python

from decotest import Decotest

# Create an instance of Decotest
DECO_TEST = Decotest()

# Define some test functions
@DECO_TEST.unittest(name="Test greater than")
@DECO_TEST.assert_gt(5)
def greater_test(x):
    return x

@DECO_TEST.unittest(name="Test equality")
@DECO_TEST.assert_eq(10)
def equal_test():
    return 10

if __name__ == "__main__":
    # Run the tests
    greater_test(6)
    equal_test()
    DECO_TEST.run_all_tests()
```

# License

This project is licensed under the MIT License.

Feel free to contribute, report issues, or request features by opening an issue on the repository!

Happy Testing! 🎉
