import math
 
 
def fact(num):
        if num == 1:
            return 1
        else:
            return num * fact(num-1)
            
def square(num):
        return num ** 0.5
    
def lognum(num):
        return math.log(num)

while True:
        usernum = input("What would you like to caculate ?\n 1. Square root \n 2. Log \n 3. Factorial \n >>>>>>> ")
 
        if usernum == '1':
            num = (int (input("enter number to sqrt ")))
            print(square(num))
        if usernum == '2':
            num = (int (input("enter number to log ")))
            print(lognum(num))
        if usernum == '3':
            num = (int (input("enter number to factorise ")))
            print(fact(num))
        if usernum == "exit":
            break
