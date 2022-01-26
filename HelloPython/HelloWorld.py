import datetime
import string
import sys

print("Hello World!")


# https://www.youtube.com/watch?v=rfscVS0vtbw
# https://openbook.rheinwerk-verlag.de/python/


def variables():
    this_is_a_variable = "It just inferred it's a String, that's crazy."
    print("You know what? " + this_is_a_variable)

    # Other variables
    number = 4
    test = True
    other_number = 8246234.122352
    a_string = "kakfkaksdk\n\\"
    print(a_string)


# Strings
def strings():
    phrase = "This is a String, Python is weird."
    print(phrase.capitalize())
    print(phrase.upper())
    print(phrase.lower())
    print(len(phrase))


# input
def user_input():
    user_input = input("Give input: ")
    print("Your input: " + user_input)


def return_function():
    return "That's really weird tbh"


def working_with_lists():
    a_list = [False, "One", 2, "Three", 4.0, ["list", "in", "a", "list"]]
    print(a_list);
    print(a_list[0])
    print(a_list[5])
    print(a_list[5][2])
    print(a_list[-2])
    print(a_list[:3])  # x:y --> x inclusive, y exclusive
    print(a_list[1:4])
    a_list[0] = True
    print(a_list[0])
    a_list[0] = "not a boolean anymore"
    print(a_list[0])


def list_functions():
    another_list = [1, 2, 4, 8, 16, 32, 666]
    print(another_list)
    another_list.extend(another_list)
    print(another_list)
    another_list.append("another element")
    print(another_list)
    another_list.insert(2, "3")
    print(another_list)
    succesful = another_list.remove(666)
    print(another_list)
    print(succesful)
    another_list.pop()
    print(another_list)
    print(another_list.index("3"))
    print(another_list.count(32))
    another_list.reverse()
    print(another_list)
    another_list.clear()
    another_list.extend([3, 4, 535132, 6, 7, 83521, 9])
    another_list.sort()
    print(another_list)


def working_with_tuples():
    coordinates = (4, 5)
    print(coordinates[0])
    coordinates = (12, 454)
    print(coordinates)
    # coordinates[0] = 10   tuple is immutable
    a_tuple = ("different type", 5, '!')
    print(a_tuple)
    coordinates = [("a list", "of"), ("tuples"), ["and", "lists", ([3], 4)], '!']
    print(coordinates)


def a_function(number1: float, number2: float) -> float:  # that is just fucking retarded:
    # https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you
    # -pass-in
    """ if (not isinstance(number1, float) or not isinstance(number2, float)) and (not isinstance(number1, int) or not isinstance(number2, int)):
         raise TypeError    """
    # apparently you shouldn't do this?
    # https://stackoverflow.com/questions/4205130/what-is-duck-typing
    number = number1 + number2
    print(number)
    return number


def try_a_function():
    a_function(3, 5)
    a_function(4.0, 3.0)
    a_function("just try", " , we do not care about the type at all!")


def if_statements():
    x = 0
    if x < 2:
        print("jo")
    if x == 1:
        print("will not be printed")
    if x == -1:
        print(-1)
    elif x == 0:
        print(0)
    elif x == 0:
        print("will never be printed")
    if (x == "a string"):
        print("I don't think so")
    else:
        print("ur right")

    var = (20 if x == 0 else 30)
    print(var)
    print("x hat den Wert 1" if x == 1 else "x ist ungleich 1")


def loops():
    x = sys.maxsize * sys.maxsize  # cool that python can handle gigantic numbers with no care by me
    while (x > 0):
        print(x)
        x -= sys.maxsize * (sys.maxsize / 9999)

    secret = 1337
    guess = 0
    while guess != secret:
        guess = int(input("Guess: "))
        if guess == -1:
            print("game over")
            break
    else:
        print("You won. (Btw, really interesting that there is while - else")
    print("the else part will only be executed if the loop is executed \"naturally\" apparently, which is really "
          "interesting -- break will result in skipping the else part")


def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(num1 + num2)
        return num1 + num2
    if operator == "-":
        print(num1 - num2)
        return num1 - num2
    if operator == "/":
        print(num1 / num2)
        return num1 / num2
    if operator == "*":
        print(num1 * num2)
        return num1 * num2


def dictionaries():
    month_conversion = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        # etc
    }
    print(month_conversion["Jan"])
    print(month_conversion.get(""))
    print(month_conversion.get(None))
    print(month_conversion.get("Jul"))
    print(month_conversion.get("AMK", "Not a valid keyyyy"))


def for_loop():
    for letter in "Serenki":
        print(letter, end=" ")  # https://stackoverflow.com/questions/493386/how-to-print-without-a-newline-or-space

    print()
    numbers = []
    for n in range(5, 20):
        numbers.append(n)
    print(numbers)

    for number in numbers:
        print(number, end=" ")


def exponent(base, pow):
    solution = 1
    for i in range(pow):
        solution *= base
    return solution


def list_2d():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]
    for row in grid:
        for x in row:
            print(x, end=" ")
        print()


def if_in(phrase: string):
    for letter in phrase:
        if letter.upper() in "AOEUI":
            print("vocal")
        else:
            print("not vocal")


def try_and_except():
    try:
        number = int(input("Enter a whole number: "))
    except TypeError:
        print("Do you not know what a number is?")
        return
    print(number)


def reading_from_files():
    our_file = open("file.txt", "r")  # modes: "r" (read); "w" (write); "a" (append); "r+" (read and write)

    print(our_file.readable())
    print(our_file.readline(), end="")
    print(our_file.readline())  # first three lines have already been "read"
    # print(our_file.readlines())
    print(our_file.readlines()[10])  # that's why this will start from line 3, aka the 4th line
    # print(our_file.read())

    our_file.close()


def writing_to_files():
    our_file = open("file.txt", "a")
    our_file.write("\nI added this line on the " + str(datetime.date.today()))
    our_file.close()

    write_file = open("write_file.txt", "w")
    write_file.write("I added this to the file and deleted everything else")
    write_file.close()

    new_file = open(input("What file do you want to create? \n"), "w")
    new_file.write(input("What line do you want to write in it? \n"))
    print("Done :)")
    new_file.close()


def modules():
    print("https://docs.python.org/3/py-modindex.html")
    print("https://youtu.be/rfscVS0vtbw?t=12493")
    print(datetime.datetime.now())
    print("Install third party programs with pip: https://youtu.be/rfscVS0vtbw?t=13252")
    print("The file it is installed in "
          "C:\\Users\\Marian\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages")
    # C:\Users\Marian\AppData\Local\Programs\Python\Python310\Lib\site-packages


class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


def experimenting_with_classes():
    student1 = Student("Jim", "Business", 3.1, False)
    print(student1.name)
    student1.__init__("Not Jim anymore", "None", 0, True)
    print(student1.name)
    student1 = Student("Not even not Jim anymore", "Identity Studies", 10, False)
    print(student1.name)
    print(student1.major)
    print(student1.gpa)

    print(student1.on_honor_roll())


print("Done for now.")