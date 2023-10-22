import pytest
from calculator import divide

##DIVIDE FUNCTION-------------------------------------------------
#-------------------------------------------------
test_cases_divide_one_int = [
    ( 1, 1, 1),
    (-1, -1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (6, 1, 6),
    (-6, 1, -6),
    (6, -1, -6),
    (-6, -1, 6),
    (0, -1, 0),
    (-0, -1, 0)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_one_int)
def test_divide_one_int(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_division_by_zero_int = [
    (0, 0, pytest.raises(ValueError)),
    (-0, -0, pytest.raises(ValueError)),
    (0, -0, pytest.raises(ValueError)),
    (-0, 0, pytest.raises(ValueError)),
    (6, 0, pytest.raises(ValueError)),
    (-6, 0, pytest.raises(ValueError)),
    (6, -0, pytest.raises(ValueError)),
    (-6, -0, pytest.raises(ValueError))
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_division_by_zero_int)
def test_divide_division_by_zero_int(num_f, divisor, expected):
        with expected:
            divide(num_f, divisor)

#-------------------------------------------------
test_cases_divide_zero_int = [
    (0, 9, 0),
    (0, -9, 0),
    (-0, 9, 0),
    (-0, -9, 0),
    (0, 9, 0),
    (0, -9, 0),
    (-0, 9, 0),
    (-0, -9, 0)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_zero_int)
def test_divide_zero_int(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_int = [
    (6, 9, 0.666_666_666_666_666_6),
    (-6, -9, 0.666_666_666_666_666_6),
    (-6, 9, -0.666_666_666_666_666_6),
    (6, -9, -0.666_666_666_666_666_6)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_int)
def test_divide_int(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_one_float = [
    (1, 1.0, 1.0),
    (1.0, 1, 1.0),
    (-1.0, -1, 1.0),
    (-1, -1.0, 1.0),
    (1.0, -1, -1.0),
    (1, -1.0, -1.0),
    (-1.0, 1, -1.0),
    (-1, 1.0, -1.0),
    (6.0, 1, 6.0),
    (6, 1.0, 6.0),
    (-6.0, 1, -6.0),
    (6, -1.0, -6.0),
    (-6.0, -1, 6.0),
    (-6, -1.0, 6.0),
    (0.0, -1, 0.0),
    (0, -1.0, 0.0),
    (-0.0, -1, 0.0),
    (-0, -1.0, 0.0)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_one_float)
def test_divide_one_float(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_division_by_zero_float = [
    (0.0, 0.0, pytest.raises(ValueError)),
    (-0.0, -0.0, pytest.raises(ValueError)),
    (0.0, -0.0, pytest.raises(ValueError)),
    (-0.0, 0.0, pytest.raises(ValueError)),
    (6.0, 0.0, pytest.raises(ValueError)),
    (-6.0, 0.0, pytest.raises(ValueError)),
    (6.0, -0.0, pytest.raises(ValueError)),
    (-6.0, -0.0, pytest.raises(ValueError)),
    (2.5, 0.0, pytest.raises(ValueError)),
    (-2.5, 0.0, pytest.raises(ValueError)),
    (2.5, -0.0, pytest.raises(ValueError)),
    (-2.5, -0.0, pytest.raises(ValueError))
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_division_by_zero_float)
def test_divide_division_by_zero_float(num_f, divisor, expected):
        with expected:
            divide(num_f, divisor)

#-------------------------------------------------
test_cases_divide_zero_float = [
    (0.0, 4.5, 0.0),
    (0.0, -4.5, 0.0),
    (-0.0, 4.5, 0.0),
    (-0.0, -4.5, 0.0)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_zero_float)
def test_divide_zero_float(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected
 
 #-------------------------------------------------   
test_cases_divide_float = [
    (2.5, 4.5, 0.555_555_555_555_555_6),
    (-2.5, -4.5, 0.555_555_555_555_555_6),
    (-2.5, 4.5, -0.555_555_555_555_555_6),
    (2.5, -4.5, -0.555_555_555_555_555_6)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_float)
def test_divide_float(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_one_float_and_int = [
    (2, 1.0, 2.0),
    (-2, 1.0, -2.0),
    (2, -1.0, -2.0),
    (-2, -1.0, 2.0),
    (1.0, 2, 0.5),
    (-1.0, 2, -0.5),
    (1.0, -2, -0.5),
    (-1.0, -2, 0.5),
    (0.0, 1, 0.0),
    (0.0, -1, 0.0),
    (0, 1.0, 0.0),
    (0, -1.0, 0.0),
    (2.5, 1, 2.5),
    (-2.5, -1, 2.5),
    (-2.5, 1, -2.5),
    (1, 2.5, 0.4),
    (1, -2.5, -0.4)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_one_float_and_int)
def test_divide_one_float_and_int(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_division_by_zero_float_and_int = [
    (0.0, 0, pytest.raises(ValueError)),
    (0, 0.0, pytest.raises(ValueError)),
    (-0.0, -0, pytest.raises(ValueError)),
    (-0, -0.0, pytest.raises(ValueError)),
    (0.0, -0, pytest.raises(ValueError)),
    (0, -0.0, pytest.raises(ValueError)),
    (-0.0, 0, pytest.raises(ValueError)),
    (-0, 0.0, pytest.raises(ValueError)),
    (6.0, 0, pytest.raises(ValueError)),
    (6, 0.0, pytest.raises(ValueError)),
    (-6.0, 0, pytest.raises(ValueError)),
    (-6, 0.0, pytest.raises(ValueError)),
    (6.0, -0, pytest.raises(ValueError)),
    (6, -0.0, pytest.raises(ValueError)),
    (-6.0, -0, pytest.raises(ValueError)),
    (-6, -0.0, pytest.raises(ValueError)),
    (2.5, 0, pytest.raises(ValueError)),
    (-2.5, 0, pytest.raises(ValueError)),
    (2.5, -0, pytest.raises(ValueError)),
    (-2.5, -0, pytest.raises(ValueError))
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_division_by_zero_float_and_int)
def test_divide_division_by_zero_float_and_int(num_f, divisor, expected):
        with expected:
            divide(num_f, divisor)

#-------------------------------------------------
test_cases_divide_zero_float_and_int = [
    (0.0, 2, 0.0),
    (0.0, -2, 0.0),
    (0, 2.0, 0.0),
    (0, -2.0, 0.0),
    (0, 2.5, 0.0),
    (0, -2.5, 0.0)
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_zero_float_and_int)
def test_divide_zero_float_and_int(num_f, divisor, expected):
        assert divide(num_f, divisor) == expected

#-------------------------------------------------
test_cases_divide_negativ = [
    ("1", "2", pytest.raises(TypeError)),
    ([1], [2], pytest.raises(TypeError)),
    (1, "2", pytest.raises(TypeError)),
    (1, [2], pytest.raises(TypeError)),
    ("1", 2, pytest.raises(TypeError)),
    ([1], 2, pytest.raises(TypeError)) 
]

@pytest.mark.parametrize("num_f, divisor, expected", test_cases_divide_negativ)
def test_divide_negativ(num_f, divisor, expected):
        with expected:
            divide(num_f, divisor)

#-------------------------------------------------
test_cases_divide_input_types = [
   (6, 9),
   (6.5, 2.5),
   (6.5, 9)  
]

@pytest.mark.parametrize("num_f, divisor", test_cases_divide_input_types)
def test_divide_input_types(num_f, divisor):
        assert isinstance(divide(num_f, divisor), (int, float))

#-------------------------------------------------