from collections import deque
class Queue:
    "popleft() == pop(0)"
    def __init__(self):
        self.queue = deque()
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        else:
            return ">>empty queue"
    def display(self):
        if len(self.queue) != 0:
            return self.queue
        else:
            return [">>empty queue"] 
q = Queue()
while True:
    print("===============QUEUE OPERATIONS================")
    print('1.enqueue\n2.dequeue\n3.display\n4.quit')
    ch = int(input('enter your choice :'))
    if ch == 1:
        data = int(input('enter data :'))
        q.enqueue(data)
    elif ch == 2:
        print(q.dequeue())
    elif ch == 3:
        print(*q.display())
    elif ch == 4:
        break
    else:
        print('invalid choice..')
    

