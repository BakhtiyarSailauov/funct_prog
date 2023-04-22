#exes 1
value = input("Введите значение для проверки: ")

result = sorted(set(value))
print(result)

#exes 2
item_list = [1, 2, 3, 4, 5, 6]
print (all(item > 2 for item in item_list))
print ([item > 2 for item in item_list])

item_list = [1, 2, 3, 4, 5, 6]
print (any(item > 2 for item in item_list))
print ([item > 2 for item in item_list])

#exes 3
def transposed(matrix):
    return [[*col] for col in zip(*matrix)]


def rot90(matrix):
    return list(map(reversed, transposed(matrix)))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = rot90(matrix)

for item in result:
    print("\n")
    for item2 in item:
        print(item2, end=" ")

#exes 4
def knapsack(v, w, n, W):

    if n < 0 or W == 0:
        return 0

    include = v[n] + knapsack(v, w, n - 1, W - w[n])

    exclude = knapsack(v, w, n - 1, W)

    return max(include, exclude)


v = [20, 5, 10, 40, 15, 25]
print("\n")
for item in range(len(v)):
    print(v[item], end=" ")

w = [1, 2, 3, 8, 7, 4]
print("\n")

for item in enumerate(w):
    print(item)

W = 10

print('Knapsack value is', knapsack(v, w, len(v) - 1, W))

#exes 5
import numpy as np

def matrix_operat(arr1, arr2, operation):
    if operation == "+":
        return map(add_matrix, zip(arr1, arr2))
    elif operation == "-":
        temp = arr1 - arr2
        return temp
    elif operation == "*":
        temp = arr1.dot(arr2)
        return temp

def add_matrix(value):
    return value[0]+value[1]

arr1 = np.array([[3,3,3],[2,5,5]])
arr2 = np.array([[2,4,2],[1,3,8]])

for item in matrix_operat(arr1=arr1, arr2=arr2, operation="+"):
    print(item)