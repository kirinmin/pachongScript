import requests
import json
import time
import logging
import multiprocessing
from datetime import datetime, date
from rich.logging import RichHandler
from rich.console import Console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  # Add time information
    datefmt="%Y-%m-%d %H:%M:%S",  # The format of time
    handlers=[RichHandler(rich_tracebacks=True)]
)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console = Console()
#自动定义抢购类
class Qianggou:
    def __init__(self, start_time_str, thread_per_ck, cks,maxkey,value):
        self.start_time = datetime.strptime(start_time_str, '%H:%M:%S.%f').time()
        self.thread_per_ck = thread_per_ck
        self.cks = cks
        self.maxkey = maxkey
        self.value = value
        self.results = multiprocessing.Manager().dict()  # 使用Manager创建共享字典
        self.logger = logging.getLogger('rich')
    #获取网络时间
    def get_network_time(self):
        url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
        response = requests.get(url)
        result = response.json()
        timestamp = int(result['data']['t']) / 1000.0
        return datetime.fromtimestamp(timestamp).time()
    #打印时间
    def print_remaining_time(self):
        while True:
            net_time = self.get_network_time()
            if net_time >= self.start_time:
                break
            remaining_seconds = (datetime.combine(date.today(), self.start_time) - datetime.combine(date.today(), net_time)).total_seconds()
            logging.info(f"剩余时间： {remaining_seconds} 秒")
            time.sleep(0.5)
    #启动函数
    def run(self):
        self.print_remaining_time()
        jobs = []
        for ck, ck_value in self.cks.items():
            for i in range(self.thread_per_ck):
                p = multiprocessing.Process(target=self.fetch, args=(ck, ck_value))
                jobs.append(p)
                p.start()

        for job in jobs:
            job.join()  # 等待所有进程结束
        logging.info(dict(self.results))  # 使用copy将共享字典的内容复制到一个普通字典中

        # 在所有线程结束后，遍历results字典，将抢券结果推送一次
        push_results = {ck: result for ck, result in self.results.items()}
        logging.info(f"Pushing results: {push_results}")
        push_results = json.dumps(push_results, ensure_ascii=False, indent=4)
        # api.QL.push(push_results)
    #主要逻辑
    def fetch(self, ck, ck_value):
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2a) NetType/WIFI Language/zh_CN",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip,compress,br,deflate",
            "Accept": "v=1.0",
            "Content-Length": "64",
            "Qm-From": "wechat",
            'Qm-From-Type': 'catering',
            "Referer": "https://servicewechat.com/wxafec6f8422cb357b/115/page-frame.html",
            "Qm-User-Token": ck_value
        }
        count = 0
        url = 'https://qmwebapi.qmai.cn/web/cmk-center/receive/takePartInReceive'
        while True:
            Keyword = self.value[count]
            count +=1
            data = {"activityId":"960462825150283776","keyWords":Keyword,"appid":"wxafec6f8422cb357b"}
            data = json.dumps(data)
            response = requests.post(url, headers=headers, data=data)
            response_text = response.text
            response_text = json.loads(response_text)
            logging.info(response_text)
            response_text = response_text['message']
            push_mesg = f"remark==>{ck}, response={response_text}"
            logging.info(f"remark==>{ck}, response={response_text}")
            if response.status_code == 200:
                if '游客禁止参与活动' in response_text or 'ok' in response_text or '本日已达上限' in response_text or count == self.maxkey :
                    self.results[ck] = push_mesg  # 更新抢券结果到results字典
                    break                    
            else:
                logging.error(f'CK={ck}, 请求失败，响应状态码为{response.status_code}')
            time.sleep(0.002)

if __name__ == '__main__':
    # 每个CK的并发数量
    thread_per_ck = 1
    #启动时间
    start_time_str = '11:16:59.550'
    #用户tokens，格式是：remark：token
    cks={
        'remark':''
    }
    maxkey = 3 #你有几个答案这里就写几
    key_value = ['龙年会友杯',"龙年会友杯什么都会有",'龙年会有'] #答案列表，把你认为最有可能的答案写在前面，顺序是依次进行的。
    logging.info(f"start_time_str={start_time_str}, thread_per_ck={thread_per_ck}, cks={cks},maxkey={maxkey},key_value={key_value}")
    qianggou = Qianggou(start_time_str, thread_per_ck, cks,maxkey,key_value)
    qianggou.run()
