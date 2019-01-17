from collections import Counter

def get_similar_count(words, words_by_count):
    max_count = 0
    words_list = []
    #Getting a list of words with the same max count
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

    return final_words

def main():
    #words = ["love", "i", "coding", "coding", "i", "love", "Deep", "learning", "i", "love", "coding"]
    words = ["do", "you", "love", "you", "love", "me", "me", "i", "love", "you", "do"]
    k = 4

    counter = Counter(words)
    words_by_count = counter.most_common()

    #while len(final_words) < k:
    final_words = get_similar_count(words, words_by_count)

    while len(final_words) < k:
        #print the rest of the words
        for word in final_words:
            while word in words:
                words.remove(word)
            for word_count in words_by_count:
                if word == word_count[0]:
                    words_by_count.remove(word_count)
        
        final_words.extend(get_similar_count(words, words_by_count))
        
    print(final_words)

if __name__ == "__main__":
    main()
