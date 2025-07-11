

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor .")
elif age == 18:
    print("You are okay to have a license.")
elif age <= 30:
    print("Please use the driving safety guide.")
else:
    print("You are older than 30.")
