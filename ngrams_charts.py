from top_ten_ngrams import *
import matplotlib.pyplot as plt

top_bigrams = bigrams_frequency.most_common(10)

bigram_length = len(bigrams_frequency.most_common(10))

def create_word_list(ngram_list):
    words = []
    for item in ngram_list:
        words.append(item[0])
    return words

def create_frequency_list(ngram_list):
    frequencies = []
    for item in ngram_list:
        frequencies.append(item[1])
    return frequencies

bigrams_words = create_word_list(top_bigrams)
# print(bigrams_words)
# print(bigrams)

bigrams_frequencies = create_frequency_list(top_bigrams)
# print(bigrams_frequencies)

# print("Top bigrams: {}".format(top_bigrams))
# print(bigram_length)


plt.bar(range(bigram_length), bigrams_frequencies)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(bigram_length))
ax.set_xticklabels(bigrams_words)
ax.set_title('Top 10 Bigrams in The Iliad by Frequency')
ax.set_xlabel('Bigram')
ax.set_ylabel('Frequency')

plt.show()


# practise with a different data set. It still isn't working: 
# countries = ["Italy", "Brazil", "Spain", "Germany", "France", "England", "Uruguay", "Argentina"]
# victories = [4, 5, 1, 4, 2, 1, 2, 2]
# length = len(countries)
# plt.bar(range(length), victories)
# ax = plt.subplot()
# ax.set_xticks(range(length))
# ax.set_xticklabels(countries)
# plt.show()

# drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
# sales =  [91, 76, 56, 66, 52, 27]

# plt.bar(range(len(drinks)), sales)

# #create your ax object here
# ax = plt.subplot()
# length = len(drinks)
# ax.set_xticks(range(length))
# ax.set_xticklabels(drinks)
# plt.show()