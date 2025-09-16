# iterative method to binary search

l = [1,2,4,6,8]
a = 3

while len(l) != 1:
    if a < l[len(l)//2]:
        l = l[0:len(l)//2]
    else:
        l = l[len(l)//2:]

print(a in l)
        

#recursive method to binary search


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


