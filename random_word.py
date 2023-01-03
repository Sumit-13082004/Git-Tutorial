import os
import random

word=[]
for x in range(10):
    li=[chr(random.randint(97,122)) for a in range(random.randint(1,5))]
    li=''.join(li)
    word.append(li)
print(word)
input()
os.system('cls')
    
        