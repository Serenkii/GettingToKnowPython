# https://www.youtube.com/watch?v=HGOBQPFzWKo

def list_fun():
    # ordered, mutable, allows duplicate elements

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = my_list[1:5]
    print(a)

    b = [x * x for x in my_list]
    print(b)

    # lists are mutable!
    c = my_list
    print(my_list)
    c.append("I added this to c")
    print(my_list)


def tuple_fun():
    # ordered, immutable, allows duplicate elements

    my_tuple = "Max", 28, "Boston"
    print(my_tuple)

    a = ("Tim")
    print(type(a))
    b = ("Tim",)
    print(type(b))

    name, age, city = my_tuple
    print(city)

    c = (0, 1, 2, 3, 4, 5)
    i1, *i2, i3 = c
    print(i1)
    print(i2)
    print(i3)

    # tuples are more efficient!


def dictionary_fun():
    # Key-Value pairs, unordered, mutable

    mydict = {"name": "Max", "age": 28, "city": "New York"}
    print(mydict)
    mydict2 = dict(name="Mary", age=27, city="Boston")
    print(mydict2)

    print(mydict["name"])
    print(mydict.get("age"))

    print(mydict.values())
    print(mydict.keys())
    mydict["email"] = "max@xyz.com"
    print(mydict)
    mydict["email"] = "not_max@xyz.com"
    print(mydict)

    del mydict["name"]
    print(mydict)
    mydict.pop("age")
    print(mydict)

    if "city" in mydict:
        print(mydict["city"])

    for key in mydict:
        print(key)
    for value in mydict.values():
        print(value)
    for key, value in mydict.items():
        print(key, value)

    mydict.update(mydict2)
    print(mydict)

    mytuple = (10, 15)
    newdict = {mytuple: 25}
    print(newdict)

    # dictionaries are mutable, use copy()!


def set_fun():
    # unordered, mutable, no duplicates

    my_set = {1, 2, 3, 1, 2}
    print(my_set)
    my_set = set("Hello")
    print(my_set)
    my_set = set([1, 2, 3, 99, 99])
    print(my_set)
    my_set.discard(99)
    print(my_set)
    if 1 in my_set:
        print("yes, 1 in set")

    odds = {1, 3, 5, 7, 9, 11, 13}
    evens = {0, 2, 4, 6, 8, 10, 12}
    primes = {2, 3, 5, 7, 11, 13}
    u = odds.union(evens)
    print(u)
    i = evens.intersection(primes)
    print(i)

    a = {1, 2, 3, 4, 5}
    b = {1, 2, 3, 10, 11}
    print(a.difference(b))  # what elements from "a" are not in "b"
    print(b.difference(a))  # what elements from "b" are not in "a"
    print(a.symmetric_difference(b))  # what elements are not both in "a" and "b"

    a = {1, 2, 3}
    b = {1, 2, 3, 4, 5}
    print(a.issubset(b))
    print(b.issuperset(a))
    c = {10, 11, 12, 13}
    print(a.isdisjoint(b))
    print(a.isdisjoint(c))  # True if no common elements

    # careful with copying! They are mutable and we are working with reference


def string_fun():
    # ordered, immutable, text representation
    my_string = "Hello World"
    print(my_string)
    my_string = 'Hello Planet'
    print(my_string)

    test = "Testing\nstuff"
    print(test)

    # H-e-l-l-o- -P-l-a-n-e--t
    # 0-1-2-3-4-5-6-7-8-9-10-11

    print(my_string[1:5])  # ello
    print(my_string[:5])  # Hello
    print(my_string[-2])  # e
    print(my_string[:-3])  # Hello Pla
    print(my_string[6:])  # Planet
    print(my_string[-6:-2])  # Plan
    print(my_string[-6:10])  # Plan
    print(my_string[::1])  # every character .. % 1 = ..
    print(my_string[::2])  # every second    .. % 2 = ..
    print(my_string[::3])  # every third       index starts with 0, so maybe it works with modulo internally
    print(my_string[::-1])  # reverse
    print(my_string[::-2])  # reversed, then from the new beginning every second (first (0)) included

    # ...other java similar methods...

    print(my_string.startswith("Hell"))  # True
    print(my_string.find("ll"))  # index
    print(my_string.count("e"))  # count

    my_string = "Why is this suddenly a list???"
    my_list = my_string.split()
    print(my_list)

    my_string = my_string.replace(" ", ",")
    print(my_string)

    my_list = my_string.split(" ")
    print(my_list)

    my_list = my_string.split(",")
    print(my_list)

    new_string = "".join(my_list)  # much faster than for loop
    print(new_string)

    new_string = " ".join(my_list)
    print(new_string)

    var = 3.12345678
    my_string = "the variable is {:.2f} and the other one is {}".format(var, 2)
    print(my_string)

    my_string = f"the variable is {var} and the other one is {2 * 3000}"
    print(my_string)


def collections_fun():
    # I think I should code some kind of mini project to practice a bit before going on from here   - 20220119
    # https://youtu.be/HGOBQPFzWKo
    pass

# Basics with Pycharm: https://youtu.be/56bPIGf4us0
