from threading import Thread
import requests
from lxml import etree

base_url = 'https://hr.tencent.com/position.php?keywords=&tid=0&start=%d#a'
headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
}


def do_somthing_using(url):
    content = requests.get(url, headers=headers)
    an(content.text)


def an(content):
    xdata = etree.HTML(content)
    name_list = xdata.xpath('//*[@id="position"]/div[1]/table//tr/td[1]/a/text()')
    for named in name_list:
        print(named)


# 这个是工作进程，负责不断从队列取数据并处理
def working(u):

    url = base_url % u
    print(url)
    do_somthing_using(url)


thread_list = []
for u in range(0, 3820, 10):
    t = Thread(target=working, args=(u, ))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()
