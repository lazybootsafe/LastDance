#conding:utf-8
import jieba
#jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典
import chnSegment
#import plotWordcloud # 另一种方式实现的依赖
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('./cn_stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


inputs = open('qq.txt', 'r', encoding='utf-8')
#inputs = open('wx.txt', 'r', encoding='utf-8')
#inputs = open('0day.txt', 'r', encoding='utf-8') # 此处有专用分词和数据预处理工具调用
outputs = open('output.txt', 'w',encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

text1 = chnSegment.word_segment(open('output.txt', encoding='utf-8').read()) #词频统计 可在词频统计中完成用户词典载入
text = open('output.txt', encoding='utf-8').read()

# 生成对象
wc = WordCloud(font_path='simhei.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)# 可改变样式 详见wordcloud

# 显示词云
# plotWordcloud.generate_wordcloud(text) 另外一种实现方式
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


