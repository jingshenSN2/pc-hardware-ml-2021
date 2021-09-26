import datetime
import os
import json
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

walk = os.walk('../../data_gather/news/comments')

file_list = []

for path, dir_list, filename_list in walk:
    for filename in filename_list:
        if filename.startswith('channel') or filename.startswith('video'):
            continue
        file_list.append(os.path.join(path, filename))

comment_list = []

# convert json to csv
for file in file_list:
    print(f'Parsing {file}...')
    with open(file, 'rb') as f:
        comment_json = json.load(f)['items']
        for comment in comment_json:
            snippet = comment['snippet']['topLevelComment']['snippet']
            published_at = datetime.datetime.strptime(snippet['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()
            published_week = published_at - datetime.timedelta(days=published_at.weekday())
            text = snippet['textOriginal'].replace('\n', ' ').encode("ascii", "ignore").decode()
            if len(text) < 20 or len(text.split(' ')) < 5:
                # we only use comments that have over 20 characters and 5 words
                continue
            comment_dict = {'video_id': snippet['videoId'], 'text': text,
                            'like': snippet['likeCount'], 'published_at': published_at,
                            'published_week': published_week}
            comment_list.append(comment_dict)

comment_df = pd.DataFrame(comment_list)
comment_df.to_csv('../../data/comments.csv', index=False)

comment_df['published_at'] = pd.to_datetime(comment_df['published_at'])
comment_df_by_date = comment_df.set_index('published_at')

# sample to be labeled manually
sample = comment_df_by_date.loc['2021-09-14'].reset_index()['text'].to_frame()
sample.insert(0, 'LABEL', value=[0] * len(sample))
for idx, row in sample.iterrows():
    text = row['text'].lower()
    for keyword in ['gpu', 'nvidia', 'amd', 'graphic', '2060', '12g', 'rtx', '00xt', '3050', '3060', '3070', '3080', 'gtx', 'crpyto', 'vram', 'litecoin', '1080']:
        if keyword in text:
            sample['LABEL'].values[idx] = 1
            break

sample.to_csv('../../data_clean/news/comment_sample_prelabeled.csv', index=False)
