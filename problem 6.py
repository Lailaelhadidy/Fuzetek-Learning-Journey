def contains_digit(n, d):
    while n!=0:
        digit=n%10
        if digit == d:
            return True
        n //= 10
    return False



x= int(input("enter a number "))
y= int(input("enter the digit "))
print(contains_digit(x,y))
