# Program which will keep adding stream of number inputted by the user. The adding stops as soon as user
# user pressed or q key on keyboard.

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
