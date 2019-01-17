#**************************#
#* Brad Hoffman  *         #
#* CECS 694-02   *         # 
#* Assignment 01 *         # 
#************************* #

def main():
    string = "())"

    stack = [-1]
    longest = 0

    for index, p in enumerate(string):
        if p == "(":
            stack.append(index)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(index)
            else:
                longest = max(longest, index - stack[len(stack) - 1])

    print(longest)

if __name__ == "__main__":
    main()
