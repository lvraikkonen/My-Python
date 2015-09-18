# wordcloud usage
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


d = path.dirname(__file__)

# read whole text
text = open(path.join(d, 'alice.txt')).read()

# read the mask image
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

wc = WordCloud(background_color="white", max_words=2000,
               mask=alice_mask, stopwords=STOPWORDS.add("said"))
wc.generate(text)

# store to file
wc.to_file(path.join(d, 'alice.png'))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(alice_mask)
plt.axis("off")
plt.show()
