# Problem 1
userNum = int(input("Enter a number: "))
if userNum == 0:
    print("The number you entered is zero")
elif userNum < 0:
    print("The number you entered is negative")
else:
    print("The number you entered is positive")

# Problem 2
number = int(input("Enter a number: "))
if number  % 2 == 0:
    print("The number you entered is even")
else:
    print("The number you entered is odd")

# Problem 3
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not yet eligible to vote")

# Problem 4
grades = float(input("Enter your grade here:\n"))
if 90 <= grades <= 100:
      print("Equivalent grade: Excellent! (90-100)")
elif 80 <= grades <= 89:
    print("Equivalent grade: Very Good! (80-89)")
elif 70 <= grades <= 79:
    print("Equivalent grade: Good! (70-79)")
elif 60 <= grades <= 69:
    print("Equivalent grade: Needs improvement (60-69)")
elif grades <=60:
    print("Equivalent grade: Failed! (Below 60)")
else:
    print("Invalid grade entered.")

# Problem 5
print("Welcome to McDonut's!\nAvail our promo of 10% discount for any $1000+ worth of purchase!")
amount = float(input("Please enter amount purchased:\n"))
if amount >= 1000:
    discount = amount * .10
    price = amount - discount
    print("Discounted amount:", price)
else:
    print("No discount applicable.")

# Problem 6
numbers = []
for i in range(3):
    user_Numbers = int(input("Enter a number: "))
    numbers.append(user_Numbers)
print(numbers)
largest = max(numbers)
print("The largest number is:\n", largest)

# Problem 7
print("Welcome to McDonut's Corporation!\nEnter the year you entered the company to see applicable bonuses")
service = int(input("Year: "))
year = 2025 - service
salary = float(input("Enter your salary: "))
if year >= 10:
    bonus = salary * 0.10
    final = salary + bonus
    print("Final Salary: ", final)
elif year >= 5:
    bonus = salary * 0.05
    final = salary + bonus
    print("Final Salary: ", final)
else:
    print("No applicable bonus.")

# Problem 8
print("Welcome to BDO!")
user = int(input("1. Balance Inquiry\n2. Deposit\n3. Withdraw\n4. Exit\n"))
if user == 1:
    print("You chose Balance Inquiry.")
elif user == 2:
    print("You chose Deposit.")
elif user == 3:
    print("You chose Withdraw.")
elif user == 4:
    print("You chose Exit")
else:
    print("Invalid Input.")

# Problem 9
while True:
    print("Enter the number of the beverage you want")
    beverage = int(input("1. Coke\n2. Sprite\n3. Royal\n4. Mountain Dew\n5. Water\n"))
    if beverage == 1:
        print("You chose Coke")
    elif beverage == 2:
        print("You chose Sprite")
    elif beverage == 3:
        print("You chose Royal")
    elif beverage == 4:
        print("You chose Mountain Dew")
    elif beverage == 5:
        print("You chose Water")
    else:
        print("Invalid input")
    again = str(input("\nDo you want to choose another beverage? Y/N: ")).lower()
    if again == "y":
        continue
    elif again == "n":
        break

#  Problem 10
horoscope = {
    "Aries": "Your energy is high today take initiative, but don't rush decisions. A small risk could bring a big reward.",
    "Pisces": "Your imagination runs wild let creativity guide you, but don't lose touch with reality. Balance both worlds.",
    "Libra": "Harmony and balance guide you. Seek compromise and beauty in your surroundings peace follows effort.",
    "Leo": "Your confidence shines bright use it to inspire others. Just don't let pride block genuine connection.",
    "Virgo": "Details matter now. Organize, plan, and fine-tune your goals. Your hard work is about to pay off.",
    "Taurus": "Stability is your friend today. Focus on routines and long-term goals, and avoid unnecessary drama.",
    "Gemini": "Your curiosity will open doors. Communicate clearly and keep your mind flexible new ideas are coming.",
    "Scorpio": "Your intuition is strong today. Trust your instincts, but keep emotions in check when making choices",
    "Cancer": "Emotions might run deep today. Spend time with people who make you feel safe and understood.",
    "Aquarius": "Original ideas flow easily today. Collaborate with others who share your vision and make something fresh.",
    "Capricorn": "Discipline leads you forward. Stick to your goals and avoid distractions progress is closer than it seems."
}
user = input("\nEnter your zodiac sign: ").title()
if user in horoscope:
    print("Your horoscope is:", horoscope[user])
else:
    print("Invalid input. Please try again.")