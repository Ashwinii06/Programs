def shipping_charge(num_items):

   if num_items <= 0:

       return 0

   elif num_items == 1:

       return 10.95

   else:

       return 10.95 + (num_items-1) * 2.95

num_items = int(input("Enter the number of items purchased: "))

shipping_cost = shipping_charge(num_items)

print("Shipping charge: $" + str(shipping_cost))