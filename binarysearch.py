class Binary:
    def __init__(self,arr:list,key:int) -> None:
        self.arr = arr
        self.key = key
    def search(self):
        """This function takes only a sorted array and a target value 'x',
           and returns the index of the first occurrence of 'x' in the array.
           O(logn)->worest case
        """
        l = 0
        h = len(self.arr)-1
        #mid = (l+h)//2
        while(l<=h):
            mid = (l+h)//2
            if self.arr[mid] == self.key:
                print(f'{self.key} found at index {mid}')
                break
            elif self.arr[mid] > self.key:
                h = mid - 1
            elif self.arr[mid] < self.key:
                l = mid + 1    
        else:
            print("element is not found") 

n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
key = int(input('enter key :'))
obj = Binary(arr,key)
obj.search()             
                



               

            
            
    

            
