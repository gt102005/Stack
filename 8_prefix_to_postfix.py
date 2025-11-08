# Converting the Prefix expression to the Postfix expression 

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
stack=Stack()
def Prefix_to_Postfix(expression):
    for i in range(len(expression)-1,-1,-1):
        if expression[i].isalnum():
            stack.push(expression[i])
        else:
            first_top=stack.pop()
            second_top=stack.pop()
            new_exp=first_top+second_top+expression[i]
            stack.push(new_exp)
    return stack.top()

expression='/-AB*+DEF'
output=Prefix_to_Postfix(expression)
print(output)
