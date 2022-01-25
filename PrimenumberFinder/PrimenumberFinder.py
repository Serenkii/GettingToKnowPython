import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divider in range(3, int(math.sqrt(number)) + 1, 2):
        if number % divider == 0:
            return False
    return True


def take_input():
    user_input = input()
    user_input.strip().lower()
    input_list = user_input.split(" ", 2)

    if len(input_list) == 1 and (input_list[0] == "exit" or input_list[0] == "stop" or input_list[0] == "0"):
        return False

    elif input_list[0] == "help" and len(input_list) == 1:
        print("Not implemented yet.")
        return True

    elif input_list[0] == "is_prime" or input_list[0] == "isPrime":
        if not len(input_list) == 2:
            print("Your input needs a number as an argument.")
            return True
        if not input_list[1].isdecimal():
            print("Your argument was not a number.")
            return True
        number = int(input_list[1])
        if is_prime(number):
            print(f"The number {number} is a prime number!")
        else:
            print(f"The number {number} is NOT a prime number!")
        return True

    else:
        print("Your input was not valid. Type 'help' for help.")
        return True


while take_input():
    pass
