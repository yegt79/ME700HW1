# Newton's Method Implementation

This repository contains Python scripts demonstrating the implementation of Newton's method for finding roots of equations. The main script provides the core functions, while individual examples apply the method to different mathematical functions.

## Files Overview

- **NewtonMainScriptHW1.py**

  - Implements Newton's method for root-finding.
  - Includes a function for numerical differentiation using the finite difference method.
  - Contains test functions for verification.

- **Example1Newton.py**

  - Applies Newton's method to the function \(f(x) = x - 4\).
  - Initial guess: \(x_0 = 3\).

- **Example2Newton.py**

  - Applies Newton's method to the function \(f(x) = x^2 - 100\).
  - Initial guess: \(x_0 = 5\).

- **Example3Newton.py**

  - Applies Newton's method to \(f(x) = \sin(x)\).
  - Initial guess: \(x_0 = 1\).

- **Example4MechNewton.py**

  - Applies Newton's method to a nonlinear mechanical equation related to material behavior under stress:
    \[
    f(e) = \sigma - E(1 + \alpha e)e
    \]
  - Uses predefined material constants (Young’s modulus, applied stress, and material constant).
  - Initial guess: \(e_0 = 0\).

## Usage

1. Ensure **Python 3** and **NumPy** are installed.
2. Run any of the example scripts to see Newton's method in action:
   ```bash
   python Example1Newton.py
   ```

## Notes

- The **derivative function** is computed numerically, which may introduce small errors.
- The method may fail if the derivative is zero at any step.

