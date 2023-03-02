m=int(input('Enter m: '))
n=int(input('Enter n: '))
for number in range(m,n+1):
    factor=0
    for i in range(1,number):
      if number%i==0:
        factor=i
    if factor>1:
      print (number)
