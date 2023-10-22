def is_input_number(num_f, num_s):
    return isinstance(num_f, (int, float)) and isinstance(num_s, (int, float))

def is_divisor_zero(divisor):
    return divisor == 0

def add(num_f, num_s):
    if not is_input_number(num_f, num_s):
        raise TypeError("Both inputs must be numbers")
    return num_f + num_s

def subtract(num_f, num_s):
    if not is_input_number(num_f, num_s):
        raise TypeError("Both inputs must be numbers")
    return num_f - num_s

def multiply(num_f, num_s):
    if not is_input_number(num_f, num_s):
        raise TypeError("Both inputs must be numbers")
    return num_f * num_s

def divide(num_f, divisor):
    if not is_input_number(num_f, divisor):
        raise TypeError("Both inputs must be numbers")
    if is_divisor_zero(divisor):
        raise ValueError("Division by 0 is not allowed")
    return num_f / divisor