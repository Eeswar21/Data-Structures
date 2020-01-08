class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

    def show(self):
        return self.queue

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.show())
print(q.isEmpty())
print(q.dequeue())
q.enqueue(4)
print(q.size())
print(q.show())
print(q.dequeue())
print(q.show())
