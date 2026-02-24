print ()
print ("2. Basic Calculator")

print()
print ("  1. Addition (+)")
print ("  2. Subtraction (-)")
print ("  3. Multiplication (*)")
print ("  4. Division (/)")
print ("  5. Modulus (%)")
print ("  6. Exponents (**)")
print ("  7. Reciprocal (1/)")
print ("  8. Root (√)")
print ()

firstNumber = int(input("Enter First Number: "))
operation = input("Enter Operation Symbol: ")

if operation == "+":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber + secondNumber
elif operation == "-":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber - secondNumber
elif operation == "*":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber * secondNumber
elif operation == "/":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber / secondNumber
elif operation == "%":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber % secondNumber
elif operation == "**":
    secondNumber = int(input("Enter second number: "))
    result = firstNumber ** secondNumber
elif operation == "1/":
    result = 1 / firstNumber
elif operation == "√":
    result = firstNumber **0.5
else:
    result = "Invalid operation"

print("=", result)