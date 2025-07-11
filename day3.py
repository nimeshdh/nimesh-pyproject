#  Takes a secret word as input(without spaces)
# then encodes the word using a custom cipher
# replace all vowls with *
# reverse the string 
# then shift each letter 2 places ahead in the alphabet(wrap around if needed,e.g,y>a , z >b)
# finally print the resulting encoded word

def encode_secret_word(word):
    vowels = "aeiouAEIOU"
    replaced = ''.join(['*' if char in vowels else char for char in word])
    
    reversed_word = replaced[::-1]
    
    encoded = ''
    for char in reversed_word:
        if char.isalpha():
            shifted = chr((ord(char.lower()) - ord('a') + 2) % 26 + ord('a'))
            encoded += shifted
        else:
            encoded += char  
    
    return encoded


secret = input("Enter the word: ")
encoded_word = encode_secret_word(secret)
print("Encoded word:", encoded_word)
