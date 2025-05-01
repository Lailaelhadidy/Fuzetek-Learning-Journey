def digit_difference(n):
    largest=0
    difference=0
    smallest = n %10
    while n!=0:
        d=n%10
        if d>largest:
            largest=d
        if d<smallest:
            smallest=d
        n//=10
        difference = largest - smallest
    return difference

x=int(input("enter a number "))
print(digit_difference(x))
