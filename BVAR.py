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
df_G['现价:其他'] =  df_G['现价:信'] + df_G['现价:租'] + df_G['现价:其'] 
df_G = df_G[['现价:农', '现价:工', '现价:建', '现价:批', '现价:交', '现价:住', '现价:金', '现价:房', '现价:其他']]


from rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects import globalenv
from rpy2.robjects import pandas2ri
pandas2ri.activate()

BVAR = importr("BVAR")
df_pre = df[:].copy()
df_pre= df_pre.append(pd.DataFrame([],index = [pd.to_datetime('2022-12-31')]))
df_pre[:] = 0

df_pre1 = df[:].copy()
df_pre1=df_pre1.append(pd.DataFrame([],index = [pd.to_datetime('2022-12-31')]))
df_pre1[:] = 0

for i in tqdm(range(84,124)): 
    rdf = pandas2ri.py2rpy(df.iloc[:i])
    globalenv['rdf'] = rdf
    rscript = """
    bv_priors <- bv_mn( 
    lambda = bv_lambda(mode = 0.6 ),
    alpha = bv_alpha(mode = 0.4), 
    var = 10000000, 
    b =1
    ) 
    x <- bvar(rdf, lags = 6, n_draw = 1000L, n_burn = 200L, priors = bv_priors(), verbose = FALSE)
    predict(x) <- predict(x, horizon = 2)
    irf(x) <- irf(x, horizon = 2, fevd = FALSE)
    summary(x)
    """
    result = r(rscript)
    df_pre.iloc[i] = np.median(result[0][10][0] ,  axis = 0 )[0]
    df_pre1.iloc[i] = np.median(result[0][10][0] ,  axis = 0 )[1]
    
  df_GDP = df_G.shift(4)
df_GDP =   df_pre[84:].merge( df_GDP , left_index=True, right_index=True , how= 'left')
df_GDP['predict'] = 0
df_GDP.iloc[:,:9] = df_GDP.iloc[:,:9] /100 + 1
df_GDP['predict'] = (df_GDP['现价:农'] * df_GDP['不变价:农'] + df_GDP['现价:工'] * df_GDP['不变价:工'] + df_GDP['现价:建'] * df_GDP['不变价:建'] + df_GDP['现价:批'] * df_GDP['不变价:批'] + df_GDP['现价:交'] * df_GDP['不变价:交'] + df_GDP['现价:住'] * df_GDP['不变价:住'] + df_GDP['现价:金'] * df_GDP['不变价:金'] + df_GDP['现价:房'] * df_GDP['不变价:房'] + df_GDP['现价:其他'] * df_GDP['不变价:其他']) / (df_GDP['现价:农'] + df_GDP['现价:工'] + df_GDP['现价:建'] + df_GDP['现价:批'] + df_GDP['现价:交'] + df_GDP['现价:住'] + df_GDP['现价:金'] + df_GDP['现价:房'] + df_GDP['现价:其他']  )* 100 - 100
df_GDP['predict'].iloc[-1] = (df_GDP['现价:农'].iloc[-4]  * df_GDP['不变价:农'].iloc[-1]  + df_GDP['现价:工'].iloc[-4]  * df_GDP['不变价:工'].iloc[-1]  + df_GDP['现价:建'].iloc[-4]  * df_GDP['不变价:建'].iloc[-1]  + df_GDP['现价:批'].iloc[-4] * df_GDP['不变价:批'].iloc[-1] + df_GDP['现价:交'].iloc[-4] * df_GDP['不变价:交'].iloc[-1] + df_GDP['现价:住'].iloc[-4] * df_GDP['不变价:住'].iloc[-1] + df_GDP['现价:金'].iloc[-4] * df_GDP['不变价:金'].iloc[-1] + df_GDP['现价:房'].iloc[-4] * df_GDP['不变价:房'].iloc[-1] + df_GDP['现价:其他'].iloc[-4] * df_GDP['不变价:其他'].iloc[-1]) / (df_GDP['现价:农'].iloc[-4] + df_GDP['现价:工'].iloc[-4] + df_GDP['现价:建'].iloc[-4] + df_GDP['现价:批'].iloc[-4] + df_GDP['现价:交'].iloc[-4] + df_GDP['现价:住'].iloc[-4] + df_GDP['现价:金'].iloc[-4] + df_GDP['现价:房'].iloc[-4] + df_GDP['现价:其他'].iloc[-4]  )* 100 - 100
 

zz
