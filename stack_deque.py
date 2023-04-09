from collections import deque
class Stack:
    def __init__(self) -> None:
        self.stack = deque()
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return "empty stack"
    def peek(self):
        if len(self.stack) !=0:
           return self.stack[-1]
        else:
            return "empty stack"  
    def display(self):
        if len(self.stack) !=0:
           return self.stack
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
                 
