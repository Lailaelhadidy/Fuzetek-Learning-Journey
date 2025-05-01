def sum_even(n):
    summ=0
    index=1
    while n != 0:
        d = n % 10
        if index%2==0:
            summ += d
        index += 1
        n //= 10
    return summ

x = int(input("Enter a number "))
print(sum_even(x))
