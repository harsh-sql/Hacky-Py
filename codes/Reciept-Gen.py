i = 0
while True:
    user = int(input("Enter the price:\n"))
    out = input("If you are done press 'q' otherwise enter key\n")
    i = i + user
    print(f"Order total so far {i}")
    if out == "q":
        print(f"Your total bill is {i}")
        print("Thankyou for using our calculator.")
        break
    else:
        continue
