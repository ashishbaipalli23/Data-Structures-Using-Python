class Stack:   
    def __init__(self, size:int):
        self.stack = []
        self.top = -1
        self.size = size

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.stack.append(item)
            print('inserted ...')
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.is_empty():
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            print("Stack Underflow")

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            return "under Flow"

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def display(self):      
       if not self.is_empty():
            for i in range(self.top+1):
                print(self.stack[i],end=" ")
       else:
           print('empty list')         

           
size = int(input('enter size :'))            
obj = Stack(size)
while True:
    print('\n1.push\n2.pop\n3.display\n4.peek\n5.quit')
    ch = int(input('enter your choice :'))
    if ch == 1:
        data = int(input('enter data into the stack :'))
        obj.push(data)
    elif ch == 2:
        print(obj.pop())
    elif ch == 3:
        obj.display()
    elif ch == 4:
        print(obj.peek())    
    elif ch == 5:
        break
    else:
        print('invalid choice..')                    
        
                    

    


