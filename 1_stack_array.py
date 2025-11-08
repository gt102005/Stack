# It is the implementation of the stack using the list
class Stack(object):
    def __init__(self):
        self.top=-1
        self.size=100
        self.arr=[0]*self.size
    
    def push(self,data):
        self.top+=1
        self.arr[self.top]=data

    def pop(self):
        element=self.arr[self.top]
        self.top-=1
        print("popped element -->",element)

    def sizee(self):
        print("stack size -->",self.top+1)

    def topp(self):
        print("stack top -->",self.arr[self.top])
    
    
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.sizee()
stack.topp()
stack.pop()
stack.topp()