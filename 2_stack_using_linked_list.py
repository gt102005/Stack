class Node(object):
    def __init__(self,data):
        self.next=None
        self.data=data

class Stack(object):
    def __init__(self):
        self.top=None

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
        return "---pushed--->>",data
    
    def pop(self):
        if self.top is None:
            return "No Element"
        popped=self.top.data
        self.top=self.top.next
        return "---popped--->",popped
    
    def peek(self):
        if self.top is None:
            return "Not Found Peek"
        return "---peek--->",self.top.data

    def display(self):
        current=self.top
        while current:
            print(">>",current.data,end="")
            current=current.next
        print()

stack=Stack()
print(*stack.push(10))
print(*stack.push(20))
print(*stack.push(30))
print(*stack.push(40))
print(*stack.push(50))
print(*stack.push(70))
print(*stack.pop())
print(*stack.pop())
print(*stack.peek())
stack.display()

