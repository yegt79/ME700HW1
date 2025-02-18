import numpy as np
import pytest
from src.newton.newton_functions import derivative_of_f, newton_method


# Test for derivative_of_f function
def test_derivative_of_f_numpy():
    """
    Test the numerical derivative function for different functions.
    """
    threshold = 0.001

    # Test 1: f(x) = x^2 - 4
    def f(x):
        return x**2 - 4
    x_value = 2
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, 4, atol=threshold)  # The derivative at x = 2 is 4

    # Test 2: f(x) = sin(x)
    def f(x):
        return np.sin(x)
    x_value = np.pi / 2
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, 0, atol=threshold)  # The derivative of sin(x) at pi/2 is 0

    # Test 3: f(x) = x^3
    def f(x):
        return x**3
    x_value = 1
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, 3, atol=threshold)  # The derivative of x^3 at x = 1 is 3

    # Test 4: f(x) = e^x
    def f(x):
        return np.exp(x)
    x_value = 0
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, 1, atol=threshold)  # The derivative of e^x at x = 0 is 1

    # Test 5: f(x) = cos(x)
    def f(x):
        return np.cos(x)
    x_value = np.pi
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, 0, atol=threshold)  # The derivative of cos(x) at x = pi is 0


# Test for newton_method function
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
    root = newton_method(f, derivative_of_f, x0)
    
    # Test if the result is correct (root = 2)
    assert np.isclose(root, 2)
