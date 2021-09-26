from data_gather.api_key import *
import requests
import os


def _get_youtube_comment(file_name, video_id, next_page_token=''):
    url = f'https://www.googleapis.com/youtube/v3/commentThreads?key={youtube_access_key}&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=100'
    if next_page_token != '':
        url += f'&pageToken={next_page_token}'
    print(f'Request video: {video_id} with pageToken: {next_page_token}')
    resp = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(resp.content)
    print(f'Save to {file_name}')
    return resp.json()['nextPageToken'] if 'nextPageToken' in resp.json() else ''


def get_youtube_comment(video_id):
    page = 1
    os.makedirs(os.getcwd() + f'\\comments\\{video_id}')
    next_token = _get_youtube_comment(f'comments/{video_id}/{page}.json', video_id, '')
    while next_token != '':
        page += 1
        next_token = _get_youtube_comment(f'comments/{video_id}/{page}.json', video_id, next_token)


gpu_related_videos = []
with open('../../data/video_tags.csv', 'r') as f:
    lines = f.readlines()
for line in lines:
    segment = line.split(',')
    for keyword in ['gpu', 'nvidia', 'amd']:
        if keyword in line.lower():
            gpu_related_videos.append(segment[0])
            break


for vid in gpu_related_videos:
    get_youtube_comment(vid)



