"""" The problem to convert the postfix expression in the Infix 
	 logic just add the operand in the stack top and stack second top and then again push the exparession in the stack 
"""
class Stack(object):
	def __init__(self):
		self.head=-1
		self.size=100
		self.arr=[0]*self.size
	def push(self,data):
		self.head+=1
		self.arr[self.head]=data
		return "Pushed >>"
	def pop(self):
		popped=self.arr[self.head]
		self.head-=1
		return popped
	def sizee(self):
		return self.head+1
	def top(self):
		return self.arr[self.head]

stack=Stack()
expression="AB-DE+F*/"
output=''
for i in range(len(expression)):
	if expression[i].isalnum():
		stack.push(expression[i])
	else:
		first_top=stack.pop()
		second_top=stack.pop()
		new_exp='('+second_top+expression[i]+first_top+")"
		stack.push(new_exp)
print("Input POstfix  Expression >>",expression)
print("Output Infix Expression >>",stack.top())
