# -*- coding:utf-8 -*-
import requests
import json
from pyecharts import Bar
"""
此位置代码获取一首歌曲的热评
"""
url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=568cec564ccadb5f1b29311ece2288f1'

headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
   'Referer':'http://music.163.com/song?id=551816010',
   'Origin':'http://music.163.com',
   'Host':'music.163.com'
}
#加密数据，直接拿过来用
user_data = {
   'params': "ld0NOuUJ+QErB0VC9Qn+qV7JAa5+QMFsO3FLxC/9eQgSarbuP+v+CKiaFoBLwqoYULC8dT532Vz8Rcr6JK7NWPPboZiRUnsnLPIqliLQ531dUc4dDKj0fPgLD3O4i+D6naXDXNlCZM3FyjlHDlRq3EyD82ZFf0m9wQ+78bxA0R8mNS/eR4SVGE/eDk+EihUa",

   'encSecKey': '0fc6e00a72970fb6c6a7bbd95b1f934834ee8ffcfc3353710eb5bdcb976818e2db0a8dbdfed9144e16b70c3d43e7e5a1c634c49084f3f2c6f7a069d1020320ad6a47205028a2b4501021f83dc5c79d5d93a113e190ae59409a9fd8533c3d12bb9f087a622f7ddace6fd0fcb0cfa53f0b184b6882c4a97e5f320d6cc24978e085'
}

response = requests.post(url, headers=headers, data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
   item = {
       'nickname': hotcommment['user']['nickname'],
       'content': hotcommment['content'],
       'likedCount': hotcommment['likedCount']
   }
   hotcomments.append(item)

# 获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

# for content in content_list:  # 测试
#     print content

"""将点赞数做成一个图表展示"""
bar = Bar("热评中点赞数示例图")
bar.add("点赞数", nickname, liked_count, is_stack=True, mark_line=["min", "max"], mark_point=["average"])
bar.render()
