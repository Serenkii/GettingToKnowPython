import random

def ask_for_length(enforce_length_requirements: bool):
    while True:
        user_input = input("What length should you password have? (8 - 32)\n")
        user_input = user_input.strip()
        if not user_input.isdecimal():
            print("Your input is not a number.")
            continue
        length = int(user_input)
        if length < 8 and enforce_length_requirements:
            print("A password with less than 8 characters is nowhere near save...")
            continue
        elif length > 32 and enforce_length_requirements:
            print("A password with more than 32 characters is a bit long. We aren't securing a nuclear vault, are we?")
            continue
        else:
            return length


def generate_password(characters: str, length: int):
    password = ""
    for i in range(length):
        password += characters[random.randrange(0, len(characters))]
    return password


def ask_yes_or_no_question(prompt: str):
    prompt = prompt.strip()
    if not prompt.endswith("(y/n)"):
        prompt += " (y/n)"

    user_input = input(prompt + "\n")
    user_input = user_input.strip().lower()
    if user_input == "y" or user_input == "yes":
        return True
    elif user_input == "n" or user_input == "no":
        return False
    print(f"\"{user_input}\" is no valid answer.")


while True:
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += characters.upper()
    characters += "0123456789"

    if ask_yes_or_no_question("Should the password contain special characters? (y/n)"):
        characters += "*.! @#$%^&(){}[]:;<>,.?/~_+-=|\\"

    length = ask_for_length(enforce_length_requirements=True)

    password = generate_password(characters, length)
    print("The generated password is:\n\n" + password + "\n\n")

    if not ask_yes_or_no_question("Do you want to generate another password?"):
        break

print("Okay, bye. Thanks for using this PasswordGenerator!")
