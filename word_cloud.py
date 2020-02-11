import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as np 
from PIL import Image


text1 = open("iliad.txt", "r").read().lower()
title1 = "The Iliad"

text2 = open("odyssey.txt", "r").read().lower()
title2 = "The Odyssey"

text3 = "ten, ten, ten, ten, ten, ten, ten, ten, ten, ten, nine, nine, nine, nine, nine, nine, nine, nine, nine, eight, eight, eight, eight, eight, eight, eight, eight, seven, seven, seven, seven, seven, seven, seven, six, six, six, six, six, six, five, five, five, five, five, four, four, four, four, three, three, three, two, two, one"
title3 = "Numbers"

def create_word_cloud(string, title):
   maskArray = np.array(Image.open("cloud.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   clean_title = title.replace(" ", "")
   cloud.to_file("%swordCloud.png" % clean_title)
create_word_cloud(text1, title1)
create_word_cloud(text2, title2)
create_word_cloud(text3, title3)

