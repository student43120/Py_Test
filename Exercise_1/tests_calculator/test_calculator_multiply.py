import pytest
from calculator import multiply

##MULTIPLY FUNCTION-------------------------------------------------
#-------------------------------------------------
test_cases_multiply_one_int = [
    (0, 1, 0),
    (-0, -1, 0),
    (1, -0, 0),
    (-1, 0, 0),
    (6, 1, 6),
    (-6, 1, -6),
    (6, -1, -6),
    (-6, -1, 6),
    (1, 9, 9),
    (1, -9, -9),
    (-1, 9, -9),
    (-1, -9, 9)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_one_int) 
def test_multiply_one_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_zero_int = [
    (0, 0, 0),
    (-0, -0, 0),
    (0, -0, 0),
    (-0, 0, 0),
    (6, 0, 0),
    (-6, 0, 0),
    (6, -0, 0),
    (-6, -0, 0),
    (0, 9, 0),
    (0, -9, 0),
    (-0, 9, 0),
    (-0, -9, 0)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_zero_int)
def test_multiply_zero_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_int = [
    (6, 9, 54),
    (-6, -9, 54),
    (-6, 9, -54),
    (6, -9, -54)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_int)
def test_multiply_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_one_float = [
    (0.0, 1.0, 0.0),
    (1.0, 0.0, 0.0),
    (-0.0, 1.0, 0.0),
    (-0.0, -1.0, 0.0),
    (0.0, -1.0, 0.0),
    (2.5, 1.0, 2.5),
    (-2.5, 1.0, -2.5),
    (2.5, -1.0, -2.5),
    (-2.5, -1.0, 2.5),
    (1.0, 4.5, 4.5),
    (1.0, -4.5, -4.5),
    (-1.0, 4.5, -4.5),
    (-1.0, -4.5, 4.5)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_one_float)
def test_multiply_one_float(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_zero_float = [
    (0.0, 0.0, 0.0),
    (-0.0, 0.0, 0.0),
    (-0.0, -0.0, 0.0),
    (0.0, -0.0, 0.0),
    (2.5, 0.0, 0.0),
    (-2.5, 0.0, 0.0),
    (2.5, -0.0, 0.0),
    (-2.5, -0.0, 0.0),
    (0.0, 4.5, 0.0),
    (0.0, -4.5, 0.0),
    (-0.0, 4.5, 0.0),
    (-0.0, -4.5, 0.0)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_zero_float)
def test_multiply_zero_float(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_float = [
    (2.5, 4.5, 11.25),
    (-2.5, -4.5, 11.25),
    (-2.5, 4.5, -11.25),
    (2.5, -4.5, -11.25)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_float)
def test_multiply_float(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_one_float_and_int = [
    (0.0, 1, 0.0),
    (0.0, -1, 0.0),
    (-0.0, -1, 0.0),
    (-0.0, 1, 0.0),
    (-0, 1.0, 0.0),
    (0, -1.0, 0.0),
    (0, 1.0, 0.0),
    (-0, -1.0, 0.0),
    (2, 1.0, 2.0),
    (-2, 1.0, -2.0),
    (2, -1.0, -2.0),
    (-2, -1.0, 2.0),
    (1.0, 2, 2.0),
    (-1.0, 2, -2.0),
    (1.0, -2, -2.0),
    (-1.0, -2, 2.0),
    (1, 2.0, 2.0),
    (1, -2.0, -2.0),
    (2.5, 1, 2.5),
    (2.5, -1, -2.5),
    (-2.5, -1, 2.5),
    (-2.5, 1, -2.5),
    (1, 2.5, 2.5),
    (1, -2.5, -2.5)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_one_float_and_int)
def test_multiply_one_float_and_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_zero_float_and_int = [
    (0.0, 0, 0.0),
    (-0.0, -0, 0.0),
    (-0, 0.0, 0.0),
    (0, -0.0, 0.0),
    (0.0, 1, 0.0),
    (0.0, -1, 0.0),
    (0.0, 2, 0.0),
    (0.0, -2, 0.0),
    (0, 1.0, 0.0),
    (0, -1.0, 0.0),
    (0, 2.0, 0.0),
    (0, -2.0, 0.0),
    (2.5, 0, 0.0),
    (-2.5, 0, 0.0),
    (0, 2.5, 0.0),
    (0, -2.5, 0.0)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_zero_float_and_int)
def test_multiply_zero_float_and_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_float_and_int = [
    (5.5, 5, 27.5),
    (-5.5, -5, 27.5),
    (-5, 5.5, -27.5),
    (5, -5.5, -27.5),
    (2, 4.0, 8.0),
    (-2, 4.0, -8.0),
    (2, -4.0, -8.0),
    (-2, -4.0, 8.0),
    (4.0, 2, 8.0),
    (-4.0, 2, -8.0),
    (4.0, -2, -8.0),
    (-4.0, -2, 8.0)
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_float_and_int)
def test_multiply_float_and_int(num_f, num_s, expected):
        assert multiply(num_f, num_s) == expected

#-------------------------------------------------
test_cases_multiply_negativ = [
    ("1", "2", pytest.raises(TypeError)),
    ([1], [2], pytest.raises(TypeError)),
    (1, "2", pytest.raises(TypeError)),
    (1, [2], pytest.raises(TypeError)),
    ("1", 2, pytest.raises(TypeError)),
    ([1], 2, pytest.raises(TypeError)) 
]

@pytest.mark.parametrize("num_f, num_s, expected", test_cases_multiply_negativ)
def test_multiply_negativ(num_f, num_s, expected):
        with expected:
            multiply(num_f, num_s)

#-------------------------------------------------
test_cases_multiply_input_types = [
   (6, 9),
   (6.5, 2.5),
   (6.5, 9)  
]

@pytest.mark.parametrize("num_f, num_s", test_cases_multiply_input_types)
def test_multiply_input_types(num_f, num_s):
        assert isinstance(multiply(num_f, num_s), (int, float))

#-------------------------------------------------