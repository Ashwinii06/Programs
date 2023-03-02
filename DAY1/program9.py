E=[]
L=[]
T = int(input())
for i in range(T):
    e=int(input())
    E.append(e)
for i in range(T):
    l=int(input())
    L.append(l)
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("output", Max)