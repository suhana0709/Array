def maximum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = max(temp, arr[i])
    return temp
def minimum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = min(temp, arr[i])
    return temp

arr = [2, 6, 9, 8, 5, 1, 7, 3]
size = len(arr)

print("Array = ", arr)
print("Maximum number: ", maximum(arr, size))
print("Minimum number: ", minimum(arr, size))