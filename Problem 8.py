def swap(n):

    n=str(n)
    n_list = list(n)

    n_list[0], n_list[-1] = n_list[-1], n_list[0]
    number = int("".join(n_list))
    return number


y = int(input("Enter a number: "))
print(swap(y))






