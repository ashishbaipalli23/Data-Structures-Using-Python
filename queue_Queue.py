from queue import Queue
class Queue1:
    
    def __init__(self):
        self.queue = Queue()
    def enqueue(self, data):
        self.queue.put(data)
    def dequeue(self):
        if not self.queue.empty():
            return self.queue.get()
        else:
            return ">>empty queue"
    def display(self):
        if not self.queue.empty():
            return self.queue
        else:
            return [">>empty queue"] 
q = Queue1()
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
    