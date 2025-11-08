class Stack(object):
    def __init__(self):
        self.head=-1
        self.sizee=100
        self.arr=[0]*self.head
    def push(self,data):
        self.head+=1
        self.arr[self.head]=data
        return
    def pop(self):
        temp=self.arr[self.head]
        self.head-=1
        return temp
    def size(self):
        return self.head+1
    def top(self):
        return self.arr[self.head]
    def empty(self):
        if self.head==-1:
            return True
        else:
            return False
    
class Solution(object):
    def Min_Element(self,num1):
        nextGreater={}
        for i in range(len(num1)):
            j=(i+1)//len(num1)
            while j<=len(num1):
                print(j)
                j=j+1
        

arr=[1,2,1]
obj=Solution()
obj.Min_Element(arr)
