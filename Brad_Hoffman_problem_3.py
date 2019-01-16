import operator

def main():

    #list of words
    words = ["i", "love", "Deep", "learning", "i", "love", "coding"]
    #pick the k most frequent words from the solution
    k = 2

    word_count = {}

    for index, word in enumerate(words):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=operator.itemgetter(1))
    print(sorted_words)

    list_length = len(sorted_words)
    for i in range(1, k + 1):
        print(sorted_words[list_length - i][0])

if __name__ == "__main__":
    main()
