# 1) Create a string "hello" and convert it to uppercase using a string method.
s="hello"
print(s.upper())
# 2)Given "PYTHON" , convert it to lowercase using a string method.
s="PYTHON"
print(s.lower())
# 3)From "hello world" , replace "world" with "python" using a string method.
s="hello world!"
new_s=s.replace("world","python")
print(new_s)
# 4)Extract "ell" from "hello" using slicing only.
s="hello"
print(s[1:4])
# 5)Reverse the string "python" using slicing (no loops).
s="python"
print(s[::-1])
# 6)Combine "hello" and "world" into one string using string operations.
s1="hello"
s2="world"
result=s1+" "+s2
print(result)
# 7)Repeat the string "hi" to get "hihihi" using string operations.
s="hi"
print(s*3)
# 8)Check if "cat" exists in "concatenate" using a string operator.
s="concatenate"
print("cat" in s)
# 9)Count how many times "a" appears in "banana" using a string method.
s="banana"
print(s.count("banana"))
# 10)Remove leading and trailing spaces from " hello " using a string method.
s="hello"
print(s.strip())
# 11)Find the index of "o" in "hello" using a string method.
s="hello"
print(s.index("o"))
# 12)Split the string "a,b,c,d" into a list using a string method.
s="a,b,c,d"
print(s.split(","))
# 13)Join the list ["a","b","c"] into "abc" using a string method.
s=["a","b","c",]
a="".join(s)
print(a)
# 14)Extract every 2nd character from "abcdef" using slicing → expected "ace" .
s="abcdef"
print(s[::2])
# 15)Replace all "a" with "@" in "banana" using a string method.
s="banana"
print(s.replace("a","@"))
# 16)Check if "hello123" is alphanumeric using a string method.
s="hello123"
print(s.isalnum())
# 17)Capitalize the first letter of "python" using a string method.
s="python"
print(s.capitalize())
# 18)Convert "hello world" into "Hello World" using a string method.
s="hello world"
print(s.title())
# 19)Remove all vowels from "python" using string operations (no loops if possible 😈).
s="python"
print(s.replace("o",""))
# 20)Check if "madam" is a palindrome using slicing.
s="madam"
print(s==s)


