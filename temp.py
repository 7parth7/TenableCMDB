# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:04:56 2020

@author: pkb13
"""
import requests,json

Params = {'fields':'id'}
r = requests.get(url = 'https://tenable.partners.org/scanResult', params = Params)

data = r.json()
print(data)
