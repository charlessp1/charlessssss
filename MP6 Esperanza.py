# Python Programming Exercises: Python Sets

## Number 1:
# numbers = set()
# for i in range(5):
#     addNumbers = int(input("Enter a number: "))
#     numbers.add(addNumbers)
# print("Initial set:", numbers)
# numbers.add(6)
# print("Updated set:", numbers)

## Number 2:
# fruits = set()
# for i in range(4):
#     addFruits = input("Enter a fruit name: ")
#     fruits.add(addFruits)
# print("Initial set:", fruits)
# fruits.remove("banana")
# fruits.add("grapes")
# print("Final set:", fruits)

## Number 3:
# set1 = set()
# set2 = set()
# print("Input numbers for first set: ")
# for i in range(4):
#     numbers1 = int(input())
#     set1.add(numbers1)
# print("Input numbers for second set: ")
# for i in range(4):
#     numbers2 = int(input())
#     set2.add(numbers2)
# print("First set:", set1)
# print("Second set:", set2)
# print("Union of two sets:", set1.union(set2))
# print("Intersection of two sets:", set1.intersection(set2))

# # Number 4:
# A = set()
# B = set()
# print("Input colors for set A: ")
# for i in range(3):
#     colorsA = (input())
#     A.add(colorsA)
# print("Input colors for set B: ")
# for i in range(3):
#     colorsB = (input())
#     B.add(colorsB)
# print("Set A:", A)
# print("Set B:", B)
# print("Difference:", A.difference(B))
# print("Symmetric Difference:", A.symmetric_difference(B))

# # Number 5:
animalNames = ["dog", "cat", "bird", "fish"]
animals = set(animalNames)
while True:
    print("Generated set: ", animals)
    animal2 = input("Enter an animal name: ").lower()
    if animal2 in animals:
        print("The animal", animal2, "is in the set: ", animals)
    else:
        print("The animal", animal2, "is not in the set.")
        animals.add(animal2)
        print("Updated set: ", animals)
    userinput = input("Do you want to continue? Yes/No: ")
    if userinput.lower() == "yes":
        continue
    elif userinput.lower() == "no":
        break