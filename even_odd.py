a=[]
#my_comment

ab=int(input("no of elements in list"))
for i in range(ab):
    x=int(input("input number"))
    a.append(x)

print(a)
len=len(a)

def count():
    even = 0
    odd = 0
    for i in a:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd

even,odd=count()

print(even)
print(odd)