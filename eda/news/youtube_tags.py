from collections import Counter

from matplotlib import pyplot as plt
from wordcloud import WordCloud


tags = []
with open('../../data/video_tags.csv', 'r') as f:
    lines = f.readlines()
for line in lines:
    segment = line.split(',')
    tags.extend(segment[1:])
counter = Counter(tags)

wc = WordCloud(width=1600, height=800, max_words=50, background_color='white').generate_from_frequencies(counter)

plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")
plt.savefig('tags_wordcloud.png', bbox_inches='tight')
plt.close()

counter.pop('Linus')
counter.pop('LinusTechTips')
counter.pop('Riley Murdock')
counter.pop('netlinked')
counter.pop('Techlinked')
counter.pop('tech news')
counter.pop('tech')
counter.pop('news')

wc = WordCloud(width=1600, height=800, max_words=50, background_color='white').generate_from_frequencies(counter)

plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")
plt.savefig('tags_wordcloud_pure.png', bbox_inches='tight')
plt.close()