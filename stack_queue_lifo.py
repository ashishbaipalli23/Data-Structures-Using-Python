from queue import LifoQueue
class Stack:
    """
    put() function to push data
    get() function to pop data
    self.stack.empty() function is check stack empty or not
    self.stack.queue --> data is present
    self.stack.qsize() --> length of the stack
    """
    def __init__(self) -> None:
        self.stack = LifoQueue()
    def push(self,data):
        self.stack.put(data) #put() function to push data
    def pop(self):
        if not self.stack.empty():
            return self.stack.get() #get() function to pop data
        else:
            return "empty stack"
    def peek(self):
        if not self.stack.empty():
           return self.stack.queue[-1]
        else:
            return "empty stack"  
    def display(self):
        if not self.stack.empty():
           return list(self.stack.queue)
        else:
            return ['empty stack']
st = Stack()
while True:
    print('\n1.push\n2.pop\n3.display\n4.peek\n5.quit')
    ch = int(input('enter your choice :'))
    if ch == 1:
        data = int(input('enter data into the stack :'))
        st.push(data)
    elif ch == 2:
        print(st.pop())
    elif ch == 3:
        print(*st.display())
    elif ch == 4:
        print(st.peek())    
    elif ch == 5:
        break
    else:
        print('invalid choice..')                    
                 
        