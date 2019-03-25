#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:07:32 2019

@author: yuchien
"""

import requests
import simplejson as json
import pandas as pd



def start_end_dates(year,month):
    if month in [1,3,5,7,8,10,12]:
        return '-'.join([str(year),str(month).zfill(2),'01']), '-'.join([str(year),str(month).zfill(2),'31'])
    elif month in [4,6,9,11]:
        return '-'.join([str(year),str(month).zfill(2),'01']), '-'.join([str(year),str(month).zfill(2),'30'])
    else:
        return '-'.join([str(year),'02','01']), '-'.join([str(year),'02','28'])

def df_one_month_closing_price(year,month,ticker):
    
    start_date, end_date = start_end_dates(year, month)
    
    queries = dict(column_index=4, start_date = start_date, end_date = end_date, api_key = 'WV5TpJc_gfxiAAgHRb6M')
    domain = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'.json'
    
    r = requests.get(domain, params = queries)
    
    df = pd.DataFrame(r.json()['dataset']['data'],columns=['Date','Close'])
    df.set_index('Date',inplace = True)
    df.index = pd.to_datetime(df.index)
    
    ax = df.plot()
    fig = ax.get_figure()
    
    return fig

    
   
