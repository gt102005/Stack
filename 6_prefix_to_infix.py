"""This example is of the Prefix expression to the infix expression
   for this we have to traverse the expression form the right to the left 
   but while pushing back in the stack concatinate first top first andd then second top
"""
class Stack(object):
    def __init__(self):
        self.head=-1
        self.sizee=100
        self.arr=[0]*self.sizee
    def push(self,data):
        self.head+=1
        self.arr[self.head]=data
        return 
    def pop(self):
        popped=self.arr[self.head]
        self.head-=1
        return popped
    def top(self):
        return self.arr[self.head]
    def size(self):
        return self.head+1

def Prefix_to_Infix(expression):
    stack=Stack()
    for i in range(len(expression)-1,-1,-1):
        if expression[i].isalnum():
            stack.push(expression[i])
        else:
            first_top=stack.pop()
            second_top=stack.pop()
            exp="("+first_top+expression[i]+second_top+")"
            stack.push(exp)
    return stack.top()
expression="*+PQ-MN"
output=Prefix_to_Infix(expression)
print(output)

