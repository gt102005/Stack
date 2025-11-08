class Stack(object):
    def __init__(self):
        self.head=-1
        self.sizee=100
        self.arr=[0]*self.sizee
    def push(self,data):
        self.head+=1
        self.arr[self.head]=data
        return
    def top(self):
        return self.arr[self.head]
    def pop(self):
        popped=self.arr[self.head]
        self.head-=1
        return popped
    def size(self):
        return self.head+1
stack=Stack()
def PostFix_to_PreFix(expression):
    for i in expression:
        if i.isalnum():
            stack.push(i)
        else:
            first_top=stack.pop()
            second_top=stack.pop()
            new_exp=i+second_top+first_top
            stack.push(new_exp)
    return stack.top()

expression='AB-DE+F*/'
print(PostFix_to_PreFix(expression))