import sys

lst = []

for i in range(9):
    n = int(sys.stdin.readline())
    lst.append(n)

print(max(lst), lst.index(max(lst))+1, sep='\n')