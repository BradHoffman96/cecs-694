from collections import Counter

def main():
    words = ["love", "i", "coding", "coding", "i", "love", "Deep", "learning", "i", "love", "coding"]
    k = 4

    counter = Counter(words)
    words_by_count = counter.most_common()

    max_count = 0
    words_list = []
    for i in range(0, len(words_by_count)):
        current_word = words_by_count[i][0]
        current_count = words_by_count[i][1]

        if i == 0:
            max_count = current_count
            words_list.append(current_word)
        elif max_count == current_count:
            words_list.append(current_word)
        else:
            break

    indexes = []
    for item in words_list:
        indexes.append(words.index(item))

    sorted_indexes = sorted(indexes)

    final_words = []
    for i in range(0, len(indexes)):
        index = sorted_indexes[i]
        final_words.append(words[index]) 

    if len(final_words) < k:
        #print the rest of the words
        remainder = k - len(final_words)
        for i in range(len(final_words), k):
            final_words.append(words_by_count[i][0])
        
    print(final_words)

if __name__ == "__main__":
    main()
