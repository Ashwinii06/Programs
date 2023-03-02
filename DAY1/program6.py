def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
a=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    x=int(input("Enter the element:"))
    a.append(x)
len1 = len(a)
print(maxArea(a, len1))
 
