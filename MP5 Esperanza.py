# Python Programming Exercise: List and Tuples

# Number 1
# numbers = []
# print("Enter 5 numbers below:")
# for i in range(5):
#     userNumbers = int(input())
#     numbers.append(userNumbers)
#     numbers.sort()
# print("List of numbers:\n", numbers)
# totalNumbers = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# print("Total:", totalNumbers)

# Number 2
# colors = []
# print("Enter 5 colors:")
# for i in range(5):
#     userColors = input().lower()
#     colors.append(userColors)
# colors = tuple(colors)
# print("List of colors:\n", colors)
# print("First color:", colors[0])
# print("Last color:", colors[-1])
# print("Number of colors:", len(colors))

# # Number 3
# fruits = []
# print("Enter 3 fruits:")
# for i in range(3):
#     userFruits = input().lower()
#     fruits.append(userFruits)
# print("Initial list of fruits:", fruits)
# fruits.append("orange")
# fruits.remove("banana")
# print("Updated list of fruits:", fruits)

# # Numer 4
# animals = []
# print("Enter 3 animals:")
# for i in range(3):
#     userAnimals = input().lower()
#     animals.append(userAnimals)
# print("List of animals:", animals)
# animals = tuple(animals)
# print("Tuple of animals:", animals)
# animals = list(animals)
# print("Back to list:", animals)

# # Number 5
# students = []
# print("Enter student's name and score:")
# for i in range(3):
#     nameScore = input().upper()
#     students.append(nameScore)
# students = tuple(students)
# print("Students and Scores:\n", students)
# print("Highest score:", max(students))


mammals= {'Carnivora', 'Perissodactyla', 'monotremata', 'cetacea', 'rodentia'}
wiwi = input("Enter a mammal: ")
if wiwi in mammals:
      print(wiwi, 'is in the set.')
else:
      print(wiwi, 'is not in the set.')
print("\n")
print ('Mammals in the set: ')
print ('Carnivora')
print('Perissodactyla')
print ('monotremata')
print('cetacea')
print('rodentia')