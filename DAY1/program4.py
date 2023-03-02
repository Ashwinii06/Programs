x=int(input("Enter the number: "))
def isPalindrome(x):
    if x < 0:
        return False
    number = x
    reverse = 0
    while number:
        reverse = reverse * 10 + number % 10
        number //= 10
    return x == reverse
print(isPalindrome(x))