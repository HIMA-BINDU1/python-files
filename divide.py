def divide(num1, num2):
    try:
        return num1//num2
    except ZeroDivisionError:
        return "Zero division error"

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(divide(num1, num2))