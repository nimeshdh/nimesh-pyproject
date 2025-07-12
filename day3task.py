# 1. Take a number from the user and print whether it's even or odd.

# num = int(input("Enter any number "))
# if num % 2 == 0:
#     print (f"{num} is even number")
# else:
#     print(f"{num} is odd number")


# 2. Write a program to count the number of vowels in a given string.

def count_vowels(text):
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print("Number of vowels:", count_vowels("iiiii"))
