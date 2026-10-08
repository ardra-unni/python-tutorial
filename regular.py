#1. re.search(pattern, string)

import re

# text = "Hello world" 
# print(re.search(r"world", text))

#2. re.match(pattern, string)

# text = "Hello world" 
# print(re.match(r"Hello", text)) 

# print(re.match(r"world", text)) 

#3. re.findall(pattern, string)

# text = "I have 2 apples and 5 oranges." 
# print(re.findall(r"\d+", text))
# print(re.findall(r"\D+", text))
# print(re.findall(r"a\s b", text))
# print(re.findall(r"\S+", text))
# print(re.findall(r"\w+", text))
# print(re.findall(r"\W+", text))

# text = "The price is 45 dollars, 30 cents, and 50 rupees." 
# print(re.findall(r"\d+", text))
# print(re.findall(r"\D+", text)) 
# print(re.findall(r"a\s b", text))
# print(re.findall(r"\S+", text))
# print(re.findall(r"\w+", text))
# print(re.findall(r"\W+", text))

#4. re.sub(pattern, repl, string)

# text = "Hello 123, welcome 456!" 
# print(re.sub(r"\d+", "number", text))  

#5. re.split(pattern, string)

# text = "apple, orange; banana, grape" 
# print(re.split(r"[;, ]", text))  

#1. re.IGNORECASE (or re.I )

# import re 

# text = "HELLO world" 
# print(re.search(r"hello", text, re.IGNORECASE)) 

#2. re.MULTILINE (or re.M )

# text = """first line 
# second line 
# third line"""
# print(re.findall(r"^s\w+", text, re.MULTILINE)) 
# print(re.findall(r"\w+e$", text, re.MULTILINE))  

#3. re.DOTALL (or re.S )

# text = "Hello\nWorld"
# print(re.search(r"Hello.*World", text)) 
# print(re.search(r"Hello.*World", text, re.DOTALL))  