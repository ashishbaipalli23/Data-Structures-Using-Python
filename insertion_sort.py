def insertion_sort(arr:list)->list:
    ""
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and temp<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr        

n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
print('sorted array :',*insertion_sort(arr))