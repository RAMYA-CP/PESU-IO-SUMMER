#Write a Python program which accepts a sequence of comma-separated numbers from the user and generate a list and a tuple with those numbers. 
l=input().split(',')
list_n=[]
for i in l:
    list_n.append(int(i))
tuple_n=tuple(list_n)
print("THIS IS A LIST OF ELEMENTS:")
print(list_n)
print("THIS IS A TUPLE OF ELEMENTS:")
print(tuple_n)