M = int(input("Enter the starting number of range: "))

N = int(input("Enter the ending number of range: "))

K = int(input("Enter the numbers to be skipped in range: "))

for i in range(M, N + 1, K):

   print(i)