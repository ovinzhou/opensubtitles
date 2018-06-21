# import requests
import json
import csv

data = [
    ['name', 'genre_id', 'logo', 'url'],
]

# 获取
# url = "http://stalker.suptv.net/stalker_portal/api/v2/tv-channels"
# headers = {
#     'Accept': 'application/json',
#     'authorization': 'Bearer 40906.cf115a881152a89ca62fe47d21bec6a2',
#     'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; GT-I9500 Build/KOT49H)',
#     'Host': 'stalker.suptv.net',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip',
# }
#
# response = requests.get(url, headers=headers)
# print(response.text)
#
# with open('ipro_tv.json', 'w') as f:
#     f.write(response.text)

# 存储
with open('ipro_tv.json', 'r') as f:
    content = f.read()

content = eval(content)
for info in content['results']:
    logo = info['logo']
    if logo == '':
        logo = ''
    else:
        logo = 'http://portal.suptv.me' + info['logo'].replace('\\', '')
    url = info['url'].replace('\\', '')
    info_list = [info['name'], info['genre_id'], logo, url]
    data.append(info_list)

with open('iprotv_example.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
