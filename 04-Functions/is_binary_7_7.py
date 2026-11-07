def f(binary_number):
    if not binary_number:
        return False

    for digit in binary_number:
        if digit not in '01':
            return False
    return True
        