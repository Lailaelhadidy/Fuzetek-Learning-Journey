def unique_digits(n):
    d = n % 10
    x = d
    result= ""
    while n!=0:
        d=n%10
        if d==x:
            result="True"
        else:
             result="False"
             break
        n //= 10

    return result

y= int(input("enter number"))
print(unique_digits(y))
