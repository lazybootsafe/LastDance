# 通讯录和停用词去重
def stopwd_reduction(infilepath, outfilepath):
    infile = open(infilepath, 'r', encoding='utf-8')
    outfile = open(outfilepath, 'w')
    stopwordslist = []
    for str in infile.read().split('\n'):
        if str not in stopwordslist:
            stopwordslist.append(str)
            outfile.write(str + '\n')


stopwd_reduction('cn_stopwords.txt', 'tongxunlu.txt')