def is_armstrong(number):
    # Convert the number to string to easily iterate through digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == number

# Input number from the user
number = int(input("Enter a number: "))

# Check if the number is Armstrong
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
