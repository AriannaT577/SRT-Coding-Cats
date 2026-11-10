import random 
import time as t
#------Part A: List------
def random_list(size, lowest, highest): #three parameters
        return [random.randint(lowest, highest) for _ in range(size)]

numbers = (random_list(20, 10, 50)) #size of array, smallest value, largest value
#print(numbers)

test_array = [11, 4, 2, 8, 5, 6]
#print((test_array)) 

#------Part B: Sorts------
#--Bubble Sort--
def bubbleSort (array):
        n = len(array) #looking at all numbers of the array
        for i in range (n):
                swap = False 

                for j in range(0, n-i-1): 
                        if array[j] > array[j+1]:#j is first number, j+1 is the number next to it
                                array[j], array[j+1] = array[j+1], array[j] #swaps the values
                                swap = True

                if swap == False:
                    break #moves on to the next (i in range)

#bubbleSort(numbers)

#--Insert Sort--
def insertSort (array):
        n = len(array) #looking at all numbers of the array
        for i in range(1, n):
                key = array [i] 
                j = i - 1 
                while j >= 0 and key < array[j]: #prevents index out of range error
                        #if key < list[j]:
                        #array[j+1], array [j] = array [j], array [j+1] #swaps them
                        array[j + 1] = array[j]
                        j -= 1
                        
                array [j+1] = key #moves key into the sorted sport
                #print (list)

#insertSort(numbers)    
#insertSort(test_array)

#--Selection Sort--
def selectionSort(array):
        n = len(array)
        for i in range (n):
                smallest = i
                for j in range(i+1, n): #looks at each number right of smallest/sorted
                        if array[j] < array[smallest]: #if there is a smaller number
                                smallest = j
                array[i], array [smallest] = array [smallest], array [i] #swaps them

#selectionSort(numbers)    

#--Merge Sort--
def mergeSort(array):
        n = len(array)
        if n <= 1:
                return array #if its sorted (aka only one value)
        
        middle = n // 2 #divides in half
        #assigns list to right part and left part
        left = array[:middle]
        right = array[middle:]

        #print(array) #debugging

        #repeat
        left_sorted = mergeSort(left)
        right_sorted = mergeSort(right)

        result = [] #new list

        while len(left_sorted) > 0 and len(right_sorted) > 0: #if it has over 1 element
                if left_sorted[0] >= right_sorted [0]: #finds smallest
                        result.append (right_sorted[0]) #puts index in result
                        right_sorted = right_sorted[1:]  #removes first item
                else:
                        result.append (left_sorted[0])
                        left_sorted = left_sorted[1:] 

        result = [*result, *left_sorted, *right_sorted] #adds them together

        return result
       
#sorted_mergeSort = mergeSort(numbers)
#print (sorted_mergeSort)

#--Proper Merge Sort--
def mergeProper(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSortProper(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSortProper(arr, left, mid)
        mergeSortProper(arr, mid + 1, right)
        mergeProper(arr, left, mid, right)

def run_merge_sort_proper(arr):
    if len(arr) > 0:
        mergeSortProper(arr, 0, len(arr) - 1)


#print(test_array)
#print(numbers)

#------Part D: Testing Sorts------       
def time(sort, data):
    test_data = data.copy()
    
    start = t.time()
    sort(test_data)
    end = t.time()
    
    return end - start

#--input sizes--
rand_small = random_list(100, 1, 20)
rand_medium = random_list(1000, 1, 200)
rand_large = random_list(10000, 1, 2000)

#--reverse order lists--
reverse_small = list(range(100, 0, -1))
reverse_medium = list(range(1000, 0, -1))
reverse_large = list(range(10000, 0, -1))

#--sorted lists--
sorted_small = list(range(100))
sorted_medium = list(range(1000))
sorted_large = list(range(10000))

print("--- Testing Merge Sort ---")

#test random for all 3 sizes
t1 = time (run_merge_sort_proper, rand_small)
t2 = time(run_merge_sort_proper, rand_medium)
t3 = time(run_merge_sort_proper, rand_large)
print("Random (N=10, 100, 1000):", t1, t2, t3)

#test rever for all 3 sizes (worst case)
t1 = time(run_merge_sort_proper, reverse_small)
t2 = time(run_merge_sort_proper, reverse_medium)
t3 = time(run_merge_sort_proper, reverse_large)
print("Reverse (N=10, 100, 1000):", t1, t2, t3)

#test sorted for all 3 sizes (best case)
t1 = time(run_merge_sort_proper, sorted_small)
t2 = time(run_merge_sort_proper, sorted_medium)
t3 = time(run_merge_sort_proper, sorted_large)
print("Sorted (N=10, 100, 1000):", t1, t2, t3)

