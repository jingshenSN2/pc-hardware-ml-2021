import datetime
import os
import json
import re
import string

import pandas as pd

walk = os.walk('../../data_gather/news/comments')

file_list = []

for path, dir_list, filename_list in walk:
    for filename in filename_list:
        if filename.startswith('channel') or filename.startswith('video'):
            continue
        file_list.append(os.path.join(path, filename))

comment_list = []

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer  # module for tokenizing strings

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
stopwords_english = stopwords.words('english')
stemmer = PorterStemmer()
extra_stopwords = {'linus', 'riley', 'anthony', 'techlinked'}

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
            text = re.sub(r"[\t\n\r\*\@\,\-\/\>\<\=\$\|\+\`\(\)\"\!\?\_]", ' ', text)
            text = re.sub(r"\s+", ' ', text)
            text = re.sub(r"\.+", '.', text)
            token = tokenizer.tokenize(text)
            cleaned = []
            for word in token:
                if word not in extra_stopwords and word not in stopwords_english and word not in string.punctuation:
                    cleaned.append(stemmer.stem(word))
            comment_dict = {'video_id': snippet['videoId'], 'text': ' '.join(cleaned),
                            'like': snippet['likeCount'], 'published_at': published_at,
                            'published_week': published_week}
            comment_list.append(comment_dict)

comment_df = pd.DataFrame(comment_list)
comment_df.to_csv('../../data/comments.csv', index=False)

# sample to be labeled manually
sample = comment_df['text'].sample(n=2000, random_state=501).reset_index(drop=True).to_frame()
sample.insert(0, 'LABEL', value=[0] * len(sample))
for idx, row in sample.iterrows():
    text = row['text'].lower()
    for keyword in ['gpu', 'nvidia', 'amd', 'graphic', 'card', 'rtx', 'gtx']:
        if keyword in text:
            sample['LABEL'].values[idx] = 1
            break
    for keyword in ['cpu', 'processor', 'ryzen', 'intel', 'core', 'i7', 'i9']:
        if keyword in text:
            if sample['LABEL'].values[idx] == 0:
                sample['LABEL'].values[idx] = 2
            else:
                sample['LABEL'].values[idx] = -1
            break
    for keyword in ['iphone', 'android', 'apple', 'xiaomi', 'huawei', 'samsung']:
        if keyword in text:
            if sample['LABEL'].values[idx] == 0:
                sample['LABEL'].values[idx] = 3
            else:
                sample['LABEL'].values[idx] = -1
            break
    for keyword in ['google', 'facebook', 'microsoft', 'amazon', 'twitter']:
        if keyword in text:
            if sample['LABEL'].values[idx] == 0:
                sample['LABEL'].values[idx] = 4
            else:
                sample['LABEL'].values[idx] = -1
            break

sample.to_csv('../../data_clean/news/comment_sample_prelabeled.csv', index=False)
