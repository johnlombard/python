def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b


print("let's do some math with just functions!")

age = add(20, 2)
height = subtract(78, 12)
weight = multiply(75, 2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

print(float(input()))