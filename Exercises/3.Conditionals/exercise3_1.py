hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
if float(hours) > 40:
    pay = pay + (float(hours) - 40) * float(rate) * 0.5
print("Pay: ", pay)