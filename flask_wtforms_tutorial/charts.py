'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries 
import pandas

API_URL = "https://www.alphavantage.co/query"
API_KEY = "X0AWJSYKTOKX2F5E"  

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

def getData(symbol, timeSeries, chartType, startDate, endDate):

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if timeSeries == '1':
        data, meta_data = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
    if timeSeries == '2':
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
    if timeSeries == '3':
        data, meta_data = ts.get_weekly(symbol=symbol)
    if timeSeries == '4':
        data, meta_data = ts.get_monthly(symbol=symbol)

    data_date_changed = data[endDate:startDate]

    if chartType == "1":
        line_chart = pygal.Bar(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}:  {} to {}'.format(symbol, startDate, endDate)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        return line_chart

    elif chartType == "2":
        line_chart = pygal.Line(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}: {} to {}'.format(symbol, startDate, endDate)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        return line_chart

