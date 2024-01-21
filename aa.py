# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)


# f = factorial(3)
# print(f)


def primeOrNot(num):
    x = num
    if num<2:
        print("not an prime number") 
    else:
        
        for i in range(2,num):
            if  num % i ==0:
                print("not an prime number")
                return
            print("prime number")
            return
            
primeOrNot(7)