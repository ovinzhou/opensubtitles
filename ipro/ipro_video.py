import requests
import csv

data = [
    ['name', 'description', 'director', 'actors', 'year', 'cover', 'original_name', 'url', 'genres_ids'],
]

# 获取
url = "http://stalker.suptv.net/stalker_portal/api/v2/video-categories/SPECIAL-RAMADAN/video"

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer 40906.cf115a881152a89ca62fe47d21bec6a2',
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; GT-I9500 Build/KOT49H)',
    'Host': 'stalker.suptv.net',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

response = requests.get(url, headers=headers)
content = response.text
print(response.text)

# with open('ipro_video.json', 'w') as f:
#     f.write(response.text)

# 存储
content = eval(content)
for info in content['results']:
    logo = info['cover']
    if logo == '':
        logo = ''
    else:
        logo = 'http://portal.suptv.me' + logo.replace('\\', '')

    genres = ''
    for g in info['genres_ids']:
        genres += g + ','

    url = info['url'].replace('\\', '')
    info_list = [info['name'], info['description'], info['director'], info['actors'], info['year'], logo,
                 info['original_name'], url, genres[:-1]]
    data.append(info_list)

with open('speclal_ramadan.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
