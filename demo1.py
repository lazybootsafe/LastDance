# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open('1234.txt', encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 生成对象
wc = WordCloud(font_path='simhei.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
