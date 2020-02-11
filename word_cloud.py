import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as np 
from PIL import Image


text1 = open("iliad.txt", "r").read().lower()
title1 = "The Iliad"

text2 = open("odyssey.txt", "r").read().lower()
title2 = "The Odyssey"

def create_word_cloud(string, title):
   maskArray = np.array(Image.open("cloud.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   clean_title = title.replace(" ", "")
   cloud.to_file("%swordCloud.png" % clean_title)
create_word_cloud(text1, title1)
create_word_cloud(text2, title2)
