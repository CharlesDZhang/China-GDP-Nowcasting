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
