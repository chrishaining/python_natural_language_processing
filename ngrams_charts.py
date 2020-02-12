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


# plt.bar(range(bigram_length), bigrams_frequencies, color='#b30000')

#create your ax object here
# ax = plt.subplot()
# ax.set_xticks(range(bigram_length))
# ax.set_xticklabels(bigrams_words)
# ax.set_title('Top 10 Bigrams in The Iliad by Frequency')
# ax.set_xlabel('Bigram')
# ax.set_ylabel('Frequency')


# PENTAGRAMS
top_pentagrams = pentagrams_frequency.most_common(5)
pentagrams_length = len(pentagrams_frequency.most_common(5))

pentagrams_words = create_word_list(top_pentagrams)
pentagrams_frequencies = create_frequency_list(top_pentagrams)

bar = plt.bar(range(pentagrams_length), pentagrams_frequencies)
bar[0].set_color('blue')
bar[1].set_color('red')
bar[2].set_color('green')
bar[3].set_color('yellow')
bar[4].set_color('purple')

# plt.show()

# note that the pentagram tick labels are long and unwieldy. So, I have an idea to use the letters A-E, then a legend. First, we need to create an array of tick labels
alias_labels = ["A", "B", "C", "D", "E"]

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(pentagrams_length))
ax.set_xticklabels(alias_labels)
ax.set_title('Top 5 Pentagrams in The Iliad by Frequency')
ax.set_xlabel('Pentagram')
ax.set_ylabel('Frequency')

# for pentagrams_label in pentagrams_labels:
#         label=pentagrams_label
label1 = 'A: {}'.format(pentagrams_words[0])
label2 = 'B: {}'.format(pentagrams_words[1])
label3 = 'C: {}'.format(pentagrams_words[2])
label4 = 'D: {}'.format(pentagrams_words[3])
label5 = 'E: {}'.format(pentagrams_words[4])
labels = [label1, label2, label3, label4, label5]
print(label2)
# plt.legend(labels, title="legend")
# plt.legend(pentagrams_labels, loc=2, title="legend")

plt.savefig('pentagram_bar_chart.png')

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