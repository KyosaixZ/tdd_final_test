from function import calculate_egg_cost
import pytest

# test for input validation
@pytest.mark.parametrize("input_number, expected_result", 
[('string', 'Invalid input: Number of eggs must be a positive integer.'),
 (-1, 'Invalid input: Number of eggs must be a positive integer.'), 
 (0, 'Invalid input: Number of eggs must be a positive integer.')])
def test_input_validation(input_number, expected_result):
    actual_result = calculate_egg_cost(input_number)
    assert expected_result == actual_result

# test for 1-11 eggs pricing tier
@pytest.mark.parametrize("input_number, expected_result", 
[(1,'The cost of 1 eggs is 4.00 baht'), 
 (5,'The cost of 5 eggs is 20.00 baht'), 
 (11,'The cost of 11 eggs is 44.00 baht')])
def test_pricing_tier1(input_number, expected_result):
    actual_result = calculate_egg_cost(input_number)
    assert expected_result == actual_result

# test for 12-59 eggs pricing tier
@pytest.mark.parametrize("input_number, expected_result", 
[(12,'The cost of 12 eggs is 36.00 baht'), 
 (25,'The cost of 25 eggs is 75.00 baht'), 
 (59,'The cost of 59 eggs is 177.00 baht')])
def test_pricing_tier2(input_number, expected_result):
    actual_result = calculate_egg_cost(input_number)
    assert expected_result == actual_result

# test for 60 or more eggs pricing tier
@pytest.mark.parametrize("input_number, expected_result", 
[(60,'The cost of 60 eggs is 175.00 baht'), 
 (100,'The cost of 100 eggs is 291.67 baht'), 
 (200,'The cost of 200 eggs is 583.33 baht')])
def test_pricing_tier3(input_number, expected_result):
    actual_result = calculate_egg_cost(input_number)
    assert expected_result == actual_result
