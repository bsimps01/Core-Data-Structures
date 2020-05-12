def reverse_numbers(combo):
    stack = []

    for num in combo:
        stack.append(num)

    reverse_numbers = ""

    while len(stack) != 0:
        reverse_numbers += stack.pop(-1)
    return reverse_numbers

print(reverse_numbers("3479"))
