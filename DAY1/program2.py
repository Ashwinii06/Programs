l=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    x=int(input("Enter the element:"))
    l.append(x)
print(l)
def sumsquare(l):
    odd=0
    even=0
    for i in l:
       if i%2==0:
           even = even + i**2
       else:
           odd = odd + i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))

