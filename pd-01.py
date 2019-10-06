# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:06:39 2019

@author: Uwe
"""

import pandas as pd

dataframe = pd.read_excel("testdatei.xlsx")
lookup = pd.read_excel("lookup.xlsx")

dataframe['Ergebnis'] = dataframe['Preis'] * dataframe['Anzahl'] 

print(dataframe)

dataframe = pd.merge(left=dataframe, right=lookup, how="inner", left_on="Name", right_on="Produkt")

print(dataframe)