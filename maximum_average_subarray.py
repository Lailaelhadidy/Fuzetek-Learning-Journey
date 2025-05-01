def findmaxaverage(nums: list[int], k:int) -> float:
    result=[]
    max=float(0)
    for i in range(0,len(nums)-3):
        sum=0
        for z in range(k):
            sum += nums[i + z]
        average= sum/k
        if average > max:
            max= average

    return max
list =[1,12,-5,-6,50,3]
print(findmaxaverage(list,4))






