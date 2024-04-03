from Crypto.Cipher import AES # pip install pycryptodome
from base64 import b64encode
import requests
import json
import colorama  # 需要安装 colorama 库
from itertools import cycle
import textwrap


def get_encSecKey():
    return "4a22c09c0f7a1198cf9bd974076c3eefbb0ff0ca52649b680f133abaacb2549f498d52e9dc5848a2b63ac7b02f806c65b5e49bae533e214d51fdaf19892e393c2b3a307d3c0d6073783c4ce5d7152c6c0c0c0c86cef3d711617e6ccc277d6e57f2fba64b015a4a6490e1fdb008e779f36d7ff5f81cf7fbfbc0d9e31f619a1359"
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def get_params(data):
    fisrt = enc_parmas(data,g)
    second = enc_parmas(fisrt,i)
    print(second)
    return second

def enc_parmas(data,key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs),"utf-8")


# 假设 parse_comments_json 是您的函数，用于处理 JSON 字符串
def parse_comments_json(json_data):
    colorama.init()

    color = '\033[94m'  # 蓝色
    end_color = '\033[0m'  # 重置颜色
    try:
        # 将 JSON 字符串解析为 Python 字典
        data = json.loads(json_data)

        # 检查响应码
        if data['code'] == 200:
            comments = data['data'].get('comments', [])
            for comment in comments:
                # # 打印评论者信息
                # user_info = comment['user']
                # print(f"用户: {user_info['nickname']}")
                # print(f"评论内容: {comment['content']}")
                # print(f"用户头像: {user_info['avatarUrl']}")
                #
                # # 检查 'beReplied' 是否存在并且不为 None
                # replies = comment.get('beReplied')
                # if replies and isinstance(replies, list):  # 确保 'beReplied' 是一个列表
                #     print("回复:")
                #     for reply in replies:
                #         print(f"    {reply['content']}")
                # print("-" * 40)

                # #使用 ASCII 字符绘制边框
                # print(f"+ 用户: {user_info['nickname']} +")
                # print(f"+ 评论内容: {comment['content']} +")
                # print(f"+ 用户头像: {user_info['avatarUrl']} +")
                # print("+ + + 回复 + + +")
                # for reply in replies:
                #     print(f"  {reply['content']}")
                # print("+ + + + + + + + + +")
                #使用颜色和高亮
                user_info = comment['user']
                print(f"{color}用户: {user_info['nickname']}{end_color}")
                print(f"{color}评论内容: {comment['content']}{end_color}")
                print(f"{color}用户头像: {user_info['avatarUrl']}{end_color}")
                # 检查 'beReplied' 是否存在并且不为 None
                replies = comment.get('beReplied')
                if replies and isinstance(replies, list):  # 确保 'beReplied' 是一个列表
                    print("回复:")
                    for reply in replies:
                        print(f"    {color} {reply['content']} {end_color}")
                print("-" * 60)
        else:
            print("请求失败，状态码：", data['code'])
    except json.JSONDecodeError as e:
        print("解析 JSON 数据时出错：", e)


def parse_comments_dict(response_dict):
    # 初始化 colorama
    colorama.init()

    # 定义一个颜色列表
    colors = cycle(['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m'])

    def colored_print(text, color=None, width=80):
        wrapped_text = textwrap.fill(text, width)

        if color:
            # 如果提供了颜色，使用提供的颜色
            print(f"{color}{wrapped_text}\033[0m")  # \033[0m 用于重置颜色
        else:
            # 否则，从颜色列表中获取下一个颜色
            color = next(colors)
            print(f"{color}{wrapped_text}\033[0m")
    try:
        # 检查响应码
        if response_dict['code'] == 200:
            comments = response_dict['data']['comments']
            for comment in comments:
                colored_print(f"用户: {comment['user']['nickname']}", color=True)
                colored_print(f"评论内容: {comment['content']}")
                print(f"用户头像: {comment['user']['avatarUrl']}")
                if 'beReplied' in comment and comment['beReplied']:
                    colored_print("回复:")
                    for reply in comment['beReplied']:
                        colored_print(f"    {reply['content']}")
                print("-" * 80)
        else:
            print("请求失败，状态码：", response_dict['code'])
    except KeyError as e:
        print("解析响应数据时出错：", e)

if __name__ == "__main__":
    get_comment_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

    data = {
        "rid": "R_SO_4_404465743",#R_SO_4_1325905146中1325905146其实就是歌词的id
        "threadId": "R_SO_4_404465743",
        "pageNo": "1",
        "pageSize": "100",#每页评论的数目 一般为20
        "cursor": "-1",
        "offset": "0",
        "orderType": "1",
        "csrf_token": ""
    }
    e = '010001'
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    g = '0CoJUm6Qyw8W8jud'
    # i要重新获取 e f g不变

    i = "E800etPzNExIq9gD"
    post_data = {}
    post_data['params'] = get_params(json.dumps(data))

    post_data['encSecKey'] = get_encSecKey()
    print(post_data)
    resp = requests.post(url=get_comment_url, data=post_data)
    # print("Response text:", resp.text)  # Add this line to print the response text

    resp.encoding = 'utf-8'
    json_resp = resp.json()
    # print(json_resp)
    # comments = json_resp['data']['comments']
    # for comment in comments:
    #     content = comment['content']
    #     print(content)
    # 如果您需要将字典转换为JSON字符串，然后再解析，可以这样做：
    json_string = json.dumps(json_resp)  # 将字典转换为JSON字符串
    parsed_json = json.loads(json_string)  # 再将JSON字符串解析回字典
    # parse_comments_json(json_string)
    parse_comments_dict(parsed_json)