#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:07:32 2019

@author: yuchien
"""

import requests
import simplejson as json
import matplotlib
matplotlib.use('Agg')
import pandas as pd
# from bokeh.plotting import figure, output_file, show
# from bokeh.resources import CDN
# from bokeh.embed import file_html
# from bokeh.models import ColumnDataSource
# from bokeh.embed import components




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
    try:    
        df = pd.DataFrame(r.json()['dataset']['data'],columns=['Date','Close'])
        df.set_index('Date',inplace = True)
        df.index = pd.to_datetime(df.index)

        #output_file("lines.html")
        #p = figure(title="simple line example", x_axis_label='Date', y_axis_label='Price')
        #p.line(df.index, df.Close, legend="Temp.", line_width=2)
        #show(p)
        
        ax = df.plot()
        fig = ax.get_figure()
        
        return fig
    except:
        return "no data for the ticker " + ticker

# def df_one_month_closing_price_v2(year,month,ticker):
    
#     start_date, end_date = start_end_dates(year, month)
    
#     queries = dict(column_index=4, start_date = start_date, end_date = end_date, api_key = 'WV5TpJc_gfxiAAgHRb6M')
#     domain = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'.json'
    
#     r = requests.get(domain, params = queries)
    
#     df = pd.DataFrame(r.json()['dataset']['data'],columns=['Date','Close'])
#     df.set_index('Date',inplace = True)
#     df.index = pd.to_datetime(df.index)

#     source = ColumnDataSource(df)

#     p = figure(x_axis_type="datetime",x_axis_label='Date', y_axis_label='Closing Price', plot_width=800, plot_height=350)
#     p.line('Date', 'Close', source=source,line_width=2)
#     script, div = components(p)
    

    
#     return script, div
   
