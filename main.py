import re
import numpy as np
import random
from PIL import Image

# Load tokenize
tokenize = open('ckip/tokenize.txt', 'r',encoding= 'UTF-8-sig').read()

# Clean up tokenize write into new file
f = open("wordlist.txt", "w+")
for n in re.findall(r'[\u4e00-\u9fff]+', tokenize):
    f.write("%s " % n)

# Load clean tokenize
wordlist = open('wordlist.txt', 'r',encoding= 'UTF-8-sig').read()

# Select png for word cloud
icon_path = 'chinese_cloud2.png'
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

from palettable.colorbrewer.sequential import Blues_9 # choose the color set you like
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Blues_9.colors[random.randint(0,8)]) # we got 9 colors, so we generate random number from 0 to 8

font_path = 'NotoSansCJKtc-Bold.otf'

from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(font_path=font_path, background_color="#ff5c5c", max_words=2000, mask=mask, max_font_size=300, random_state=1)
wc.generate_from_text(wordlist)
wc.recolor(color_func=color_func, random_state=2)

# Save as png
output_path = 'wordcloud.png'
wc.to_file(output_path)
# Display the word cloud
plt.rcParams["figure.figsize"] = (25,25)
plt.imshow(wc)
plt.axis("off")
plt.show()