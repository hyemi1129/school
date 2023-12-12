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


""" class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFUll(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = e
            print(self.list)
        else:
            print("stack overflow")
            exit()

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.list[self.top + 1]
        else:
            print("stack underflow")
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.list[self.top]
        else:
            pass """


# 원형 큐

MAX_QSIZE = 10
class CircularQueue :
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE

    def clear(self):
        self.front = self.rear
    
    def __len__(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]


    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    
    def print(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]

        print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)
        


# 원형 덱

class CircularDeque(CircularQueue):
    
    def __init__(self):
        super().__init__()

    def addRear (self, item):
        self.enqueue(item)

    def deleteFront (self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1 + MAX_QSIZE) % MAX_QSIZE
            return item

    def getRear(self):
        return self.items[self.rear]
    

# 선형 큐

class Queue:
    def __init__(self):
        self.front = self.rear = -1
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            self.front += 1
            return self.queue[self.front]

    def is_full(self):
        if self.rear == len(self.queue)-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        






class ArrayStack:
    def __init__(self, capacity): # 초기화
        self.capacity = capacity  # 스택 최대 용량
        self.list = [None] * capacity  # 스택 요소를 저장하는 리스트
        self.top = -1  # 스택 비어 있게

    def isEmpty(self): # 스택 빈 코드
        return self.top == -1

    def isFull(self): # 스택 가득 찬 코드
        return self.top == self.capacity - 1

    
    def push(self, e): # 값 넣기
        if not self.isFull():  # 스택이 가득 찼는지
            self.top += 1  # 넣기
            self.list[self.top] = e  # 리스트 안 탑
            print(self.list)  # 스택 출력
        else:
            print("stack overflow")  # 가득 찼다는 문장 출력
            exit()  # 나가기

    def pop(self): # 빼내기
        if not self.isEmpty():  # 스택이 비었나 확인
            self.top -= 1  # 빼기
            return self.list[self.top + 1]  # 반환
        else:
            print("stack underflow")  # 다 뺐다는 문장 출력
            exit()  # 나가기

    def peek(self): # 빼내고 반환?
        if not self.isEmpty():  # 스택이 비었나 확인
            return self.list[self.top]  # 반환
        else:
            pass  # 패스




MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0  # 맨 앞 초기화
        self.rear = 0   # 맨 뒤 초기화
        self.items = [None] * MAX_QSIZE  # 요소 저장

    def isEmpty(self): # 비었나
        return self.front == self.rear  # front와 rear가 같이 있으면 비어있음

    def isFull(self): # 가득찼나
        return self.front == (self.rear + 1) % MAX_QSIZE  # front와 rear가 순환하면 가득참

    def enqueue(self, item): 
        if not self.isFull():  # 큐가 가득 차지 않았으면
            self.rear = (self.rear + 1) % MAX_QSIZE  # rear를 다음 위치로 이동
            self.items[self.rear] = item  # 해당 위치에 값 저장

    def dequeue(self):
        if not self.isEmpty():  # 큐가 비어있지 않으면
            self.front = (self.front + 1) % MAX_QSIZE  # front를 다음 위치로 이동하고
            return self.items[self.front]  # 해당 위치의 값 반환

    def peek(self):
        if not self.isEmpty():  # 큐가 비어있지 않으면
            return self.items[(self.front + 1) % MAX_QSIZE]  # 다음 값 반환

    def clear(self): # 비우기
        self.front = self.rear  # 큐를 비우기

    def __len__(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE  # 현재 큐의 길이 반환
    
    def twodequeue(self): # 두개 이동
        if front >= 2: # front 2번 이상
            return self.items[self.front] # 2 개 반환



class Queue:
    def __init__(self, capacity):
        self.front = self.rear = -1  # 큐 앞 뒤 초기화
        self.queue = [0] * capacity # 큐 길이

    def enqueue(self, data): # 삽입
        if self.is_full():  # 큐가 가득 찼으면
            print('큐가 다 찼습니다.')  # 오류 메시지 출력
        else:
            self.rear += 1  # 뒤 증가
            self.queue[self.rear] = data  # 큐에 값 저장

    def dequeue(self): # 삭제
        if self.isempty():  # 큐가 비어있으면
            print('큐가 비었습니다.')  # 오류 메시지 출력
        else:
            self.front += 1  # 앞 증가가
            return self.queue[self.front]  # 큐에서 값 반환

    def isfull(self):
        if self.rear == len(self.queue) - 1:  # 가득찼음
            return True 
        else:
            return False

    def isempty(self):
        if self.front == self.rear:  # 비었음
            return True
        else:
            return False



class Queue:
    def __init__(self):
        self.front = self.rear = -1  # 큐의 전면과 후면을 -1로 초기화
        self.queue = [0] * 5  # 큐를 길이 5의 배열로 초기화

    def enqueue(self, data):
        # 제일 뒤에 삽입
        if self.is_full():  # 큐가 가득 찼으면
            print('큐가 다 찼습니다.')  # 오류 메시지 출력
        else:
            self.rear += 1  # 후면을 증가시켜서 다음 위치에 데이터 삽입
            self.queue[self.rear] = data  # 큐에 데이터 저장

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():  # 큐가 비어있으면
            print('큐가 비었습니다.')  # 오류 메시지 출력
        else:
            self.front += 1  # 전면을 증가시켜서 다음 위치의 데이터를 반환
            return self.queue[self.front]  # 큐에서 데이터 반환

    def is_full(self):
        if self.rear == len(self.queue) - 1:  # 후면이 배열 길이 - 1과 같으면 큐가 가득 찬 상태
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:  # 전면과 후면이 같으면 큐가 비어있는 상태
            return True
        else:
            return False


class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity  # 덱의 최대 크기 설정
        self.deque = [None] * self.capacity  # 덱을 초기화
        self.front = self.rear = -1  # 덱의 앞 뒤 초기화

    def isfull(self):
        return (self.rear + 1) % self.capacity == self.front  # 덱이 가득 찼는지

    def isempty(self):
        return self.front == self.rear == -1  # 덱이 비어있는지

    def addrear(self, data):
        if self.is_full():  # 덱이 가득 찼으면
            print('덱이 다 찼습니다.')  # 오류 메시지 출력
        else:
            if self.isempty():  # 덱이 비어있으면
                self.front = self.rear = 0  # 전면과 후면을 0으로 설정
            else:
                self.rear = (self.rear + 1) % self.capacity  # 뒤 증가 값 저장
            self.deque[self.rear] = data  # 덱에 값 저장

    def deletefront(self):
        if self.isempty():  # 덱이 비어있으면
            print('덱이 비었습니다.')  # 오류 메시지 출력
            return None
        removed_data = self.deque[self.front]  # 값 저장
        if self.front == self.rear:  # front rear 같으면
            self.front = self.rear = -1  # 덱 비우기
        else:
            self.front = (self.front + 1) % self.capacity  # 앞 증가
        return removed_data  # 덱에서 값 반환

    def getfront(self):
        if self.isempty():  # 덱이 비어있으면
            print('덱이 비었습니다.')  # 오류 메시지 출력
            return None
        return self.deque[self.front]  # 현재 앞 값 반환

    def delete_rear(self):
        if self.isempty():  # 덱이 비어있으면
            print('덱이 비었습니다.')  # 오류 메시지 출력
            return None
        removed_data = self.deque[self.rear]  # 현재 뒤의 데이터를 저장
        if self.front == self.rear:  # front rear 같으면
            self.front = self.rear = -1  # 비우기
        else:
            self.rear = (self.rear - 1) % self.capacity  # 감소 다음 위치
        return removed_data  # 값 반환

    def get_rear(self):
        if self.isempty():  # 비어있으면
            print('덱이 비었습니다.')  # 오류 메시지 출력
            return None
        return self.deque[self.rear]  # 값 반환



class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)  # 추가

    def deleteFront(self):
        return self.dequeue()  # 제거 반환

    def getFront(self):
        return self.peek()  # 꺼내기?

    def addFront(self, item):
        if not self.isFull():  # 안비었으면
            self.items[self.front] = item  # 추가
            self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE  # 다음 위치

    def deleteRear(self):
        if not self.isEmpty():  # 비었나
            item = self.items[self.rear]  # 저장
            self.rear = (self.rear - 1 + MAX_QSIZE) % MAX_QSIZE  # 다음
            return item  # item 반환

    def getRear(self):
        return self.items[self.rear]  # 반환
