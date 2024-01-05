def Fibanacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + Fibanacci(num-1)

result = Fibanacci(5)
print(result)