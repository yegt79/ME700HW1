import numpy as np
import bisection_functions as bf

# Example 1: Root of x - 4
def f1(x):
    return x - 4

a, b = bf.sort_values(9, -3)
threshold = 0.01
iteration = 0

while True:
    iteration += 1
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break
    
    c = bf.calculate_mean(a, b)
    fa, fb, fc = f1(a), f1(b), f1(c)
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    flag = bf.check_sign(fc, fa)
    a, b = bf.reassign_ab(flag, a, b, c)

# Example 2: Root of x^3 + 8
def f2(x):
    return x**3 + 8

a, b = bf.sort_values(11, -10)
iteration = 0

while True:
    iteration += 1
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break
    
    c = bf.calculate_mean(a, b)
    fa, fb, fc = f2(a), f2(b), f2(c)
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    flag = bf.check_sign(fc, fa)
    a, b = bf.reassign_ab(flag, a, b, c)

# Example 3: Root of 10 * log10(x)
def f3(x):
    return 10 * np.log10(x)

a, b = bf.sort_values(0, 60)
iteration = 0

while True:
    iteration += 1
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break
    
    c = bf.calculate_mean(a, b)
    fa, fb, fc = f3(a), f3(b), f3(c)
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    flag = bf.check_sign(fc, fa)
    a, b = bf.reassign_ab(flag, a, b, c)

# Example 4: Nonlinear Equation
def f4(e):
    return sigma - E * (1 + alpha * e) * e

E = 2e11
alpha = 0.01
sigma = 50000
a, b = bf.sort_values(7, 0)
iteration = 0

while True:
    iteration += 1
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break
    
    c = bf.calculate_mean(a, b)
    fa, fb, fc = f4(a), f4(b), f4(c)
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    flag = bf.check_sign(fc, fa)
    a, b = bf.reassign_ab(flag, a, b, c)

# Example 5: Root of C - P * v^n
def f5(v):
    return C - P * v**n

P = 50000
C = 200000
n = 1.4
a, b = bf.sort_values(0, 5)
iteration = 0

while True:
    iteration += 1
    if iteration > 200:
        print("Breaking the loop after 200 iterations")
        break
    
    c = bf.calculate_mean(a, b)
    fa, fb, fc = f5(a), f5(b), f5(c)
    print(f"a = {a}, b = {b}, c = {c}, f(a) = {fa}, f(b) = {fb}, f(c) = {fc}")
    
    if abs(fc) < threshold:
        print(f"Root found at c = {c} with f(c) = {fc}")
        break
    
    flag = bf.check_sign(fc, fa)
    a, b = bf.reassign_ab(flag, a, b, c)
