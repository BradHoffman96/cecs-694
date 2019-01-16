import operator

def check_index(words_list, current_word, previous_word):
    current_index = words_list.index(current_word)
    previous_index = words_list.index(previous_word)

    print(current_index, previous_index)

    if current_index < previous_index:
        return (current_index, previous_index)
    else:
        return (previous_index, current_index)

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
    previous_word = ""
    previous_count = 0
    top_k_words = []
    for i in range(1, k + 1):
        current_word = sorted_words[list_length - 1][0] 
        current_count = sorted_words[list_length - 1][1] 
        
        if i == 1:
            previous_word = current_word
            previous_count = current_count
        elif previous_count == current_count:
            #Check the index and add the correct one to the final array
            first_word, second_word = check_index(words, current_word, previous_word)
            continue

        top_k_words.append(current_word)

        previous_word = 

if __name__ == "__main__":
    main()
