numbers = []

number = 1 
while ( number > 0):
   number = int(input("enter a number. put in a negative number to end "))
   if number > 0 :
      print (number)
      # save the number for later usage.
      numbers.append(number)

# calculate average
if len(numbers) == 0:
    print("You have not inputted anything. I need at least one value in order to calculate the average!")
else:
    print("The average of your numbers is: %s" % (sum(numbers) / len(numbers)))