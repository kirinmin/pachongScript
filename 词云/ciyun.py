# import pandas as pd
# import os
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# wordcloud = WordCloud(font_path='msyh.ttc')
# # 定义生成词云的函数
# def generate_wordcloud(text, save_path):
#     # 生成词云
#     wordcloud = WordCloud(font_path='simhei.ttf').generate(text)
#
#     # 显示词云
#     # plt.imshow(wordcloud, interpolation='bilinear')
#     # plt.axis('off')
#     # plt.show()
#
#     # 保存词云图片
#     wordcloud.to_file(save_path)
#
# # 读取数据文件
# df = pd.read_excel('2015_kunming_9-10.xlsx', sheet_name='Sheet1', usecols=[0, 1, 2, 3, 4, 5], names=['date', 'time', 'id', 'lat', 'lng', 'content'])
#
# # 将日期列转换为日期类型
# df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
#
# # 提取2015年9月1日的内容部分
# mask = (df['date'].dt.year == 2015) & (df['date'].dt.month == 9) & (df['date'].dt.day == 3)
# content = df.loc[mask, 'content']
#
# # 去除网址
# content = content.str.replace(r'http\S+', '', regex=True)
#
# # 合并文本
# text = content.str.cat(sep=' ')
#
# for day in range(1, 32):
#     # 读取文本文件
#     # text_file = f'data/{day}.txt'
#     # if not os.path.exists(text_file):
#     #     continue
#     # with open(text_file, 'r', encoding='utf-8') as f:
#     #     text = f.read()
#     # 生成词云并保存
#     save_path = f'wordclouds/{day}.png'
#     generate_wordcloud(text, save_path)
# # 创建词云
# wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white', max_words=100, max_font_size=100, random_state=42)
# # wordcloud = WordCloud(font_path='simhei.ttf', mask=mask, background_color='white')
# wordcloud.generate(text)
#
# # 显示词云
# plt.figure(figsize=(12, 6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()
#
#
import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
# 定义生成词云的函数
def generate_wordcloud(text, save_path):
    # 生成词云
    wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', width=800, height=400, random_state=42).generate(text)

    # 保存词云图片
    wordcloud.to_file(save_path)

# 读取数据文件
df = pd.read_excel('2015_kunming_9-10.xlsx', sheet_name='Sheet1', usecols=[0, 1, 2, 3, 4, 5], names=['date', 'time', 'id', 'lat', 'lng', 'content'])
# 将日期列转换为日期类型
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
# 循环生成每一天的词云图片
for day in range(1, 32):
    # 提取指定日期的内容部分
    mask = (df['date'].dt.year == 2015) & (df['date'].dt.month == 9) & (df['date'].dt.day == day)
    content = df.loc[mask, 'content']
    # 去除网址
    content = content.str.replace(r'http\S+', '', regex=True)
    # 去除无效字符
    content = content.str.strip()
    # 合并文本
    text = content.str.cat(sep=' ')
    # 要去除的无效词列表
    invalid_words = ['分享图片', '泪泪', '哈哈','哈','泪','亚洲新歌榜','嘻嘻','爱你','笑cry','鲜花','打榜','拜拜','怒骂','色','晚安','霍建华','心','鼓掌','doge','害羞','邓超','微笑','抓狂','我正在为','拍拍','小店']
    # 使用正则表达式去除无效词
    for word in invalid_words:
        text = re.sub(word, '', text)
    # 如果文本为空，则跳过处理
    if not text:
        continue
    print(f'Day {day}: {text[:50]}...')  # 输出前50个字，方便调试
    # 生成词云并保存
    save_path = f'wordclouds/09{day}.png'
    # 检查目录是否存在，如果不存在则创建目录
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    generate_wordcloud(text, save_path)
for day in range(1, 32):
    # 提取指定日期的内容部分
    mask = (df['date'].dt.year == 2015) & (df['date'].dt.month == 10) & (df['date'].dt.day == day)
    content = df.loc[mask, 'content']
    # 去除网址
    content = content.str.replace(r'http\S+', '', regex=True)
    # 去除无效字符
    content = content.str.strip()
    # 合并文本
    text = content.str.cat(sep=' ')
    # 要去除的无效词列表
    invalid_words = ['分享图片', '泪泪', '哈哈','哈','泪','亚洲新歌榜','嘻嘻','爱你','笑cry','鲜花','打榜','拜拜','怒骂','色','晚安','霍建华','心','鼓掌','doge','害羞','邓超','微笑','抓狂','我正在','拍拍','小店']
    # 使用正则表达式去除无效词
    for word in invalid_words:
        text = re.sub(word, '', text)
    # 如果文本为空，则跳过处理
    if not text:
        continue
    print(f'Day {day}: {text[:50]}...')  # 输出前50个字，方便调试
    # 生成词云并保存
    save_path = f'wordclouds/10{day}.png'
    # 检查目录是否存在，如果不存在则创建目录
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    generate_wordcloud(text, save_path)