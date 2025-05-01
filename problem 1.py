def replace(n):
    result= ""
    for d in n:
        name = ""
        if d == "0":
            name = "zero"
        elif d == "1":
            name = "one"
        elif d == "2":
            name = "two"
        elif d == "3":
            name = "three"
        elif d == "4":
            name = "four"
        elif d == "5":
            name = "five"
        elif d == "6":
            name = "six"
        elif d == "7":
            name = "seven"
        elif d == "8":
            name = "eight"
        elif d == "9":
            name = "nine"
        result += name

    return result


x= input("enter a number ")
print(replace(x))
