import pandas as pd
from matplotlib import pyplot as plt, animation
from wordcloud import WordCloud, STOPWORDS

comments_df = pd.read_csv('../../data/comments_labeled.csv')
gpu_related_df = comments_df[comments_df['LABEL'] == 1]
gpu_related_df['published_at'] = pd.to_datetime(gpu_related_df['published_at'])
gpu_related_df = gpu_related_df.set_index('published_at')

year_month_start = []
year_month_end = []
for y in ['2019', '2020']:
    for m in range(4):
        year_month_start.append(f'{y}-{m+1}')
        year_month_end.append(f'{y}-{m+4}')

for m in range(3):
    year_month_start.append(f'2021-{m+1}')
    year_month_end.append(f'2021-{m+4}')

ym_comments = {}

for ym_s, ym_e in zip(year_month_start, year_month_end):
    ym_comments[ym_s] = gpu_related_df.loc[ym_s:ym_e].reset_index()['text']
    # print(len(ym_comments[ym]))

ym_comment_texts = {}
for ym in ym_comments:
    text = ''
    for comment in ym_comments[ym]:
        text += comment.lower()
    ym_comment_texts[ym] = text

# extra_stopwords = ['nvidia', 'amd', 'gpu', 'gpus', 'card', 'cards', 'graphic', 'will']
# STOPWORDS.update(extra_stopwords)

wordcloud_list = []

for ym in ym_comment_texts:
    max_words = 20
    wc = WordCloud(width=1600, height=800, stopwords=STOPWORDS, max_words=max_words, background_color='white', include_numbers=True).generate_from_text(ym_comment_texts[ym])
    wordcloud_list.append((ym, wc))


def update_wordcloud(data):
    ym, wc = data
    plt.cla()
    plt.imshow(wc)
    plt.axis("off")
    plt.title(f'Word cloud of comments from {ym}', fontsize=32)
    plt.tight_layout()


def update_barplot(data):
    ym, wc = data
    plt.cla()
    plt.barh(range(max_words), [wc.words_[w] for w in wc.words_][::-1])
    plt.yticks([x for x in range(max_words)], list(wc.words_.keys())[::-1], fontsize=32)
    plt.xlabel('Frequency', fontsize=32)
    plt.title(f'Top {max_words} words in comments from {ym}', fontsize=32)
    plt.tight_layout()


fig = plt.figure(figsize=(20, 10))
ani = animation.FuncAnimation(fig, update_wordcloud, frames=wordcloud_list, interval=3000)
ani.save('comments_wordcloud.gif', writer='pillow')

fig = plt.figure(figsize=(20, 10))
ani = animation.FuncAnimation(fig, update_barplot, frames=wordcloud_list, interval=3000)
ani.save('comments_barplot.gif', writer='pillow')
