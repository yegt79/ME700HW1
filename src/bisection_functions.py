import numpy as np

def sort_values(x, y):
    """
    Ensures that the larger value is assigned to b and the smaller to a.
    Returns the sorted values as (a, b).
    """
    x = float(x)  # Convert x to a float
    y = float(y)  # Convert y to a float

    if x > y:
        sorted_x = y
        sorted_y = x
    else:
        sorted_x = x
        sorted_y = y
    return sorted_x, sorted_y


def calculate_mean(x, y):
    """
    Calculates the mean value of a and b.
    Returns the mean value.
    """
    return (x + y) / 2


def check_sign(x, y):
    """
    Checks if x and y have the same sign.
    Returns 1 if they have the same sign, 0 otherwise.
    """
    return 1 if np.sign(x) == np.sign(y) else 0


def reassign_ab(flag, a, b, c):
    """
    Reassigns a or b to c based on the flag value.
    If flag == 1, a = c. If flag == 0, b = c.
    Returns the new values of a and b.
    """
    if flag == 1:
        a = c
    else:
        b = c
    return a, b
