number = input("Enter a number: ")
max = None
min = None
while number != "done":
    try:
        num = float(number)
        if max is None or num > max:
            max = num
        if min is None or num < min:
            min = num
    except:
        print("Invalid input")
    number = input("Enter a number: ")
print(max, min)