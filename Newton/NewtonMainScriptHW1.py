import numpy as np
import pytest


def derivative_of_f(f, x):
    """
    Returns the numerical derivative of the function f at point x.
    Uses the finite difference method with step size h.
    """
    h = 1e-5
    return (f(x + h) - f(x)) / h


# Test function for numerical derivatives with 5 different tests
@pytest.mark.parametrize("f, x_value, expected_derivative, threshold", [
    (lambda x: x**2 - 4, 2, 4, 0.001),  # f(x) = x^2 - 4, derivative at x = 2 should be 4
    (lambda x: np.sin(x), np.pi / 2, 0, 0.001),  # f(x) = sin(x), derivative at pi/2 should be 0
    (lambda x: x**3, 1, 3, 0.001),  # f(x) = x^3, derivative at x = 1 should be 3
    (lambda x: np.exp(x), 0, 1, 0.001),  # f(x) = e^x, derivative at x = 0 should be 1
    (lambda x: np.cos(x), np.pi, 0, 0.001),  # f(x) = cos(x), derivative at x = pi should be 0
])
def test_derivative_of_f_numpy(f, x_value, expected_derivative, threshold):
    """
    Test the numerical derivative function for different functions.
    """
    f_prime = derivative_of_f(f, x_value)
    assert np.isclose(f_prime, expected_derivative, atol=threshold), \
        f"Failed for {f.__name__} at x = {x_value}, expected {expected_derivative}, got {f_prime}"


# Test for Newton's method on the function f(x) = x^2 - 4.
@pytest.mark.parametrize("f, derivative_of_f, x0, expected_root", [
    (lambda x: x**2 - 4, lambda f, x: 2*x, 3.0, 2),  # f(x) = x^2 - 4, root should be 2
])
def test_newton_method(f, derivative_of_f, x0, expected_root):
    """
    Test for Newton's method on the function f(x) = x^2 - 4.
    The root should be x = 2.
    """
    root = newton_method(f, derivative_of_f, x0)
    assert np.isclose(root, expected_root), f"Expected root: {expected_root}, got: {root}"


# --- Main Script --- to run the tests
def newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100):
    """
    Applies Newton's method to find the root of the function f(x).
    
    Args:
    f: The function whose root is to be found.
    derivative_of_f: The derivative of the function f(x).
    x0: Initial guess for the root.
    tolerance: Desired tolerance for stopping the method.
    max_iter: Maximum number of iterations allowed.
    
    Returns:
    The estimated root of the function.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = derivative_of_f(f, x)
        
        # Avoid division by zero
        if fpx == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        # Newton's method formula
        x_new = x - fx / fpx
        
        # Check if the result is within the desired tolerance
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    print("Max iterations reached. Solution may not have converged.")
    return x


if __name__ == "__main__":
    pytest.main()
