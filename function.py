def process_egg_cost(num_eggs):
    # Processing
    dozen = num_eggs // 12
    cost = 0

    if dozen >= 5:
        cost = num_eggs * (35/12)
    elif dozen >= 1:
        cost = num_eggs * 3
    else:
        cost = num_eggs * 4

    return cost



def validate_input(num_eggs):
    # Input validation
    if not isinstance(num_eggs, int) or num_eggs < 0:
        return "Invalid input: Number of eggs must be a positive integer."
    return None

def calculate_egg_cost(num_eggs):
    error = validate_input(num_eggs)
    if error:
        return error

    cost = process_egg_cost(num_eggs)
    output = format_output(num_eggs, cost)
    return output

def format_output(num_eggs, cost):
    return f"The cost of {num_eggs} eggs is {cost:.2f} baht"