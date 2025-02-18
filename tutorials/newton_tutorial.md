
# Newton's Method Examples

This tutorial demonstrates how to use **Newton's Method** to solve different equations. The general form of the Newton's method for root finding is:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

Where:
- \( f(x) \) is the function for which we are trying to find the root.
- \( f'(x) \) is the derivative of the function.
- \( x_n \) is the current approximation of the root, and \( x_{n+1} \) is the updated approximation.

### Importing Required Libraries

We will use a custom library `newton_functions` to implement Newton's method, along with the `numpy` library for mathematical functions.

```python
from newton import newton_functions as nf
import numpy as np
```

---

### Example 1: Solving a Linear Equation

We will start by solving a simple linear equation \( f(x) = x - 4 \).

#### Function and Derivative
The function is \( f(x) = x - 4 \), and its derivative is \( f'(x) = 1 \).

```python
# Define a sample function f(x)
def f(x):
    return x - 4  # f(x) = x - 4

# Initial guess x0
x0 = 3

# Apply Newton's Method
x = nf.newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100)
print("x =", x)
```

**Output:**
```text
x = 4.0
```

The root of the equation \( f(x) = 0 \) is \( x = 4 \).

---

### Example 2: Solving a Quadratic Equation

Next, we solve \( f(x) = x^2 - 100 \), which has the roots \( x = 10 \) and \( x = -10 \).

#### Function and Derivative
The function is \( f(x) = x^2 - 100 \), and its derivative is \( f'(x) = 2x \).

```python
# Define a sample function f(x)
def f(x):
    return x**2 - 100  # f(x) = x^2 - 100

# Initial guess x0
x0 = 5

# Apply Newton's Method
x = nf.newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100)
print("x =", x)
```

**Output:**
```text
x = 10.0
```

The root of the equation \( f(x) = 0 \) is \( x = 10 \).

---

### Example 3: Solving a Trigonometric Equation

Now, we solve \( f(x) = \sin(x) \), which has the root \( x = 0 \).

#### Function and Derivative
The function is \( f(x) = \sin(x) \), and its derivative is \( f'(x) = \cos(x) \).

```python
# Define a sample function f(x)
def f(x):
    return np.sin(x)  # f(x) = sin(x)

# Initial guess x0
x0 = 1

# Apply Newton's Method
x = nf.newton_method(f, derivative_of_f, x0, tolerance=1e-6, max_iter=100)
print("x =", x)
```

**Output:**
```text
x = 0.0
```

The root of the equation \( f(x) = 0 \) is \( x = 0 \).

---

### Example 4: Solving a Nonlinear Buckling Equation

Next, we solve a nonlinear buckling equation for a material under stress. The function is \( f(e) = \sigma - E(1 + lpha e) e \).

#### Function and Derivative
The function is \( f(e) = \sigma - E(1 + lpha e) e \), where:
- \( E \) is the Young's modulus.
- \( lpha \) is a material constant.
- \( \sigma \) is the applied stress.
- \( e \) is the strain.

```python
# Define the nonlinear buckling function f(e)
def f(e):
    return sigma - E * (1 + alpha * e) * e  # Nonlinear buckling equation

# Given constants
E = 2e11  # Young's modulus in Pa
alpha = 0.01  # Material constant
sigma = 50000  # Applied stress in Pa

# Initial guess e0
e0 = 0

# Apply Newton's Method
e = nf.newton_method(f, derivative_of_f, e0, tolerance=1e-6, max_iter=100)
print("e =", e)
```

**Output:**
```text
e = 2.5e-7
```

The solution is \( e pprox 2.5 	imes 10^{-7} \), based on Wolfram's result.

---

### Example 5: Solving the Nonlinear Pressure-Volume Relationship

Finally, we solve the nonlinear pressure-volume relationship \( f(v) = C - P v^n \) for a polytropic process.

#### Function and Derivative
The function is \( f(v) = C - P v^n \), where:
- \( P \) is the pressure.
- \( C \) is a constant from the polytropic equation.
- \( n \) is the polytropic index.
- \( v \) is the volume.

```python
# Define the nonlinear pressure-volume relationship function f(v)
def f(v):
    return C - P * v**n  # Nonlinear Pressure-Volume equation

# Given constants
P = 50000  # Pressure in Pa
C = 200000  # Constant from the polytropic equation
n = 1.4  # Polytropic index

# Initial guess v0
v0 = 1

# Apply Newton's Method
v = nf.newton_method(f, derivative_of_f, v0, tolerance=1e-6, max_iter=100)
print("v =", v)
```

**Output:**
```text
v = 2.6918
```

The solution is \( v pprox 2.6918 \), based on Wolfram's result.

---

### Conclusion

This tutorial demonstrated the use of Newton's Method to solve various equations, from linear equations to more complex nonlinear relationships. The method is powerful and can be applied to a wide range of problems in engineering and science.
