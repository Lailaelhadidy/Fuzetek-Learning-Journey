def selection_sort(myarray):
    for i in range(0, len(myarray)):
        for j in range(i+1, len(myarray)):
            if myarray[j] < myarray[i]:
                temp = myarray[i]
                myarray[i]= myarray[j]
                myarray[j]= temp
    return myarray


myarray=[2, 4, 5, 1, 6, 7]
print(selection_sort(myarray))