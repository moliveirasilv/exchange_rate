# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:06:48 2020

@author: mathe
"""

import pandas as pd
import requests

def get_exchange_rate(rate1, rate2, inicial_data, num_months=2):
    
    '''
    Retorna as taxas de cambio das moedas desejadas(rate1 e rate2) dado a data inicial
    inicial_data: deve ser no formato YYYY-MM-DD
    '''
    
    url = 'https://fx-rate.net/historical/?c_input={}&cp_input={}&date_to_input={}&range_input=30&csv=true'.format(rate1,rate2,inicial_data)
    response = requests.get(url)
    text = response.text
    split = text.split("\n")[2:]
    
    
    datas = []
    taxas = []
    
    for i in split:
        data,taxa = i.split(',')
        datas.append(data)
        taxas.append(taxa)
        
        
    n = 1
    while n>=1:
        n+=1
        url = 'https://fx-rate.net/historical/?c_input=ARS&cp_input=USD&date_to_input={}&range_input=30&csv=true'.format(pd.to_datetime(datas[-1]))
        response = requests.get(url)
        text = response.text
        split = text.split("\n")[2:]
        for i in split:
            data,taxa = i.split(',')
            datas.append(data)
            taxas.append(taxa)
    
        if n == num_months:
            break
    return datas,taxas
        
def exchange_rate(rate1, rate2, inicial_data, num_months=2):
    
    '''
    Retorna as taxas de cambio das moedas desejadas(rate1 e rate2) dado a data inicial
    inicial_data: deve ser no formato YYYY-MM-DD
    '''
    
    Dict = {'Data':None,
            'Taxa':None}
    
    Dict['Data'], Dict['Taxa'] = get_exchange_rate(rate1, rate2, inicial_data, num_months)
    
    return Dict
    






