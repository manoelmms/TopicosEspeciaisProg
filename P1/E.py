import math

def partition(arr, l, r):
    
    x = arr[r]
    i = l
    for j in range(l, r):
        
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quick_select(arr, l, r, k):
    # if k is smaller than number of elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last element and get position of pivot element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur for left subarray 
        if (index - l > k - 1):
            return quick_select(arr, l, index - 1, k)

        # Else recur for right subarray 
        return quick_select(arr, index + 1, r, k - index + l - 1)

test_cases = int(input())

for i in range(test_cases):
    street = list(map(int, input().split()))
    #print(street)
    size = street.pop(0)

    #find median
    ss = sum(street)
    mean = ss //len(street)
    #print(mean)
    median = quick_select(street, 0, len(street), size//2)
    print(median)
    s = 0
    for i in street:
        s += abs(mean-i)
    print(s)