# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:45:25 2020

@author: admin
"""

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''    
'''
a = ''
b = ""
c = ""
#女
msg=[
b+"相信大家都很熟悉，但是"+a+"是怎么回事呢，下面就让小编带大家一起了解吧。",
a+",其实就是"+c+"，大家可能会很惊讶"+a+"怎么会"+b+"呢？但事实就是这样，小编也感到非常惊讶。",
"这就是关于"+a+"的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！",
]
'''
msg=[
     '语言区',
]
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
for i in msg:
    result  = client.synthesis(i, 'zh', 1, {
        'vol': 5,
        'per': 4 ,#01女2男3情感男4情感女
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(r'D:/Android/%s.mp3'%(i), 'wb') as f:
            f.write(result)