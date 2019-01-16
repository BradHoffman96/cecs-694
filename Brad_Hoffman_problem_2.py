
def main():
    string = "()())"
    solution = [-1]
    longest = 0

    for index, p in enumerate(string):
        if p == ")"and len(solution) != 0:
            pop_index = solution.pop()
            if index - pop_index > longest:
                longest = index - pop_index
        else:
            solution.append(index)

    print(longest)

if __name__ == "__main__":
    main()
