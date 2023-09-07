def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def sum_helper(arr,number):
    first = 0
    second = len(arr)-1
    return can_sum(arr,number,first,second)
def can_sum(arr,number,first,second):
    arr = merge_sort(arr)
    result = arr[first] + arr[second]
    if result == number:
        print("Yes, ",end=(""))
        print(arr[first],end=(" + "))
        print(arr[second],end=(" = "))
        print(number)
    elif second <= first:
        print("No")
    elif result < number:
        return can_sum(arr,number,first+1,second)
    else:
        return can_sum(arr,number,first,second-1)
        
            
            



lst = [5,10,15,20,25]
num = int(input())
sum_helper(lst,num)


