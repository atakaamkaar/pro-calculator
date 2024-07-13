import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def square(a):
    return a * a

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Negative number"

def sin_value(a):
    return math.sin(math.radians(a))

def cos_value(a):
    return math.cos(math.radians(a))

def log_value(a):
    if a > 0:
        return math.log(a)
    else:
        return "Error: Non-positive number"

def display_menu():
    print("Pro Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Log")
    print("10. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-10): ")
        
        if choice == '10':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        
        elif choice in ['5', '6', '7', '8', '9']:
            a = float(input("Enter the number: "))
        
        if choice == '1':
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            print(f"Result: {square(a)}")
        elif choice == '6':
            print(f"Result: {square_root(a)}")
        elif choice == '7':
            print(f"Result: {sin_value(a)}")
        elif choice == '8':
            print(f"Result: {cos_value(a)}")
        elif choice == '9':
            print(f"Result: {log_value(a)}")
        else:
            print("Invalid choice, please select a number between 1 and 10.")
        
        # Ask if the user wants to perform another calculation
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
