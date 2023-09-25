import math
import random
import os

s=[]
carry=0
with open("inputFile_Day1.txt", "r") as file:
    for line in file:
        if line.rstrip()!='':
            carry+=int(line.rstrip())
        else:
            s+=[carry]
            carry=0
s.sort()
print(s[len(s)-1])
print(sum(s[len(s)-3:]))