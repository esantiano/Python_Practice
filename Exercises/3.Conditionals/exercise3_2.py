hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    hours_float = float(hours)
    rate_float = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
pay = float(hours) * float(rate)
print("Pay: ", pay)