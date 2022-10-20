import random

randLengthA = random.randint(0, 51)
randLengthB = random.randint(0, 51)

a = []
b = []
c = []

for x in range(randLengthA):
    a.append(random.randint(0, 100))

for y in range(randLengthB):
    b.append(random.randint(0, 100))

a = sorted(a)
b = sorted(b)

print("A Length:", randLengthA)
print("B Length:", randLengthB)

print("A:", a)
print("B:", b)

while len(a) != len(b):
    if len(a) > len(b):
        b.append(" ")
    elif len(a) < len(b):
        a.append(" ")

for i in a:
    if i in b and i not in c:
        c.append(i)

print("C:", c)
