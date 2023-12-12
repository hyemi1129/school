""" 
a = input()
a = int(a)

sum=0
for i in range(1, a+1):
    if a%2==0 :
        sum+=i
    
print(sum) 
"""


""" 8/21 """

""" 
a = int(input())
b = int(input())
print(a+b) """

""" 
boolean bool
a=True
b=False
print(a)

&& || ! 대신
and or not 적으면 됨
ex)print(a and b)
"""

""" 
if(a): 콜론
    들여쓰기하기 ()대신 들여쓰기
elif: = else if()

if a and b 괄호 없음



반복문
for i in range( , , ): -> 괄호에 하나만 써도됨 5번 반복시킬거면
for i in range(5):
    print(i) 

결과 값 : 
0 -> 0부터 시작
1
2
3
4 


ex)
for i in range(0,5,1): = 0부터 5까지 1부터 증가시키기
for i in rane(5, 0, -1):



while문 

while True: -> 무한루프
    print("hello") 

printf()랑 print()차이
줄바꿈, ; X
"""

""" 
6069
a = input()
if a == 'A':
    print("best!!!")
elif a == 'B':
    print("good!!")
elif a == 'C':
    print("run!")
elif a == 'D':
    print("slowly~")
else:
    print("what?")
"""

""" 
6070
a = int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")
"""

""" 
6073
a = int(input())
while a!=0:
    a-=1
    print(a)
"""

""" 
6075
a = int(input())
b = 0
while b<=a:
    print(b)
    b+=1
"""

""" 
6077
a = int(input())
b = 0
for i in range(1, 1+a):
    if i%2==0:
        b += i

print(b)
"""

"""
6079
a = int(input())
b = 0
c = 0
while b < a:
    c+=1
    b+=c

print(c)
"""

""" 
6080
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)
"""

""" 
6083
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
for i in range(0, r) :sss
  for j in range(0, g) :
    for k in range(0, b) :
      print(i, j, k)

print(r*g*b)
"""

""" 
6088
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s)
"""

""" 
6089
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a)
"""

""" 
6090
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a*m+d

print(a)
"""


"""
a = (1, 2, 3)
type(a)

b = 1, 2, 3
type(b)

a = [1, "가", 2, "나"]
b = tuple(a)
b
c = tuple(range(1, 15, 2))
c 
"""

""" 
a = (1, 2, 3, 4, 5)
a[2]
a[1:3]
b = list(a)
ba = (1, 2, 3, 4, 5, 4, 3, 2, 1)
3 in a
3 not in a
a.count(3)
a.index(5)
"""

"""
a = set([1, 2, 3, 4, 5])
b = {3, 4, 5, 6, 7}
a | b


from gtts import gTTs
ss
text = "안녕하세요 부소마입니다."
tts=gTTs(text-text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환/hi.mp3)
"""


"""
b_list = []
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)
"""

"""
c_list = [1, 3.14, "hello", [1, 2, 3]]
print(c_list)
print(c_list[1:3])
"""

"""
d = [[0 for j in range(20)] for i in range(20)]
n = int(input())
for i in range(n):    
   x,y = map(int,input().split())    
   d[x][y] = 1

for i in range(1,20):    
   for j in range(1,20):        
      print(d[i][j], end=' ')   
   print()
 """

""" def o(n):
    if n == 1:
        print(1)
    else:
        o(n-1)
        print(n)

o(int(input())) """

""" def o(n):
    if n == 1:
        print(1)
    else:
        print(n)
        o(n-1)

o(int(input())) """

""" def o(a, b):
    if a%2 == 1:
        print(a)
    if a == b:
        return
    o(a+1, b)
a, b = map(int, input().split())

o(a, b) """

""" def profile(name, age, language):
	print("이름: {0}\t나이: {1}\t 주사용언어: {2}".format(name, age, language))
	
profile("뭐시기", "17", "알랄라")

=

def profile(name, age = 17, language = "알랄라"):
	print("이름: {0}\t나이: {1}\t 주사용언어: {2}".format(name, age, language))
	
profile("뭐시기") """

""" def f(n):
    if n ==1:
        return 1
    return n*f(n-1)

t = int(input())
print(f(t)) """

""" def d(n):
    if n//2 == 0:
        return str(n%2)
    return d(n//2)+str(n%2)

N = int(input())
print(d(N)) """

""" def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(f"Disk {n} : {from_pos} to {to_pos}")
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(f"Disk {n} : {from_pos} to {to_pos}")
    hanoi(n - 1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1, 'A', 'C', 'B')
print("n = 2")
hanoi(2, 'A', 'C', 'B')
print("n = 3")
hanoi(3, 'A', 'C', 'B') """

""" def mysubstr(word,start,count):
    for i in range(count):
        #끝이 개행문자x 띄어쓰기x (cde처럼 바로 뒤에 출력)
        print(word[start+i],end='')
w=input()
s,c=map(int,input().split())
mysubstr(w,s,c) """

""" 
리스트 값 다 더하기

n = input().split()
sum = int(0)

for i in range(5) :
    n[i] =int(n[i])

for i in range(5) :
    sum += n[i]

print(sum)
"""

""" 
수행평가(리스트를 가지고 함수로 아무거나 그냥 다함)

1. 리스트 값 다 더하기 (재귀함수)
"""

""" 
def a(n):
    if not n:
        return 0

        return n[0] + a(n[1:])

my_list = [1, 2, 3, 4, 5]

result = a(my_list)
print(result)
"""

""" def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum

print(list_sum([1, 2, 3, 4, 5])) """

""" 
d = [[0 for j in range(20)] for i in range(20)]
n = int(input())
for i in range(n):    
   x,y = map(int,input().split())    
   d[x][y] = 1

for i in range(1,20):    
   for j in range(1,20):        
      print(d[i][j], end=' ')   
   print()
"""

""" def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) """

""" import time
import random

WORD_LIST=[
    "아무 문장이나 적으세요",
    "코딩하는 하루 되세요",
    "여러분 화이팅",
    "오늘 급식 뭐죠?"
]

random.shuffle(WORD_LIST)

for i in WORD_LIST:
    start_time=time.time()
    user_input=str(input(i+'\n')).strip()
    end_time=time.time()-start_time

    correct = 0
    for index, c in enumerate(user_input):
        if index >= len(i):
            break
        if c == i[index]:
            correct+=1

    total_len=len(i)
    c = correct/total_len*100
    e = (total_len-correct)/total_len*100
    speed=correct / end_time *60

    print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".format(speed,c,e)) """

""" class Bssm:
    def __init__(self, task, age, name):
        self.team="부소마" #Bssm클래스로 찍어낸 객체들은 모두 team 변수에 부소마가 들어가도록
        self.task=task #나머지는 다 다르게
        self.age=age
        self.name=name
        
    def intro(self):
        print("안녕하세요, %s에서 %s를 담당하고 있는 %d살 %s입니다." %(self.team, self.task, self.age, self.name)) """

""" class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score=score
    def s_grade(self):
        if self.score >= 90:
            self.grade="A"
        elif self.score >= 80:
            self.grade="B"
        else:
            self.grade="C"
    def __str__(self):
        return "%s: %c 등급" %(self.name, self.grade)
    
a1 = Grade("이름", 89)
a1.s_grade()
print(a1) """

"""문자열 거꾸로 출력"""
""" s = 'abcde'

for i in range(len(s)-1, -1, -1):
    print(s[i], end='') """

""" s = 'abcde'

s_reverse = ''
for char in s:
    s_reverse = char + s_reverse
    print(s_reverse) """

""" 거꾸로 출력하기 겁나 쉬운 방법 """
""" s = 'abcde'
print(s[::-1]) """

""" 
ex)
s = 'abcde'
print(s[3::1]) # -> [start:end:stop]
"""


""" n = int(input())

for i in range(1, 7):
    for j in range(1, 7):
        if i+j == n:
            print(i, j) """


""" a, b = map(int, input().split())

while a%b != 0:
    a, b = b, a%b

print(b) """

""" 재귀함수로 바꾼거 ↓ """

""" def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

x, y = map(int, input().split())
result = gcd(x, y)
print(result) """

""" 다른 재귀함수 ↓ """

""" a, b = map(int, input().split())

def gcd(a, b):
    if a%b==0:
        return b
    return gcd(b, a%b)

print(gcd(a,b)) """


""" 최대공약수 구하기 """

""" def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
a, b = map(int, input().split())
print(gcd(a, b)) """

""" a, b = map(int, input().split())

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)
print(gcd(a, b)) """

""" a = int(input())
cnt = 0

for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    if a // i != 0:
        cnt += a//i
        a = a%i

print(cnt) """

""" class FishCakeMaker:
    def __init__(self, **kwargs): # 가변인자매개변수이기 때문에 **이 붙음 → 매개변수 자리의 개수 지정 X / init 초기화
        self.size=10
        self.flavor="팥"
        self.price=100

        if "size" in kwargs:
            self.size = kwargs.get("size") # kwargs 딕셔너리 안에 size라는 key값이 있냐? 있다면 가져와서 size 변수에 대입
        if "flavor" in kwargs:
            self.flavor=kwargs.get("flavor")
        if "price" in kwargs:
            self.price=kwargs.get("price")

    def show(self):
        print("붕어빵 크기 {}".format(self.size))
        print("붕어빵 종류 {}".format(self.flavor))
        print("붕어빵 가격 {}".format(self.price))
        print("*"*30)

fish1=FishCakeMaker() # **을 붙였기 때문에 안넣어도 됨
fish2=FishCakeMaker(size=20, price=300)
fish3=FishCakeMaker(flavor="초콜릿", size=15)

fish1.show()
fish2.show()
fish3.show()

#붕어빵기계 클래스를 상속받은 마켓굿즈

class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.market_price = self.price + margin
    def show(self):
        print(self.flavor, self.market_price)

fish1 = MarketGoods(size=20, price=500)
fish1.show()
"""

""" class Country:

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

class Korea(Country):

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            .format(self.name, self.population, self.capital)
        ) """


# 스택 응용

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFUll(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
            print(self.array)
        else:
            exit()

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

# 연산자 우선순위 계산 함수
def precedence(op):
    if op == '*' or op == '/': return 2
    elif op == '+' or op == '-': return 1
    elif op == '(' or op == ')': return 0
    else : return -1

# 중위표기 -> 후위표기로 바꾸는 함수
def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
              s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
            
        elif term in "*/+-":
            while not s.isEmpty():
                op = s.peek()     
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop

                else : break
            s.push(term)
        else:
            output.append(term)

        
    while not s.isEmpty():
        output.append(s.pop)
    return output

infix1 = input()
infix1 = list(infix1)
postfix1=Infix2Postfix(infix1)
print(postfix1)