def insertion_sort(arr:list)->list:
    ""
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr        

n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
print('sorted array :',*insertion_sort(arr))