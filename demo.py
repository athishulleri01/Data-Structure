# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)

# result = factorial(4)
# print(result)

# list1 = ["apple","orange","graphe"]
# list2 = ["banana","apple","lemon"]
# list1 = list1+list2
# list2 = list(set(list1))
# print(list2)

# l1 = [1,2,3,4,5,6]
# l2 = [if x%2==0 for x in l1 else x ]
# print(l2)


even = [x if x % 2 == 0 else 0 for x in range(1, 11)]
odd = [x if x % 2 != 0 else 0 for x in range(1, 11)]

# Filter out the zeros
even = [x for x in even if x != 0]
odd = [x for x in odd if x != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
# ...........................................
# Creating a dictionary of even squares
numbers = [1, 2, 3, 4, 5]
even_squares_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares_dict)



# ///////////////////
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# ///////////////////////
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

