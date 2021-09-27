import datetime
import json
import re
import pandas as pd
video_list = []

for i in range(1, 11):
    with open(f'../../data_gather/news/channel/channel_videos_info-{i}.json', 'rb') as f:
        video_info_json = json.load(f)['items']
    for video in video_info_json:
        snippet = video['snippet']
        published_at = datetime.datetime.strptime(snippet['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()
        video_info = {'video_id': video['id'], 'title': snippet['title'],
                      'published_at': published_at,
                      'description': snippet['description'], 'tags': ','.join(snippet['tags'])}
        video_list.append(video_info)


video_df = pd.DataFrame(video_list)
for idx, row in video_df.iterrows():
    segment = row['description'].split('\n')
    for i, content in enumerate(segment):
        # clean some promotion description
        if str(content).startswith('FOLLOW US ELSEWHERE'):
            segment = segment[:i]
            break
    text = ' '.join(segment)
    text = re.sub(r"[\t\n\r\*\.\@\,\-\/\>\<\=\$\'\|\+\`\(\)]", ' ', text)
    text = re.sub(r"\s+", ' ', text)
    video_df['description'].values[idx] = text

video_df.to_csv('../../data/channel_videos.csv', index=False)

with open('../../data/video_tags.csv', 'w') as f:
    for idx, row in video_df.iterrows():
        f.write(row['video_id'] + ',')
        f.write(row['tags'])
        f.write('\n')
