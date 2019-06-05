#Write a Python program to calculate the sum of the digits in an integer.
num=int(input("ENTER THE NUMBER:"))
p=num
q=0
while(p>0):
    q+=p%10
    p=p//10
print("the sum of the digits is:")
print(q)