try:
    value
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError:
    print("divivded by zero")
except ValueError:
    print("Invlid value")