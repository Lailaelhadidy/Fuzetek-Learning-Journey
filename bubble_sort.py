def bubble_sort(myarray):
    for i in range(0, len(myarray)):
        flag= False
        for j in range(0, len(myarray)-1-i):
            if myarray[j] > myarray[j+1]:
                temp = myarray[j]
                myarray[j]= myarray[j+1]
                myarray[j+1]= temp
                flag= True
        if flag == False:
            break #to break after the first round if the array was already sorted
    return myarray






myarray=[2, 4, 5, 1, 6, 7]
print(bubble_sort(myarray))