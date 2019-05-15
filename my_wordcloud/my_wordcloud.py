# -*- coding: utf-8 -*- 
from wordcloud import WordCloud
import jieba
import cv2
import numpy as np

def create_wordcloud(text_path,bg_file,wc_file):
    text_path = "text/" + text_path
    bg_file = "bg/" + bg_file
    wc_file = "result/" + wc_file
    with open(text_path,'r',encoding='utf-8') as f:
        cut_word = jieba.cut(f.read())
    result = " ".join(cut_word)
    img = cv2.imread(bg_file) #背景图，可以换成自己想要的图片
    img_array = np.array(img)
    stop_words = ["开发","工作","优先","具有","要求","公司","java","PHP","参与","熟悉","任职"] #需要屏蔽的词语
    
    wc = WordCloud(
        font_path='simhei.ttf',     #字体
        background_color='white',   #背景颜色
        width=1000,
        height=600,
        max_font_size=80,
        min_font_size=10,
        mask = img_array,  #背景图片
        max_words=1000,
        stopwords=stop_words
    )
    wc.generate_from_text(result)
    wc.to_file(wc_file)

'''
if __name__ == '__main__':
    create_wordcloud("job_java.txt",'bg_java.png','job_java.png')
'''