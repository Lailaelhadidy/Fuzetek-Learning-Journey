def remove_digit(n, d):
    result= ""
    while n!=0:
        digit= n%10
        if digit!=d:
            result= str(digit) + result
        n//=10
    return int(result)

x= int(input("enter a number "))
y= int(input("enter the digit "))
print(remove_digit(x, y))

