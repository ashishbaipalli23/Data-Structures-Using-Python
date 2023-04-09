class Bubble:
    def __init__(self,arr:list) -> None:
        self.arr = arr
    def sort_fun(self):
       
        "this fuction is used to sort the array elements..with O(n**2)"    
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                   
                   self.arr[j],self.arr[j+1] = self.arr[j+1],self.arr[j]
        print('sorted array :',*self.arr) 
                  
n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
obj = Bubble(arr)
obj.sort_fun()



        