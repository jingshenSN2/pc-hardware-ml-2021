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


def get_youtube_info(vid_list, file_name):
    vids = ','.join(vid_list)
    print(f'Request videos: {vids}')
    url = f'https://www.googleapis.com/youtube/v3/videos?key={youtube_access_key}&part=snippet&id={vids}'
    resp = requests.get(url)
    with open(f'comments/{file_name}.json', 'wb') as f:
        f.write(resp.content)
    print(f'Save to comments/{file_name}.json')


video_list = ['lEwZTNQCxYQ', '0vz-pTclTiI', 'qlKubWocKkg', 'zF2KF-SVIXc', 'u1Qn_KHM1GY', '3LfjmI1krJs', '718PVQ3Oty4',
              'nl1tZx9knzA', 'aSlI5dcpNE4', 'HZigkcTxRo0', 'XOeBnGirfKc', 't4TbEqKmdPc', 'YqR-klyztC0', '2zIKPKkgzm4',
              'l1B-xsSeoCM', 'QUv6h0eFCjg', 'BjRcNFgNo-g', 'u2UGqLvq0_k', 'TI_-1dZJrk4', 'hnOmghy5B7Y', 'egop1jwc_Xs',
              'pZo0r45xxC0']

# get_youtube_info(video_list, 'video_info')
# for vid in video_list:
#     get_youtube_comment(vid)

def get_youtube_channel(channel, file_name):
    print(f'Request channel: {channel}')
    video_ids = []
    page = 1
    url = f'https://www.googleapis.com/youtube/v3/search?key={youtube_access_key}&part=id&channelId={channel}&order=date&maxResults=50'
    resp = requests.get(url)
    for video in resp.json()['items']:
        video_ids.append(video['id']['videoId'])
    with open(f'channels/{file_name}-{page}.json', 'wb') as f:
        f.write(resp.content)
        print(f'Save to channels/{file_name}-{page}.json')
    while 'nextPageToken' in resp.json():
        page += 1
        next_page_token = resp.json()['nextPageToken']
        resp = requests.get(url + f'&pageToken={next_page_token}')
        for video in resp.json()['items']:
            if 'id' in video and 'videoId' in video['id']:
                video_ids.append(video['id']['videoId'])
        with open(f'channels/{file_name}-{page}.json', 'wb') as f:
            f.write(resp.content)
        print(f'Save to channels/{file_name}-{page}.json')
    return video_ids


video_ids = get_youtube_channel('UCeeFfhMcJa1kjtfZAGskOCA', 'channel_videos_id')
get_youtube_info(video_ids, 'channel_videos_info')

