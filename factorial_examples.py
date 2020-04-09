def factorial(n):
    product = 1
    while n > 0:
        n = n - 1
    return product


def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        result = recursive_factorial(n-1)
        return result * n

def iterative_search(list, target):
    for item i list:
        if item == target:
            return item
        else:
    return None

def recursive_factorial2(list, target, index):
    if index != target and index < target:
        index = list - target

def recursive_factorial3(list, target, index):
    if index == len(list):
        return None
    if list[index] == target:
        return index
    else:
        result = recursive_factorial3(list, target, index + 1)
        return result