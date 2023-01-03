import os
os.system("cls")

def fibo(num):
    if num==0:
        return 1
    if num<0:
        return 0
    val=fibo(num-1)+fibo(num-2)
    return val



term=int(input("Enter the term:"))
print("The value is {}".format(fibo(term)))










# term=int(input("Enter the term:"))

# num_1=0
# num_2=1
# c=0
# i=1
# val=0

# while(i):
#     val=num_1+num_2

#     if c==0:
#         num_1=val
#         c=1
#     else:
#         num_2=val
#         c=0
    
#     if i==term:
#         break
#     else:
#         i+=1

# print(val)
