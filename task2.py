# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]
s="PythonPractice"
print(s[1])
print(s[-3:])
print(s[2:7])




# 2.  Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.
text="developer"
print(text[::-1])



# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("Number of vowels:", count_vowels("iiiii"))







# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

def is_palindrome(text):
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

print(is_palindrome("pubg mobile")) 





# 5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"
text = "   hello world! welcome to Python.   "
replace = text.strip().title().replace("Python", "Programming")
print(replace)







# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("I love  her"))




# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1
s1 = "Py"
s2 = "thon"

print(s1 + s2)     
print(s1 * 3)      
print("y" in s1)




# 8. Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("arsenal"))




# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.
def is_anagram(s, ss):
    return sorted(s.lower()) == sorted(ss.lower())

print(is_anagram("listen", "silent"))






# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.


def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("my name is nimesh.my name isnot nimesh"))  
