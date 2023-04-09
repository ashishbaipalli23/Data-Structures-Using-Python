class Linear:
    def __init__(self,arr:list,key:int) -> None:
        self.arr = arr
        self.key = key
    def search(self):
        "main logic in the linear search"
        for i in range(len(self.arr)):
            if self.arr[i] == self.key:
                print(f'{self.key} found at index {i}')
                break
        else:
            print("element not found")
n = int(input('enter size :'))                
arr = [int(i) for i in input('enter elements :').split()[:n]]
key = int(input('enter key :'))
obj = Linear(arr,key)
obj.search()                


        