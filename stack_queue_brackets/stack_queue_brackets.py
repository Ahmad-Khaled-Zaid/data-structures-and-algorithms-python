from Stack_and_Queue.stack_and_queue import Stack


def validate_brackets(shape):
    shapes = ["{}", "[]", "()"]
    stack = Stack()
    for bracket in shape:
        if bracket == "{" or bracket == "(" or bracket == "[":
            stack.push(bracket)
        elif bracket == "}" or bracket == ")" or bracket == "]":
            if stack.top is None:
                return False
            elif (stack.top.value + bracket) in shapes:
                stack.pop()
            else:
                return False
    return True if stack.is_empty() else False


if __name__ == "__main__":
    print(validate_brackets("{}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("()[[Extra Characters]]"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("{}{Code}[Fellows](())"))
    print(validate_brackets("[({}]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("{([])}"))

