def reverse_str(my_string):
    my_stack = []

    for character in my_string:
        my_stack.append(character)

    reverse_str = ""

    while len(my_stack) != 0:
        reverse_str += my_stack.pop(-1)
    return reverse_str

print(reverse_str("abc"))
