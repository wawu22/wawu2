from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

Wolf Warrior 2 is a 2017 Chinese action film directed by Wu Jing, who also starred in the lead role. The film co-stars Celina Jade, Frank Grillo, Hans Zhang, and Wu Gang. The film is a sequel to the 2015 s Wolf Warrior. The film tells a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world. In this sequel, he finds himself in an African country protecting medical aid workers from local rebels and vicious arms dealers. received general praise for its patriotic plot, special effects, action sequences and the performances of the cast. It was a massive commercial success and has become the highest-grossing Chinese film ever released. The film broke numerous box office records, including the biggest single-day gross for a Chinese film as well as the fastest film to cross RMB 2 billion, 3 billion, 4 billion and 5 billion box office marks.
Wolf Warrior 2 is a 2017 Chinese action film directed by Wu Jing, who also starred in the lead role. The film co-stars Celina Jade, Frank Grillo, Hans Zhang, and Wu Gang. The film is a sequel to the 2015s Wolf Warrior. The film tells a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world. In this sequel, he finds himself in an African country protecting medical aid workers from local rebels and vicious arms dealers. received general praise for its patriotic plot, special effects, action sequences and the performances of the cast. It was a massive commercial success and has become the highest-grossing Chinese film ever released. The film broke numerous box office records, including the biggest single-day gross for a Chinese film  well the fastest film to cross RMB  billion, billion, 4 billion and 5 billion box office marks.


cloud = WordCloud(background_color="white",).generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()
