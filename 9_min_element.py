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
        if self.head<0:
            return -1
        else:
            return self.arr[self.head]
    def size(self):
        return self.head+1
    def pop(self):
        if self.head==-1:
            return None
        temp=self.arr[self.head]
        self.head-=1
        return temp
    def empty(self):
        if self.head<0:
            return True
        else:
            return False
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=Stack()
        nextGreaterElement={}
        for num in nums2:
            while (not stack.empty()) and stack.top() < num:
                nextGreaterElement[stack.pop()]=num
            stack.push(num)
        while not stack.empty():
            nextGreaterElement[stack.pop()]=-1   
        return [nextGreaterElement[num] for num in nums1]
        

            



nums1 = [4,1,2]
nums2 = [1,3,4,2]
obj=Solution()
print(obj.nextGreaterElement(nums1,nums2))
