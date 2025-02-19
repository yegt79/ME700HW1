import pytest
import numpy as np
import bisection_functions as bf

def test_sort_values():
    # Test 1: Positive and negative numbers
    a = 10
    b = -5
    sorted_a, sorted_b = bf.sort_values(a, b)
    assert np.isclose(sorted_a, -5)
    assert np.isclose(sorted_b, 10)

    # Test 2: Both positive numbers
    a = 20
    b = 30
    sorted_a, sorted_b = bf.sort_values(a, b)
    assert np.isclose(sorted_a, 20)
    assert np.isclose(sorted_b, 30)

    # Test 3: Both negative numbers
    a = -10
    b = -20
    sorted_a, sorted_b = bf.sort_values(a, b)
    assert np.isclose(sorted_a, -20)
    assert np.isclose(sorted_b, -10)

    # Test 4: Zero and positive number
    a = 0
    b = 5
    sorted_a, sorted_b = bf.sort_values(a, b)
    assert np.isclose(sorted_a, 0)
    assert np.isclose(sorted_b, 5)

    # Test 5: Zero and negative number
    a = 0
    b = -5
    sorted_a, sorted_b = bf.sort_values(a, b)
    assert np.isclose(sorted_a, -5)
    assert np.isclose(sorted_b, 0)

def test_calculate_mean():
    # Test 1: Positive values
    a = 10
    b = 20
    mean = bf.calculate_mean(a, b)
    assert np.isclose(mean, 15)

    # Test 2: Negative values
    a = -10
    b = -20
    mean = bf.calculate_mean(a, b)
    assert np.isclose(mean, -15)

    # Test 3: Zero and positive value
    a = 0
    b = 10
    mean = bf.calculate_mean(a, b)
    assert np.isclose(mean, 5)

    # Test 4: Zero and negative value
    a = 0
    b = -10
    mean = bf.calculate_mean(a, b)
    assert np.isclose(mean, -5)

    # Test 5: Equal values
    a = 5
    b = 5
    mean = bf.calculate_mean(a, b)
    assert np.isclose(mean, 5)

def test_check_sign():
    # Test 1: Same sign, both positive
    x = 10
    y = 20
    flag = bf.check_sign(x, y)
    assert np.isclose(flag, 1)

    # Test 2: Different sign
    x = -10
    y = 20
    flag = bf.check_sign(x, y)
    assert np.isclose(flag, 0)

    # Test 3: Both negative
    x = -5
    y = -10
    flag = bf.check_sign(x, y)
    assert np.isclose(flag, 1)

    # Test 4: One positive and one negative
    x = -10
    y = 5
    flag = bf.check_sign(x, y)
    assert np.isclose(flag, 0)

    # Test 5: Both zero
    x = 0
    y = 0
    flag = bf.check_sign(x, y)
    assert np.isclose(flag, 1)

def test_reassign_ab():
    # Test 1: Flag = 1 (assign c to a)
    flag = 1
    a = 10
    b = 5
    c = 7
    new_a, new_b = bf.reassign_ab(flag, a, b, c)
    assert np.isclose(new_a, 7)
    assert np.isclose(new_b, 5)

    # Test 2: Flag = 0 (assign c to b)
    flag = 0
    a = 10
    b = 5
    c = 7
    new_a, new_b = bf.reassign_ab(flag, a, b, c)
    assert np.isclose(new_a, 10)
    assert np.isclose(new_b, 7)

    # Test 3: Assign a to c when flag is 1
    flag = 1
    a = 3
    b = 6
    c = 9
    new_a, new_b = bf.reassign_ab(flag, a, b, c)
    assert np.isclose(new_a, 9)
    assert np.isclose(new_b, 6)

    # Test 4: Assign b to c when flag is 0
    flag = 0
    a = 5
    b = 8
    c = 10
    new_a, new_b = bf.reassign_ab(flag, a, b, c)
    assert np.isclose(new_a, 5)
    assert np.isclose(new_b, 10)

    # Test 5: Test with zero
    flag = 1
    a = 0
    b = 8
    c = 10
    new_a, new_b = bf.reassign_ab(flag, a, b, c)
    assert np.isclose(new_a, 10)
    assert np.isclose(new_b, 8)

# Print if all tests pass
def run_all_tests():
    pytest.main()
    print("All tests successful!")

# Uncomment this line to run the tests and print the success message
run_all_tests()
