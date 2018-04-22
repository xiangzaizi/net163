# -*- coding:utf-8 -*-
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path
import jieba
import os
import numpy as np
import PIL.Image as Image
from wordcloud import wordcloud, ImageColorGenerator

"""将热评进行词云显示"""
# 1. 将存在text内容加载出来
d = path.dirname(__file__)
text = open(path.join(d, 'we_comment.txt')).read()

# 2. 使用jieba分词对中文进行显示
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)


"""图片生成方式一: 默认图片内容的生成"""
# wordcloud = WordCloud(font_path=r"./SIMHEI.TTF", max_words=200).generate(wl_space_split)
# plt.figure()
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

"""方式二: 使用自己添加的图片"""
# 更改目录下worldcloud, 生成自定义的图片
from scipy.misc import imread
# 生成图片的方式一 imread
# alice_coloring = imread(path.join(d, "xiaohuangren.jpg"))
# 生成图片方式二  np.array 两者的导包不一样, 用法页不一样
alice_coloring = np.array(Image.open(os.path.join(d, "xiaohuangren.jpg")))


wc = WordCloud(font_path=r"./SIMHEI.TTF",
                      background_color='white',  # 背景颜色
                      stopwords=STOPWORDS.add("said"),  # 优化字体？
                      max_words=2000,  # 词云显示的最大词数 最大次数支持？
                      mask=alice_coloring,  # 添加自定义的图片
                      max_font_size=66,  # 设置显示的字体的大小

                      ).generate(wl_space_split)

# 设置通过图片的背景生成颜色值
image_colors = ImageColorGenerator(alice_coloring)

# 绘制词云
plt.figure()
plt.imshow(wc)
# plt.imshow(wc.recolor(color_func=image_colors))  # color_func 背景图片颜色值
# plt.imshow(wc, interpolation='bilinear')  # 默认图片生成
plt.axis('off')
# plt.show()

# 绘制背景图片未颜色的图片
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

# 将生成的图片保存
wc.to_file(path.join(d, 'cloud_words.jpg'))