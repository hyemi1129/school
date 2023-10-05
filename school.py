""" 
a = input()
a = int(a)

sum=0
for i in range(1, a+1):s
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
