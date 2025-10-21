def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\n1. Add\n2. Sub\n3. Mul\n4. Div\n5. Exit")
    c = int(input("Enter your choice (1-5): "))

    if c == 5:
        print("Quit")
        break

    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))

    if c == 1:
        print("Result:", add(a, b))
    elif c == 2:
        print("Result:", sub(a, b))
    elif c == 3:
        print("Result:", mul(a, b))
    elif c == 4:
        if b != 0:
            print("Result:", div(a, b))
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please enter between 1 and 5.")
