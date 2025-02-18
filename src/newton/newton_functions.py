import numpy as np


def derivative_of_f(f, x):
    """
    Returns the numerical derivative of the function f at point x.
    Uses the finite difference method with step size h.
    """
    h = 1e-5
    return (f(x + h) - f(x)) / h


def newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100):
    """
    Applies Newton's method to find the root of the function f(x).
    
    Args:
    f: The function whose root is to be found.
    f_prime: The derivative of the function f(x).
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
