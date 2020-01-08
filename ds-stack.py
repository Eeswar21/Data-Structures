#Last In First Out - Stack

class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return len(self.stack)==0

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

st=Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.show())
print(st.isEmpty())
print(st.peek())
print(st.pop())
print(st.show())
st.push(4)
print(st.show())
        
