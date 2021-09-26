from data_gather.api_key import *
import requests


def get_youtube_info(vid_list, file_name):
    vids = ','.join(vid_list)
    print(f'Request videos: {vids}')
    url = f'https://www.googleapis.com/youtube/v3/videos?key={youtube_access_key}&part=snippet&id={vids}'
    resp = requests.get(url)
    with open(f'channel/{file_name}.json', 'wb') as f:
        f.write(resp.content)
    print(f'Save to channel/{file_name}.json')


def get_youtube_channel(channel, file_name):
    print(f'Request channel: {channel}')
    page = 1
    url = f'https://www.googleapis.com/youtube/v3/search?key={youtube_access_key}&part=id&channelId={channel}&order=date&maxResults=50'
    video_ids = []
    resp = requests.get(url)
    for video in resp.json()['items']:
        video_ids.append(video['id']['videoId'])
    get_youtube_info(video_ids, f'{file_name}_info-{page}')
    while 'nextPageToken' in resp.json():
        page += 1
        video_ids = []
        next_page_token = resp.json()['nextPageToken']
        resp = requests.get(url + f'&pageToken={next_page_token}')
        for video in resp.json()['items']:
            if 'id' in video and 'videoId' in video['id']:
                video_ids.append(video['id']['videoId'])
        if video_ids:
            get_youtube_info(video_ids, f'{file_name}_info-{page}')


get_youtube_channel('UCeeFfhMcJa1kjtfZAGskOCA', 'channel_videos')

