""" stack_size = 5
list = [None]*stack_size
top=-1

def isEmpty():
    if top == -1 : return True
    else : return False

def isFull():
    return top == stack_size-1

def push(e):
    global top
    if not isFull():
        top = top+1
        list[top] = e
        print(list)
    else:
        print("stack overflow")
        exit()

def pop():
    global top
    if not isEmpty():
        top = -1
        return list[top-1]
    else:
        print("stack underflow")
        exit()


def peek():
    if not isEmpty():
        return list[top]
    else : pass """


""" class CircularQueue :
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity
    def enqueue(self, item):
        //
    def dequeue(self):
        // """