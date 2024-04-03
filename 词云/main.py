import pandas as pd
import pyperclip


#pip install openpyxl
# 读取数据文件
# df = pd.read_csv('2015_kunming_9-10.xlsx', sep='\t', header=None, names=['date', 'time', 'id', 'lat', 'lng', 'content'])
df = pd.read_excel('2015_kunming_9-10.xlsx', sheet_name='Sheet1', usecols=[0, 1, 2, 3, 4, 5], names=['date', 'time', 'id', 'lat', 'lng', 'content'])

# 将日期列转换为日期类型
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')

# 提取2015年9月的内容部分
mask = (df['date'].dt.year == 2015) & (df['date'].dt.month == 9)
content = df.loc[mask, 'content']

# 选择日期为2015年9月1日的内容
mask = (df['date'] == '2015-09-01')
content2 = df.loc[mask, 'content']

# 去除网址
content = content.str.replace(r'http\S+', '', regex=True)
content2 = content2.str.replace(r'http\S+', '', regex=True)
# 将处理后的文本复制到剪贴板
pyperclip.copy(content2.str.cat(sep='\n'))
# 打印处理后的文本
# print(content2)

# 去除网址
content = content.str.replace(r'http\S+', '', regex=True)
# 将处理后的文本保存到文件
content.to_csv('processed_content.csv', index=False, header=False)
content2.to_csv('processed_content2.csv', index=False, header=False)