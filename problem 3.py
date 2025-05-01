def sum_digits(x):
    n=x
    length = 0
    while n > 0:
        length += 1
        n //= 10

    summ=0
    place=0
    position=0
    n=x
    while n!=0:
        d=n%10
        position=length-place
        summ+= d**position
        place += 1
        n//=10
    return summ

z=int(input("enter a number "))
print(sum_digits(z))
