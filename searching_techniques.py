def linear_search(myarray, target):
    for i in range(len(myarray)):
        if myarray[i] == target:
            return print(f"the index of the target is index {i}")
        return print("Target was not found")

def binary_search(myarray, target):
    low=0
    high= len(myarray) - 1
    while low <= high:
        mid= len(myarray) // 2
        if target==myarray[mid]:
            return print(f" index of target is {mid}")
        elif myarray[mid] < target:
            low= mid+1
        elif myarray[mid] > target:
            high = mid-1
    return print("Target was not found")

def binary_search_recursive(myarray, target, low, high):
    if low > high:
        return print("Target was not found")

    mid = (low + high) // 2

    if myarray[mid] == target:
        return print(f"Index of target is {mid}")
    elif myarray[mid] < target:
        return binary_search_recursive(myarray, target, mid + 1, high)
    else:
        return binary_search_recursive(myarray, target, low, mid - 1)

myarray=[2, 4, 5, 1, 6, 7]
binary_search_recursive(myarray, 6, 0 , 6)