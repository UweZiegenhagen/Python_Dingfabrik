# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:50:57 2019

@author: Uwe
"""

def addiere_all(*werte):
    ergebnis = 0
    for jeder_eintrag in werte:
        ergebnis = ergebnis + jeder_eintrag
    print(ergebnis)
    
addiere_all(1,2,3,4,5,6)

def gib_aus(**werte):
    for key, value in werte.items():
        print(key,":", value)
        
gib_aus(Vorname="Uwe", Nachname="Ziegenhagen", Ort="Köln")