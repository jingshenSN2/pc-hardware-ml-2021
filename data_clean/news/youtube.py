import json

import pandas as pd

with open('../../data_gather/news/comments/video_info.json', 'rb') as f:
    video_info_json = json.load(f)['items']

video_list = []

for video in video_info_json:
    video_info = {'video_id': video['id'], 'title': video['snippet']['title'], 'published_at': video['snippet']['publishedAt'],
                  'description': video['snippet']['description'], 'tags': ','.join(video['snippet']['tags'])}
    video_list.append(video_info)

video_df = pd.DataFrame(video_list)

print(video_info_json)