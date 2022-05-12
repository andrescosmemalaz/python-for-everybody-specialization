# Problem 1
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

count = 0
for vowels in s:
    if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
        count = count + 1
print("Number of vowels: " + str(count))


