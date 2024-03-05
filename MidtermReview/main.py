class Pizza:

    def __init__(self, diameter_in_centimeters: int, base_cost: float,
                 cost_in_cents_per_centimeter: int, base_diameter_in_centimeters: int):
        self.set_diameter_in_centimeters(diameter_in_centimeters)
        self._base_cost = base_cost
        self._cost_in_cents_per_centimeter = cost_in_cents_per_centimeter
        self._base_diameter_in_centimeters = base_diameter_in_centimeters
        self._toppings = []

    def add_toppings(self, topping):
        self._toppings.append(topping)

    def get_total_cost(self):
        total_cost = self._base_cost
        if self._diameter_in_centimeters > self._base_diameter_in_centimeters:
            total_cost += ( self._diameter_in_centimeters - self._base_diameter_in_centimeters ) \
                * self._cost_in_cents_per_centimeter
        return total_cost

    def set_diameter_in_centimeters(self, diameter_in_centimeters):
        if diameter_in_centimeters <= 0:
            raise ValueError
        self._diameter_in_centimeters = diameter_in_centimeters

# umgpt prompt: write a function that determines if a value is value is prime or not
def is_prime(number):
    if number <= 1:
        return False  # numbers less than or equal to 1 are not prime
    if number <= 3:
        return True   # 2 and 3 are prime numbers
    if number % 2 == 0 or number % 3 == 0:
        return False  # multiples of 2 and 3 are not prime

    # Check for divisors from 5 to the square root of the number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True  # if no divisors are found, the number is prime


def sum_of_white_primes_minus_black_primes(some_2d_list):
    total = 0
    # is_white_square = False
    # for row in some_2d_list:
    #     is_white_square = not is_white_square
    #     for value in row:
    #         if is_prime(value):
    #             if is_white_square:
    #                 total += value
    #             else:
    #                 total -= value
    #         is_white_square = not is_white_square

    for row_index, row in enumerate(some_2d_list):
        is_white_square = row_index % 2 == 0
        for value in row:
            if is_prime(value):
                if is_white_square:
                    total += value
                else:
                    total -= value
            is_white_square = not is_white_square

    return total

some_2d_list = [
    [3, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

print(sum_of_white_primes_minus_black_primes(some_2d_list))



def standard_deviation(some_numbers):
    average = sum(some_numbers) / len(some_numbers)
    variance = 0
    for value in some_numbers:
        variance += (value - average)**2
    variance /= len(some_numbers)
    return variance**.5

def _standard_deviation_recursive(some_numbers, average, current_value_index, total_variance):
    if current_value_index >= len(some_numbers):
        return total_variance
    total_variance += (some_numbers[current_value_index]-average)**2
    return _standard_deviation_recursive(some_numbers, average, current_value_index+1, total_variance)

def standard_deviation_recursive(some_numbers):
    average = sum(some_numbers) / len(some_numbers)
    return (_standard_deviation_recursive(some_numbers, average, 0, 0)/len(some_numbers))**.5


def _reverse_list(some_list, start_index, end_index):
    if start_index < end_index:
        temp = some_list[start_index]
        some_list[start_index] = some_list[end_index]
        some_list[end_index] = temp
        _reverse_list(some_list, start_index+1, end_index-1)

def reverse_list(some_list):
    _reverse_list(some_list, 0, len(some_list) - 1)