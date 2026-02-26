first_integer = int(input("Enter an integer: "))
second_integer = int(input("Enter another integer: "))
first_integer = first_integer % second_integer
first_integer = first_integer % second_integer
second_integer = second_integer % first_integer
print(second_integer)

