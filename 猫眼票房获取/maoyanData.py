import requests
import time
import random
import hashlib
import math
import json
from loguru import logger
import base64
import pandas as pd

class Spider:
    def __init__(self):
        # self.url = 'https://piaofang.maoyan.com/dashboard/webHeatData'#网络播放热度
        self.url = 'https://piaofang.maoyan.com/dashboard-ajax'#综合数据

        self.cookies = {
            '_lxsdk_cuid': '18e9d7a5d52c8-0d0be97856c61a-26001a51-240000-18e9d7a5d52c8',
            '_lxsdk': '18e9d7a5d52c8-0d0be97856c61a-26001a51-240000-18e9d7a5d52c8',
            '_lxsdk_s': '18e9d7a5d52-099-6e3-228%7C%7C25',
        }
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        binary_data = ua.encode('utf-8')
        byte_string=base64.b64encode(binary_data)
        userAgent =byte_string.decode('utf-8')
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://piaofang.maoyan.com/dashboard',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': userAgent,
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.headers = headers
        self.pay_loads = {
            # 'showDate': '20240402',#综合数据无此参数
            'uuid': '18e9d7a5d52c8-0d0be97856c61a-26001a51-240000-18e9d7a5d52c8',
            'channelId': '40009',
            'sVersion': '2',
            'User-Agent': userAgent,
        }
        self.key = 'A013F70DB97834C0A5492378BD76C53A'

    def getIndex(self):
        return math.floor(1000 * random.random() + 1)

    def getD(self):
        self.pay_loads['index'] = self.getIndex()
        self.pay_loads['timeStamp'] = int(time.time() * 1000)
        logger.info('timeStamp:' + str(self.pay_loads['timeStamp']))
        d = 'method=GET&timeStamp=' + str(self.pay_loads['timeStamp']) + '&User-Agent=' + self.pay_loads['User-Agent'] + '&index=' \
            + str(self.pay_loads['index']) + '&channelId=' + str(self.pay_loads['channelId']) + '&sVersion=' + str(self.pay_loads['sVersion']) + \
            '&key=' + self.key
        d = d.replace(r'/\s+/g', " ")
        return d

    def getSignKey(self):
        md5 = hashlib.md5()
        d = self.getD()
        md5.update(d.encode('utf-8'))
        signKey = md5.hexdigest()
        self.pay_loads['signKey'] = signKey
        logger.info("signKey:" + signKey)
        return signKey

    def send_request1(self):
        signKey = self.getSignKey()
        self.pay_loads['signKey'] = signKey
        try:
            # response = requests.get(self.url, cookies=self.cookies, headers=self.headers)
            # 打印完整的 URL 和请求参数
            full_url = self.url + '?' + '&'.join([f'{key}={value}' for key, value in self.pay_loads.items()])
            # print('Full URL:', full_url)
            response = requests.get(full_url,cookies=self.cookies, headers=self.headers)
            # print(response.text)  # 打印返回的响应内容
            # params=self.pay_loads
            # print(params)
            response.raise_for_status()  # 如果响应状态码不为 200，将会抛出一个异常
            data = response.json()
            if data['status']:
                logger.info("请求成功")
                dataList = data['dataList']['list']
                for item in dataList:
                    logger.info("影片名称：" + item['seriesInfo']['name'])
                    logger.info("当前热度：" + str(item['currHeat']))
                    logger.info("当前热度描述：" + item['currHeatDesc'])
                    if 'playCountSplitUnit' in item:
                        logger.info("播放次数：" + str(item['playCountSplitUnit']['num']) + item['playCountSplitUnit']['unit'])
                    if 'platformDesc' in item['seriesInfo']:
                        logger.info("播放平台：" + item['seriesInfo']['platformDesc'])
                    logger.info("上线时间：" + item['seriesInfo']['releaseInfo'])
            else:
                logger.error("请求失败")
        except requests.exceptions.RequestException as e:
            logger.error("请求异常：" + str(e))

    def send_request(self):
        # Your existing code
        signKey = self.getSignKey()
        self.pay_loads['signKey'] = signKey
        try:
            # response = requests.get(self.url, cookies=self.cookies, headers=self.headers)
            # 打印完整的 URL 和请求参数
            full_url = self.url + '?' + '&'.join([f'{key}={value}' for key, value in self.pay_loads.items()])
            # print('Full URL:', full_url)
            response = requests.get(full_url, cookies=self.cookies, headers=self.headers)
            # print(response.text)  # 打印返回的响应内容
            # params=self.pay_loads
            # print(params)
            response.raise_for_status()  # 如果响应状态码不为 200，将会抛出一个异常
            data = response.json()
            if data['status']:
                logger.info("请求成功")
                dataList = data['dataList']['list']
                # Create an empty list to store the data
                result_data = []
                for item in dataList:
                    # Your existing code

                    # Append the data for each item to the result_data list
                    result_data.append({
                        "影片名称": item['seriesInfo']['name'],
                        "当前热度": item['currHeat'],
                        "当前热度描述": item['currHeatDesc'],
                        "播放次数": str(item['playCountSplitUnit']['num']) + item['playCountSplitUnit'][
                            'unit'] if 'playCountSplitUnit' in item else None,
                        "播放平台": item['seriesInfo']['platformDesc'] if 'platformDesc' in item['seriesInfo'] else None,
                        "上线时间": item['seriesInfo']['releaseInfo']
                    })

                # Convert the list of dictionaries to a DataFrame
                df = pd.DataFrame(result_data)

            else:
                logger.error("请求失败")
        except requests.exceptions.RequestException as e:
            logger.error("请求异常：" + str(e))
                # Display the DataFrame
        print(df)
    def send_request3(self):
            # Your existing code
            signKey = self.getSignKey()
            self.pay_loads['signKey'] = signKey
            try:
                # response = requests.get(self.url, cookies=self.cookies, headers=self.headers)
                # 打印完整的 URL 和请求参数
                full_url = self.url + '?orderType=0' + '&'.join([f'{key}={value}' for key, value in self.pay_loads.items()])
                # print('Full URL:', full_url)
                response = requests.get(full_url, cookies=self.cookies, headers=self.headers)
                # print(response.text)  # 打印返回的响应内容
                # params=self.pay_loads
                # print(params)
                response.raise_for_status()  # 如果响应状态码不为 200，将会抛出一个异常
                data = response.json()
                # 检查响应状态
                if data['status']:
                    logger.info("请求成功")

                    # 提取电影列表数据
                    movie_list = data.get('movieList', {}).get('data', {}).get('list', [])
                    movie_data = [{'电影名称': item['movieInfo']['movieName'],
                                   '上映天数': item['movieInfo']['releaseInfo'],
                                   '累计票房': item['sumBoxDesc'],
                                   '场均人次': item['avgSeatView'],
                                   '场均放映': item['avgShowView'],
                                   '票房占比': item['boxRate']} for item in movie_list]

                    # 提取网络列表数据
                    web_list = data.get('webList', {}).get('data', {}).get('list', [])
                    web_data = [{'剧集名称': item['seriesInfo']['name'],
                                 '更新天数': item['seriesInfo']['releaseInfo'],
                                 '当前热度': item['currHeat'],
                                 '热度描述': item['currHeatDesc']} for item in web_list]

                    # 提取电视列表数据
                    tv_list = data.get('tvList', {}).get('data', {}).get('list', [])
                    tv_data = [{'节目名称': item['programmeName'],
                                '关注度': item['attentionRateDesc'],
                                '市场占有率': item['marketRateDesc'],
                                '频道名称': item['channelName']} for item in tv_list]

                    # 将数据转换为DataFrame
                    movie_df = pd.DataFrame(movie_data)
                    web_df = pd.DataFrame(web_data)
                    tv_df = pd.DataFrame(tv_data)

                    # 这里可以添加将DataFrame保存到文件或进行进一步处理的代码
                    # ... 您的代码 ...

                    # return movie_df, web_df, tv_df  # 返回所有DataFrame
                    print(movie_df, web_df, tv_df)
                else:
                    logger.error("请求失败: " + data.get('message', 'No message provided'))
            except requests.exceptions.RequestException as e:
                logger.error("请求异常：" + str(e))
                    # Display the DataFrame

if __name__ == "__main__":
    spider = Spider()
    spider.send_request3()
