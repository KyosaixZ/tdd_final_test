from function import calculate_egg_cost


def get_num_eggs():
    while True:
        try:
            num_eggs = int(input("How many eggs would you like to buy? "))
            if num_eggs < 0:
                print("Invalid input: Number of eggs must be a positive integer.")
            else:
                return num_eggs
        except ValueError:
            print("Invalid input: Number of eggs must be a positive integer.")


num_eggs = get_num_eggs()
egg_cost = calculate_egg_cost(num_eggs)
print(egg_cost)