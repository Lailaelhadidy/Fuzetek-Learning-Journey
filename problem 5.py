def multiply_digits(n):
    product = 1
    while n != 0:
        d = n % 10
        product *= d
        n //= 10
    return product

x = int(input("Enter a number "))
print(multiply_digits(x))
