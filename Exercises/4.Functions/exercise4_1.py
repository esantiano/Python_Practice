hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
def computepay(hours, rate):
    pay = float(hours) * float(rate)
    if float(hours) > 40:
        pay = pay + (float(hours) - 40) * float(rate) * 0.5
    return pay
print("Pay: ", computepay(hours, rate))