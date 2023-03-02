def findkmax(m, array):
    array.sort(reverse=True)
    print(array[m - 1])
def findkmin(n, array):
    array.sort()
    print(array[n - 1])
array=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    x=int(input("Enter the element:"))
    array.append(x)
m=int(input())
n=int(input())
findkmax(m, array)
findkmin(n, array)


