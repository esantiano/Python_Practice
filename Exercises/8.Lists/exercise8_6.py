nums = list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        print("Maximum:", float(max(nums)))
        print("Minimum:", float(min(nums)))
        exit()
    else:
        nums.append(num)
