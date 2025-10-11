number = input("Enter a number: ")
count = 0
total = 0
while number != "done":
    try:
        total += int(number)
        count += 1
    except: 
        print("Invalid input")
    number = input("Enter a number: ")
print(total, count, float(total)/count)