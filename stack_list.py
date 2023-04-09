class Stack:
    def __init__(self) -> None:
        self.stack = []
    def add_element(self,data:int):
        self.stack.append(data)

    def remove_ele(self):
        if self.length() == 0:
            print('empty stack')
        else:
            self.stack.pop()   
        
    def length(self):
        return len(self.stack)
    def display(self):  
        if self.length() == 0:
            print('empty stack')
        else:     
            print('stack elements :',*self.stack)
    def peek(self):
        if not self.length() == 0:        
            return self.stack[-1]
        else:
            return "empty stack"
obj = Stack()
while True:
    print('1.peek\n2.dispaly\n3.pop\n4.push\n5.quit')
    ch = int(input('enter your choice :'))
    if ch == 1:
        print(obj.peek())
    elif ch == 2:
        obj.display()
    elif ch == 3:
        obj.remove_ele()
    elif ch == 4:
        data = int(input('enter data into the stack :'))
        obj.add_element(data)  
    elif ch == 5:
        break
    else:
        print('invalid choice..')              




