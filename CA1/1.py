def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):
            print(num)

print_narcis_numbers(1000, 5000)

#  error is in line 1 there is no colon.
#  error is in line 3 used '==' instead of '='
#  error is in line 4 used '==' instead of '='
#  error is in line 6 used '***' instead of '**'
# error in line 13 used is_narcissistic(num) instead of is_narc(num)
# error in line 14 used narc_numbers instead of narcis_numbers.
