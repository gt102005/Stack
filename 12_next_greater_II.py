class Stack(object):
    def __init__(self):
        self.num=100
        self.top=-1
        self.arr=[0]*self.num


    def push(self,data):
        self.top+=1
        self.arr[self.top]=data

    def pop(self):
        element=self.arr[self.top]
        self.arr[self.top]=0
        self.top-=1
        return element

    def size(self):
        return self.top+1

    def head(self):
        return self.arr[self.top]

    def empty(self):
        if self.top==-1:
            return True
        else:
            return False

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        output = [-1] * n
        stack = []   # use list as stack

        for i in range(2 * n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                output[i % n] = nums[stack[-1]]
            stack.append(i % n)

        return output



nums = [1,2,3,4,3]
sol=Solution()
output=sol.nextGreaterElements(nums)
print(output)




