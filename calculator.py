# Get input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose your operation (+, -, /, x): ")

# Perform calculation
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "/":
    # Optional: prevent division by zero
    if b == 0:
        result = "Cannot divide by zero!"
    else:
        result = a / b
elif op == "x":
    result = a * b
else:
    result = "Invalid operation."

# Show result
print(f"Result: {result}")
