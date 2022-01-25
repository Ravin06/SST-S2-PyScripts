'''
text = "MONKE"
for ch in text : 
	print(ch)

for x in range(n + 1):
    print(x)



import time

n = int(input("n: "))

for x in range(n, 0, -1) :
    print(x)
    time.sleep(1)


a = 0
while a < 10000000:
	print(a)
	a = a + 1



from __future__ import print_function

word = 'https://youtu.be/dQw4w9WgXcQ'

for i in range(len(word)):
    for j in range(len(word)):
        if i == j:
            print(word[i], end="")
        else:
            print(' ', end="")
    print()

'''

N = int(input("Enter number : "))

for c in range(N) :
    print("*", end="")
    print()

'''
txt = input(" What do you want to type diagonally: ")
s = 0
for ch in txt:
    print(" " * s, end="")
    print(ch)
    s += 1

Total = 0
N = 0
while N >= 0:
    Total += N
    N = int(input("N: "))
print("Total:" , Total)


total, evenTotal, evenCount = 0
large, small = 0, 999

while True:
    n = int(input("N: "))
    if n >= 0:

        if n > large:
            large = n
        if n < small:
            small = n
    if n%2 == 0:
        evenTotal += n
        evenCount += 1
            

        total += n
    else:
        break

nRange = large-small
evenMean = evenTotal / evenCount

print("Total: " , total)
print("large", large, " | small", small)
print("Range:", nRange)

'''




