""" a = int(input())

for i in range(a+1):
    print(i)
 """

""" a = int(input())
b = 0
for i in range(a+1):
    if i%2==0:
        b+=i
print(b) """

""" a = int(input())
b = 0

for i in range(a):
    b+=i
    
    if b>=a:
        print(i)
        break """

""" a, b = map(int, input().split())

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j) """


""" r, g, b = map(int, input().split())

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)

print(r*g*b) """

a, b, c = map(int, input().split())

for i in range(2, c+1):
    a+=b

print(a)

