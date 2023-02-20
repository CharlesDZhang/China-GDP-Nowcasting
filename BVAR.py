import pandas as pd
import numpy as np 

# GDP_NOM_SECTORS: Nominal GDP of different sectors
# GDP_YOY_SECTORS: Year-on-year real GDP growth rates for different sectors
# AR: Agriculture, Forestry and Fisheries
# ID: Industrial
# CO: Construction
# WH: Wholesale and retail trade
# TR: Transportation, storage and postal services
# AC: Accommodation and catering
# FI: Finance
# RE: Real Estate
# IN: Information transmission, software and information technology services
# LE: Leasing and business services
# OT: Other Industries

GDP_NOM_SECTORS = pd.read_csv('GDP_NOM_SECTORS.csv').set_index('QTR')
GDP_YOY_SECTORS = pd.read_csv('GDP_YOY_SECTORS.csv').set_index('QTR')
GDP_YOY_SECTORS['OT'] = (GDP_NOM_SECTORS[['IN', 'LE', 'OT']].sum(axis = 1) / np.multiply(GDP_NOM_SECTORS[['IN', 'LE', 'OT']] , 1 / (1 + GDP_YOY_SECTORS[['IN', 'LE', 'OT']]/ 100)).sum(axis = 1) - 1 ) * 100
GDP_YOY_SECTORS = GDP_YOY_SECTORS.drop(columns=['IN','LE'])
GDP_NOM_SECTORS['OT'] = GDP_NOM_SECTORS[['IN', 'LE', 'OT']].sum(axis = 1)
GDP_NOM_SECTORS = GDP_NOM_SECTORS.drop(columns=['IN','LE'])
GDP_YOY_SECTORS
#


#
