class Stack(object):
    def __init__(self):
        self.top=-1
        self.length=100
        self.arr=[0]*self.length
        self.size=0

    def push(self,data):
        if self.top == self.length:
            return "stack overflow"
        else:
            self.top+=1
            self.arr[self.top]=data
            self.size+=1
        return "Inserted >>",data
    
    def peek(self):
        return "Top >>",self.arr[self.top]
    
    def pop(self):
        temp=self.arr[self.top]
        self.arr[self.top]=0
        self.top-=1
        return "Popped >>",temp

    def empty(self):
        if self.top==-1:
            return True

    def valid_paranthesis(self,s):
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                self.push(s[i])
            else:
                if self.empty():
                    return False
                else:
                    if (s[i]=="]" and self.arr[self.top]=='[') or (s[i]=="}" and self.arr[self.top]=='{') or (s[i]==")" and self.arr[self.top]=='('):
                        self.pop()
                    else:
                        return False
        if self.empty():
            return True
        else:
            return False





stack=Stack()
s='[[]{}{]()'
print(stack.valid_paranthesis(s))


