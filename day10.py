# Your code here
import sys
A,B,K = [int(i) for i in input().split()]
count = 0
while A < B:
    A *= K
    count += 1
print(count)