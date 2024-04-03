import requests
import time
import random
import hashlib
import math
import json
from loguru import logger
import base64

class Spider:
    def __init__(self):
        self.url = 'https://piaofang.maoyan.com/dashboard/webHeatData'
        text_data = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        binary_data = text_data.encode('utf-8')
        byte_string=base64.b64encode(binary_data)
        userAgent =byte_string.decode('utf-8')
        # print(userAgent)
        self.pay_loads = {
            'showDate': '20240402',
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

    def send_request(self):
        signKey = self.getSignKey()
        self.pay_loads['signKey'] = signKey
        try:
            # params = self.pay_loads
            # print(params)
            # response = requests.get(self.url, params=self.pay_loads)
            # 打印完整的 URL 和请求参数
            full_url = self.url + '?' + '&'.join([f'{key}={value}' for key, value in self.pay_loads.items()])
            print('Full URL:', full_url)
            response = requests.get(full_url)
            print(response.text)  # 打印返回的响应内容
            params = self.pay_loads
            print(params)
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
                        logger.info(
                            "播放次数：" + str(item['playCountSplitUnit']['num']) + item['playCountSplitUnit']['unit'])
                    if 'platformDesc' in item['seriesInfo']:
                        logger.info("播放平台：" + item['seriesInfo']['platformDesc'])
                    logger.info("上线时间：" + item['seriesInfo']['releaseInfo'])
            else:
                logger.error("请求失败")
        except requests.exceptions.RequestException as e:
            logger.error("请求异常：" + str(e))

if __name__ == "__main__":
    spider = Spider()
    spider.send_request()
