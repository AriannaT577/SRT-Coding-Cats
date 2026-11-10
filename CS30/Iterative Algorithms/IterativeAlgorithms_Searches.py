import random 
import time as t

#------Part E: Searches------
#--Linear Search--
def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

#--Binary Search--
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


#------Part F: Testing Searches------       
def time(search, data, targetVal):
    test_data = data.copy()
    
    start = t.time()
    search(test_data, targetVal)
    end = t.time()
    
    return end - start

#--input sizes (using sorted range lists for valid binary search)--
small = list(range(100))
medium = list(range(1000))    
large = list(range(10000))     

print("--- Testing Linear Search ---")

#test best case (target at index 0)
t1 = time(linearSearch, small, 0)
t2 = time(linearSearch, medium, 0)
t3 = time(linearSearch, large, 0)
print("Best Case (N=100, 1000, 10000):", t1, t2, t3)

#test worst case (target missing -1)
t1 = time(linearSearch, small, -1)
t2 = time(linearSearch, medium, -1)
t3 = time(linearSearch, large, -1)
print("Worst Case (N=100, 1000, 10000):", t1, t2, t3)

#test average case (target in middle)
t1 = time(linearSearch, small, 50)
t2 = time(linearSearch, medium, 500)
t3 = time(linearSearch, large, 5000)
print("Average Case (N=100, 1000, 10000):", t1, t2, t3)


print("\n--- Testing Binary Search ---")

#test best case (target at middle index)
t1 = time(binarySearch, small, 49)
t2 = time(binarySearch, medium, 499)
t3 = time(binarySearch, large, 4999)
print("Best Case (N=100, 1000, 10000):", t1, t2, t3)

#test worst case (target missing -1)
t1 = time(binarySearch, small, -1)
t2 = time(binarySearch, medium, -1)
t3 = time(binarySearch, large, -1)
print("Worst Case (N=100, 1000, 10000):", t1, t2, t3)

#test average case (target at 75% position)
t1 = time(binarySearch, small, 75)
t2 = time(binarySearch, medium, 750)
t3 = time(binarySearch, large, 7500)
print("Average Case (N=100, 1000, 10000):", t1, t2, t3)