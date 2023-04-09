class Queue:
    def __init__(self) -> None:
        self.queue = []
    def add_element(self,data:int):
        self.queue.append(data)
    def remove_ele(self):
        if self.length() == 0:
            print('empty queue')
        else:
            del self.queue[0] #self.queue.pop(0)
            print('deleted sucessfully ..')   
        
    def length(self):
        return len(self.queue)
    def display(self):  
        if self.length() == 0:
            print('empty queue')
        else:     
            print('queue elements :',*self.queue)
obj = Queue()
while True:
    print('1.length of queue\n2.dispaly\n3.delete\n4.add element\n5.quit')
    ch = int(input('enter your choice :'))
    if ch == 1:
        print('length = ',obj.length())
    elif ch == 2:
        obj.display()
    elif ch == 3:
        obj.remove_ele()
    elif ch == 4:
        data = int(input('enter data into the queue :'))
        obj.add_element(data)  
    elif ch == 5:
        break
    else:
        print('invalid choice..')              




