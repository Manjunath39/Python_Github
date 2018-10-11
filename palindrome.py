x=input("enter a string")
flag=0
l=len(x)

# while l%2==0:
#     print("not a palindrome")


for i in range(0,l//2+1):
    if x[i]!=x[-i-1]:
        flag=1
        break

if flag==1:
    print( "Not Palindrome")
else:
    print ("Palindrome")



 