
#  Taking  input from user
message = input("Enter your message: ")
shift = 3  # fixing the  shift

# output ko lagi chuttako
secret_code = ""

#  loop using for each character
for char in message:
    if char.isalpha():  # Check if character is a letter
        # Convert to lowercase
        lower_char = char.lower()
        # Shift and wrap using ASCII(americal standard infromation interchange a-97 to z-122) print(ord('a'))
        shifted = chr((ord(lower_char) - ord('a') + shift) % 26 + ord('a'))
        '''ascii_code = ord(lower_char)
shifted_code = ascii_code + 3
if shifted_code > ord('z'):
    shifted_code = shifted_code - 26 
shifted = chr(shifted_code)
secret_code += shifted'''
        secret_code += shifted
    else:
        # Keep non-alphabet characters as they are
        secret_code += char

# Step 4: Print the result
print("Secret Code:", secret_code)
