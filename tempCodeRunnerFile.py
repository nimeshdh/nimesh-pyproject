age = int(input("enter your age"))

if age == 18:
    print("You are okay to have a license")
elif age < 30:
    print("please use the driving safety guide")
elif age > 30:
    print("you are greater than 30")
else:
    print("you are minor")
