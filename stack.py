

stack = [] #empty stack
top = -1

#push function, pushing the element x onto the stack
def push(x):
    global top ## this line is used to point out that the 'top' variable is the same as the one declared in line 4
    stack.append(x)
    top = top + 1

#pop function, returns the topmost element from the stack
def pop():
    global top ## this line is used to point out that the 'top' variable is the same as the one declared in line 4
    x = stack[top]
    top = top -1
    return x


##String reversal using stack

def ReverseString(str):
    ###complete your code here. 
    stack = list(str)
    rev = ''
    for i in range(1,len(stack)+1):
        rev = rev+stack[-i]
    return rev

ReverseString('Cloud Computing')

def ReverseString(str):
    stack = list(str)
    rev = ''
    for i, j in enumerate(stack):
        rev = rev+stack[-i-1]
    return rev

ReverseString('Cloud Computing')

