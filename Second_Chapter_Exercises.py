#Exercise 1: List Comprehension Mastery (for loop, you can write it in a single line)
#Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
#Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]
#Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
input = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [word.upper() for word in input if len(word) >= 4]
#print(result)
#=====================================================================================
#Dictionary Merging with Logic
#Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
#Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}
#Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}
dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
#dict_c = dict_a | dict_b
#print(dict_c)
dict_c = dict_a.copy()
for keys, values in dict_b.items():
    if keys in dict_c:
        dict_c[keys] += values
    else:
        dict_c[keys] = values
#print(dict_c)
#========================================================================
#Exercise 3: Frequency Map with Counter
#Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.
#Given Input: text = "Python Programming"
text = "Python Programming"
def character_count(charStr):
    return_count = {}
    for char in charStr:
        if char == " ":
            continue
#Get the current count of char from the dictionary. If it doesn't exist, use 0. Then add 1 and store it back.
        return_count[char] = return_count.get(char, 0) +1
    print(return_count) #{'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

character_count(text)
#==============================================================================
#Exercise 4: Anagram Checker
#Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
#Given Input: word1 = "listen", word2 = "silent"
#Expected Output: Is "listen" an anagram of "silent"? True
import sys
word1 = "listen"
word2 = "silent"
if len(word1) != len(word2):
    print("Not an anagram")
    sys.exit()
#Sorting arranges the characters in alphabetical order. listen ↓ Sort eilnst (both word will be eilnst, compare)
if sorted(word1) == sorted(word2):
        print("This an anagram")
else:
        print("Not an anagram")
#=====================================================================================
#Exercise 5: Flatten a Nested List
#Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.
#Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]
#Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]
def recursive_count(nested_list):
    nested_listArr = []
    for item in nested_list:
        if isinstance(item, list):
            nested_listArr.extend(recursive_count(item)) #add/merge link, tuple, dictionary
        else:
            nested_listArr.append(item) #add one number or char
    return nested_listArr

nested = [1, [2, 3], [4, [5, 6]], 7]
print(recursive_count(nested))
#flatlist = [x for subtile1 in matrix for x in subtile1]
#print(flatten)
#==================================================================================
#Exercise 6: Reverse Each Word of a String
#Given a sentence, reverse each individual word within the string while maintaining the original word order.
#Given Input: "Python is awesome"
#Expected Output: "nohtyP si emosewa"
text = "Python is awesome"
#result = []
result = text.split()  # string to list conversation
print(result) #['Python', 'is', 'awesome']
#result = " ".join(result) #convert list to string
result = " ".join(x[::-1] for x in result)
print(result)
#=============================================================================
#interview question
x = 10
def func():
    x = 5
    return [x * i for i in range(3)]

result = func()
#print(result) #[0,5,10]
#print(x)  #10
#================================================================================
#strig to list
text = "Python is awesome"
result = text.split()  # string to list conversation
#print(result) #['Python', 'is', 'awesome']
result = " ".join(result) #convert list to string
#print(result)
#=======================================================================================
#Exercise 7: Palindrome Sentence
#Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.
#Given Input: "A man, a plan, a canal: Panama"
#Expected Output: True
data = "A man, a plan, a canal: Panama"
