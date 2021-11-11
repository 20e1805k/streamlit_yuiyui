# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:13:56 2021

@author: iwanaga yuika
"""

import streamlit as st

st.title('初めてのstream')
st.write('私の名前は〇〇です')

text=st.text_input('あなたの名前を教えてください')
'あなたの名前は,',text,'です'

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition

option = st.selectbox(
    '好きな数字を教えてください',
    list(['1番','2番','3番','4番',])
)
'あなたが選択したのは,',option,'です'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
from PIL import Image
img = Image.open('room.jpg')
st.image(img,caption='写真の説明',use_column_width=True)