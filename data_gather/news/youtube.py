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


get_youtube_comment('lEwZTNQCxYQ')
get_youtube_comment('0vz-pTclTiI')
get_youtube_comment('qlKubWocKkg')
get_youtube_comment('zF2KF-SVIXc')
get_youtube_comment('u1Qn_KHM1GY')
get_youtube_comment('3LfjmI1krJs')
get_youtube_comment('718PVQ3Oty4')
get_youtube_comment('nl1tZx9knzA')
get_youtube_comment('aSlI5dcpNE4')
get_youtube_comment('HZigkcTxRo0')
get_youtube_comment('XOeBnGirfKc')
get_youtube_comment('t4TbEqKmdPc')
get_youtube_comment('YqR-klyztC0')
get_youtube_comment('2zIKPKkgzm4')
get_youtube_comment('l1B-xsSeoCM')
get_youtube_comment('QUv6h0eFCjg')
get_youtube_comment('BjRcNFgNo-g')
get_youtube_comment('u2UGqLvq0_k')
get_youtube_comment('TI_-1dZJrk4')
get_youtube_comment('hnOmghy5B7Y')
get_youtube_comment('egop1jwc_Xs')
get_youtube_comment('pZo0r45xxC0')
