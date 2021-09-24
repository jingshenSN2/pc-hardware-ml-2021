import json

import pandas as pd
video_list = []

for i in range(1, 11):
    with open(f'../../data_gather/news/comments/channel_videos_info-{i}.json', 'rb') as f:
        video_info_json = json.load(f)['items']
    for video in video_info_json:
        video_info = {'video_id': video['id'], 'title': video['snippet']['title'],
                      'published_at': video['snippet']['publishedAt'],
                      'description': video['snippet']['description'], 'tags': ','.join(video['snippet']['tags'])}
        video_list.append(video_info)


video_df = pd.DataFrame(video_list)
for idx, row in video_df.iterrows():
    desc = row['description']
    segment = desc.split('\n')
    for idx, content in enumerate(segment):
        if str(content).startswith('FOLLOW US ELSEWHERE'):
            segment = segment[:idx]
            break
    row['description'] = '\n'.join(segment)

video_df.to_csv('../../data/channel_videos.csv', index=False)
