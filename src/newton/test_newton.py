import pytest
import newton_functions as nf
import numpy as np


# Test the derivative_of_f function
@pytest.mark.parametrize("func, x_value, expected_derivative", [
    (lambda x: x**2 - 4, 2, 4),  # f(x) = x^2 - 4, derivative at x=2 is 4
    (lambda x: np.sin(x), np.pi / 2, 0),  # f(x) = sin(x), derivative at x=pi/2 is 0
    (lambda x: x**3, 1, 3),  # f(x) = x^3, derivative at x=1 is 3
    (lambda x: np.exp(x), 0, 1),  # f(x) = e^x, derivative at x=0 is 1
    (lambda x: np.cos(x), np.pi, 0),  # f(x) = cos(x), derivative at x=pi is 0
])
def test_derivative_of_f(func, x_value, expected_derivative):
    result = nf.derivative_of_f(func, x_value)
    assert np.isclose(result, expected_derivative, atol=1e-3)


# Test Newton's method
def test_newton_method():
    """
    Test for Newton's method on the function f(x) = x^2 - 4.
    The root should be x = 2.
    """
    
    # Define the function and its derivative
    def f(x):
        return x**2 - 4
    
    def derivative_of_f(f, x):
        return 2*x
    
    # Initial guess
    x0 = 3.0
    
    # Apply Newton's method
    root = nf.newton_method(f, derivative_of_f, x0)
    
    # Test if the result is correct (root = 2)
    assert np.isclose(root, 2, atol=1e-6)

# Print if all tests pass
def run_all_tests():
    pytest.main()
    print("All tests successful!")

# Uncomment this line to run the tests and print the success message
run_all_tests()
