#coding:utf-8
import urllib2
import json
import string

page = 1
while True:
    print page
    url = ('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend'
            '&page_limit=20&page_start=' + str((page - 1) * 20))
    print url
    res = urllib2.urlopen(url)
    html = res.read()
    obj = json.loads(html)
    if not(obj['subjects']):
        print all
        break
    else:
        list = obj['subjects']
        filename = '豆瓣热门电影' + string.zfill(page, 3) + '.txt'
        metas = ['id', '标题', '链接', '评分', '海报', '播放源', '新电影']
        line = '\t'.join(metas) + '\n'
        f = open(filename, 'w+')
        f.write(line)
        f.close()
        for index in range(len(list)):
            title = list[index]['title'].encode('utf-8')
            rate = list[index]['rate'].encode('utf-8')
            url = list[index]['url'].encode('utf-8')
            if list[index]['playable']:
                playable = 'playable'
            else:
                playable = 'noplayable'
            cover = list[index]['cover'].encode('utf-8')
            id = list[index]['id'].encode('utf-8')
            if list[index]['is_new']:
                is_new = 'new'
            else:
                is_new = 'nonew'
            metas = [id, title, url, rate, cover, playable, is_new]
            line = '\t'.join(metas) + '\n'
            f = open(filename, 'a')
            f.write(line)
            f.close()
    print 'page %d crawl over.' % (page)
    page += 1
print 'all pages crawl over.'