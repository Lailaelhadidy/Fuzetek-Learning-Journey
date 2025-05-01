def counter(n, d):
    count=0
    while n!=0:
        digit=n%10
        if digit == d:
            count+=1
        else:
            count= count
        n//=10
    return count


x= int(input("enter a number "))
y= int(input("enter the digit "))
print(counter(x,y))

