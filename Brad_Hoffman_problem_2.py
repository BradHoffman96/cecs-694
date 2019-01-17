
def stack_version(string):
    last = -1
    longest = 0
    stack = []

    for index, p in enumerate(string):
        if p == "(":
            stack.append(index)
        else:
            stack_len = len(stack)
            if stack_len == 0:
                last = index
            else:
                item = stack.pop()
                if stack_len == 0:
                    longest = max(longest, index - last)
                else:
                    longest = max(longest, index - item)

    return longest

def main():
    string = "()())"

    print(stack_version(string))

    longest = [0] * len(string)
    for i in range(1, len(string)):
        if string[i] == ')':
            # Index where matching ( would have to be, if it exists.
            j = i - longest[i-1] - 1
            if j >= 0 and string[j] == '(':
                longest[i] = 1 + i - j + longest[j-1]
    
    print(max(longest))

if __name__ == "__main__":
    main()
