print ("2. Basic Calculator")

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

print ("Choose an operation")
print ("  1. Addition (+)")
print ("  2. Subtraction (-)")
print ("  3. Multiplication (*)")
print ("  4. Division (/)")
print ("  5. Modulus (%)")
print ("  6. Power (**)")
print ("  7. Reciprocal ()")
print ("  8. Root (√)")
operation = input("Enter operation: ")

if operation == "+" or "Addition":
    result = firstNumber + secondNumber
if operation == "-" or "Subtraction":
    result = firstNumber - secondNumber
if operation == "*" or "Multiplication":
    result = firstNumber * secondNumber
if operation == "/" or "Division":
    result = firstNumber / secondNumber
if operation == "%" or "Modulus":
    result = firstNumber % secondNumber
if operation == "**" or "Power ":
    result = firstNumber ** secondNumber
if operation == "√" or "Root":

print("=", result)