def selection_sort(arr:list):
    "O(n**2)"
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #swaping 
        if min_idx != i:
            arr[i],arr[min_idx] = arr[min_idx],arr[i]                       
    return arr
n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
print('sorted array :',*selection_sort(arr))