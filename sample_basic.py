#reading files
#read() method

# a=open("sample.txt","r")
# content=a.read()
# print(content)
# a.close()

#readline() method

a=open("sample.txt","r")
print(a.readline())
print(a.readline())
a.close()

#readlines() method

a=open("sample.txt","r")
print(a.readlines())
a.close()

#writing to files
#write() method

a=open("sample.txt","w")
a.write("hello,world!")
a.close()

#writelines() method






