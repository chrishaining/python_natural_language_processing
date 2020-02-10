# Python Natural Language Processing 

This is a collection of tools for analysing language.

My initial learning has come from the Codecademy course on [Natural Language Processing](https://www.codecademy.com/learn/natural-language-processing)

---

## Setup and Packages 
The programs use:
* Python 3
* pip3 for installing packages
* nltk
* re
* collections

---

## Source text
The programs analyse text of The Iliad, taken from [Project Gutenberg](http://www.gutenberg.org/ebooks/6130).

---

## __parse.py__ 
This program takes a text and identifies the grammatical type of each word. 

---

## __word_count.py__ 
This program takes a text and for each word counts the number of times that word occurs. 

---

## __top_ten_ngrams.py__ 
This program takes a text and displays the top ten two-word, three-word and five-word phrases by frequency.

---

## Problems and Workarounds
There were problems trying to use nltk. I had to open the Python shell (in terminal, type `python` then hit `enter`), then had to download various models. See [stack overflow advice, answer 11](https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed/59530679#59530679)