#Stack Declaration and operations
class Stack(object):
    def __init__(self):
        self.size=100
        self.head=-1
        self.arr=[0]*self.size
    
    def push(self,data):
        self.head+=1
        self.arr[self.head]=data
        return data
    
    def pop(self):
        element=self.arr[self.head]
        self.arr[self.head]=0
        self.head-=1
        return element
    
    def top(self):
        return self.arr[self.head]

    def siz(self):
        return self.head+1
    
    def empty(self):
        if self.head==-1:
            return True
        else:
            return False


# String Reverse function 
def reverse_str(data):
    output=''
    for i in range(len(data)-1,-1,-1):
        if data[i]=='(':
            output+=')'
        elif data[i]==")":
            output+='('
        else:
            output+=data[i]
    return output

def sign_priority(sign):
    if sign=="^":
        return 3
    elif sign=="*" or sign=="/":
        return 2
    elif sign=="+" or sign=="-":
        return 1
    else:
        return -1

def infix_to_prefix(data):
    output=""
    n=len(data)
    i=0
    stack=Stack()
    while i<=n-1:
        if data[i].isalnum():
            output+=data[i]
        elif data[i]=="(":
            stack.push(data[i])
        elif data[i]==")":
            while not stack.empty() and stack.top()!="(":
                output+=stack.top()
                stack.pop()
            stack.pop()
        else:
            while stack.empty() and sign_priority(data[i])<=sign_priority(stack.top()):
                output+=stack.top()
                stack.pop()
            stack.push(data[i])
        i+=1
    while stack.empty()!=True:
        output+=stack.top()
        stack.pop()
    return output


string_str="(A+B)*C-D+F"
reversed_str=reverse_str(string_str)
answer=infix_to_prefix(reversed_str)
print(answer[::-1])




    


        

    
