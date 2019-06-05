#Write a python program for binary search to search a number in the list of given numbers. If the number isn't present, give the appropriate message. Both the list and the number to be searched is given by the user. 
l=input().split(',')
list_n=[]
for i in l:
    list_n.append(int(i))
list_n=sorted(list_n)
num=int(input("ENTER THE NUMBER TO BE SEARCHED:"))
low=0
high=len(list_n)-1
c=0
while(high>=low and c==0):
    mid=int((high+low)/2)
    if(list_n[mid]==num):
        print("ELEMENT FOUND!")
        c+=1
    elif(list_n[mid]>num):
        high=mid-1
    else:
        low=mid+1
if(c==0):
    print("ELEMENT NOT FOUND!!!")
