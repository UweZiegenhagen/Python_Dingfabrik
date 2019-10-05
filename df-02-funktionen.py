# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:50:57 2019

@author: Uwe
"""

def addiere_all(*werte):
    ergebnis = 0
    for wert in werte:
        ergebnis = ergebnis + wert
    print(ergebnis)
    
addiere_all(1,2,3,4,5,6)

def gib_aus(**werte):
    for key, value in werte.items():
        print(key,":", value)
        
gib_aus(Vorname="Uwe", Nachname="Ziegenhagen", Ort="Köln")

def gib_aus2(text):
    for zeichen in text:
        print(zeichen)
        
gib_aus2("Hallo Welt")

def gib_aus2_alternativ(text):
    l = len(text)
    for i in list(range(l)):
        print(text[i],end='')
    
gib_aus2_alternativ("Hallo Omm")

