#implement the single linked list
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class Singlelist:
    def __init__(self) -> None:
        self.head = None
    def length(self):
        l = 0
        temp = self.head
        if temp == None:
            return l
        else:
            while temp:
                l += 1
                temp = temp.next
        return l              
    def add_at_begin(self,data):
          new = Node(data)
          new.next = self.head
          self.head = new
          print('>>inserted sucessfully')
    def add_at_end(self,data):       
        if self.length() == 0:
            self.add_at_begin(data)
        else:
            new = Node(data)
            temp = self.head
            while  temp.next:
                temp = temp.next  
            temp.next = new
            print('>>inserted sucessfully')
    def add_at_middle(self,data,idx:int):
        if self.head == None:
            self.add_at_begin(data)
        elif idx > self.length():
            print(">>invalid index positon to insert")
        elif idx == 1:
            self.add_at_begin(data)   
        elif idx == self.length():
            self.add_at_end(data)     
        else:
            new = Node(data)
            temp = self.head

            for i in range(idx-1):
                temp = temp.next

            new.next = temp.next #right connection
            temp.next = new      #left connection 
            print('>>inserted sucessfully') 
    def display(self):
        temp = self.head
        if temp == None:
            print(">>empty list")
        else:
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next
    def delete_at_begin(self):
        if self.head == None:
            print(">>empty list")
        else:            
            temp = self.head.next
            self.head = temp
            temp = None
            print(">>deleted sucessfully")
    def delete_at_middle(self,idx):
        if idx > self.length():
            print(">>invalid location")
        else:
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
            temp.next = temp.next.next
            print(">>deleted sucessfully")            
    def delete_at_end(self):
        #travel to the end of the list
        temp = self.head.next
        while temp.next.next:
            temp = temp.next
        temp.next = None   
        

#starting data in the single linked list

n1 = Node(10)
l = Singlelist()
l.head = n1

n2 = Node(20)
n1.next = n2

n3 = Node(30)
n2.next = n3

def run_code(l):
    while True:
        print("\n1.insertion\n2. deletion\n3. display\n4. exit")
        x = int(input('enter your choice : '))
        if x == 1:
            print("\na)add_at_begin\nb)add_at_end\nc)add_at_middle")
            ch = input('enter your choice : ')
            if ch.lower() == 'a':
                data = int(input('enter data :'))
                l.add_at_begin(data)
            elif ch.lower() == 'b':
                data = int(input('enter data :'))
                l.add_at_end(data)
            elif ch.lower() == 'c':
                data = int(input('enter data :'))
                place = int(input('enter place to insert :'))
                l.add_at_middle(data,place)
            else:
                print('invalid choice')
        elif x == 2:
            print("\na)delete_at_begin\nb)delete_at_middle\nc)delete_at_end")
            ch = input('enter your choice : ')
            if ch.lower() == 'a':
                l.delete_at_begin()
            elif ch.lower() == 'b':
                position = int(input('enter position to delete :'))
                l.delete_at_middle(position)
            elif ch.lower() == 'c':
                l.delete_at_end()
            else:
                print('invalid choice')        
        elif x == 3:
            l.display()
        elif x == 4:
            break

run_code(l)        
            



