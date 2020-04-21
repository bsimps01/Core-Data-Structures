def check_brackets(expression):
    #use a stack
    bracket_stack = [] #push and pop from the end
    valid_brackets = {"}":"{", "]":"[",")":"("}

    #loop through my expression
    #if I find an open bracket I push to the stack
    #if I find a closed I compare to teh top of the stack
    #if mismatch return false
    #otherwise if match pop from stack and repeat
    for character in expression:
        if character in valid_brackets.values():
            bracket_stack.append(character)
        if character in valid_brackets.keys():
            if len(bracket_stack) != 0:
                top = bracket_stack[-1]
                matchingopen = valid_brackets[character]
                if top == matchingopen:
                    bracket_stack.pop(-1)
                else:
                    return False
            else:
                return False
    #if stack empty at the end return true
    #else return false
    if len(bracket_stack) == 0:
        return True
    else:
        return False
print(check_brackets("([jess], {hello})"))
print(check_brackets("([[jess], "))