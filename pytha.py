# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:08:15 2019

@author: Uwe
"""

def pythagoras():
    global kathete1
    global kathete2
    kathete1 = float(input("Seite 1 "))
    kathete2 = float(input("Seite 2 "))
    print((kathete1**2 + kathete2 **2)**0.5)
    
pythagoras()