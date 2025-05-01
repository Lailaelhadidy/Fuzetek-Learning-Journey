def insertion_sort(myarray):
    for i in range(1, len(myarray)):
        k=myarray[i]
        j= i-1
        while j>=0 and k<myarray[j]:
            myarray[j+1] = myarray[j] #j+1 ==i
            j-=1
        myarray[j+1] = k
    return  myarray

myarray=[2, 4, 5, 1, 6, 7]
print(insertion_sort(myarray))

