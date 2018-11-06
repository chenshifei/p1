def describe_number(number):
    print("The number", number, "is a very interesting number.")
    print("The square of", number, "is", number**2,
          "and the cube of", number, "is", number**3)
    print("This line shows how big", number, "is:,", number * "-")
    print()

def do_numbers():
    for n in range(5, 11):
        describe_number(n)

do_numbers()
