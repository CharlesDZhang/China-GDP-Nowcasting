import sys
import os
import os.path
import pandas as pd
import numpy as np 
from datetime import datetime
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")
from WindPy import *  
w.start()
if w.isconnected():
    print('Wind API 连接成功！')
else:
    print('Wind API 连接失败，请重试！') 

    
df = pd.read_excel('GDP_Q.xlsx',header = 1, index_col = 0).fillna(0)
df_G = df.copy()
df['不变价:其他'] = 0 
df.loc[df[:92].index, '不变价:其他'] = df.loc[df[:92].index, '不变价:其']
df.loc[df[92:].index, '不变价:其他'] = ((df['现价:信'] + df['现价:租']+ df['现价:其'])  / (df['现价:信'] / (df['不变价:信']/100+1) + df['现价:租'] / (df['不变价:租']/100+1)   + df['现价:其'] / (df['不变价:其']/100+1)) *100 -100 )[92:]
df = df[['不变价:农', '不变价:工', '不变价:建', '不变价:批', '不变价:交', '不变价:住', '不变价:金', '不变价:房',  '不变价:其他']]
df
