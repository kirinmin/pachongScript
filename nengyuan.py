from ast import Num
from math import floor
import re
import requests
import time
import sqlite3
from lxml import etree

url = "http://search.sasac.gov.cn:8080/searchweb/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Referer": "http://search.sasac.gov.cn:8080/searchweb/search_gzw.jsp",
    "Host": "search.sasac.gov.cn:8080",
    "Origin": "http://search.sasac.gov.cn:8080",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1"
}

if __name__ == "__main__":
    con = sqlite3.connect("news_data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, title TEXT, publish TEXT, url TEXT)")

    datas = {
        "fullText": "能源",
        "pageSize": 10,
        "pageNow": 1,
        "sortType": 0,
        "searchType": 0,
        "cateId": "",
        "titleFoldBegin": 0,
        "titleFoldPage": 0,
        "highlighter": 2,
        "urls": "",
        "ztfl": "",
        "xxly": "",
        "tcfl": "",
        "keyType": "fullText",
        "lowerLimit": "2022-01-01",
        "upperLimit": "2022-06-15",
        "keywordNavigation": 1,
        "checkSearch": 1,
        "timeRange": "",
        "ex": "",
        "url": "",
    }

    s = requests.session()
    r = s.post(url, data=datas, headers=headers)
    # print(r.json())
    page_num = r.json()["pageNum"]
    all_num = r.json()["num"]
    query_times = floor(all_num / 20) + 1
    print("QueryTimes:", query_times)

    time.sleep(5)

    datas["pageSize"] = 20

    now_base = 1

    try:
        nn = con.execute("SELECT max(id) FROM data").fetchone()[0]
        print("[*] Total:", nn)
        now_base += int(nn / 20) * 20
    except:
        now_base = 1

    if now_base == 1:
        start = 1
    else:
        start = int(now_base / 20) + 1

    for i in range(start, query_times + 1):
        datas["pageNow"] = i
        print("[*] try to fetch page:", i)

        r2 = s.post(url, data=datas, headers=headers)
        data_list = r2.json()

        data_list = data_list["array"]
        print(len(data_list))

        for idx, data in enumerate(data_list):
            if cur.execute("select * from data where id = {}".format(idx + now_base - 1)).fetchone():
                print("pass...{}/{}, {}%".format(idx + now_base - 1, all_num,
                                                 round((idx + now_base - 1) / all_num * 100, 2)))
                continue
            title = data["name"]
            pattern = re.compile(r'<[^>]+>', re.S)
            title = pattern.sub('', title)

            showTime = data["showTime"]
            news_url = data["url"]
            time.sleep(1)

            print("fetching url:", news_url)
            r3 = s.get(news_url, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
            })
            r3.encoding = 'utf-8'
            tree = etree.HTML(r3.text)
            content = tree.xpath('//p/text()')

            news_content = ""
            for line in content:
                if line != "":
                    news_content += line
                    news_content += '\n'
            try:
                cur.execute("INSERT INTO data values(?,?,?,?)", (idx + now_base - 1, title, showTime, news_content))
                con.commit()
            except:
                pass
            # print(title, showTime, url, news_content)
            print("processing: {}/{}, {}%".format(idx + now_base - 1, all_num,
                                                  round((idx + now_base - 1) / all_num * 100, 2)))

        now_base += 20
        time.sleep(0.5)
