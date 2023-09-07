def search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

def binary_search_recursive(arr, target, low, high):
    if low > high:
        print("not found")
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        print("Found")
        return 1
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


lst = [1,2,3,4,5,6,7,8,9,10]
find = search(lst,10)