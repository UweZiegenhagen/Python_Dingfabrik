# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def berechne_jaehrliche_Annuitaet(kreditsumme, nominalzins_prozent, tilgungssatz_prozent):
    """ Berechnet die _jährliche_ Annuität.
        Jährliche_Rate = (nominalzins + tilgungssatz) * Kreditsumme
        Quelle: https://de.wikipedia.org/wiki/Annuit%C3%A4tendarlehen
    """ 

    zinssatz = nominalzins_prozent / 100
    tilgung = tilgungssatz_prozent / 100
    return round(kreditsumme * (zinssatz + tilgung), 2)


def berechne_monatliche_Annuitaet(kreditsumme, nominalzins_prozent, tilgungssatz_prozent):
    """ Berechnet die _monatliche_ Annuität.
        Jährliche_Rate = (nominalzins + tilgungssatz) * Kreditsumme
        Monatliche_Rate = Jährliche_Rate / 12
    """ 

    zinssatz = nominalzins_prozent / 100
    tilgung = tilgungssatz_prozent / 100
    return round(kreditsumme * (zinssatz + tilgung) / 12, 2)
    
def tilgungsplan_df(kreditsumme, nominalzins_prozent, tilgungssatz_prozent, sondert, wartezeit, monate):
    """ 
        Gibt DataFrame der monatlichen Tilgungen zurück
        
        "monate" für wieviele Monate wird der Tilgungsplan erstellt
        "sondert" Betrag der jährlichen Sondertilgung
        "wartezeit" Anzahl der Jahre ohne Sondertilgung
    """

    df = pd.DataFrame()
    restschuld = kreditsumme # Am Anfang entspricht die Restschuld der Kreditsumme
    zinssatz = nominalzins_prozent / 100
    tilgung = tilgungssatz_prozent / 100
    
    annuitaet = berechne_monatliche_Annuitaet(kreditsumme, nominalzins_prozent, tilgungssatz_prozent)
    zinsen = 0
    
    for j in range(1,monate+1):
        # Split der Annuität in ihre Komponenten Zinslast und Tilgung
        zinsen = restschuld * zinssatz / 12 
        # Wenn Restschuld kleiner Annuität, dann wird die komplette 
        # Restschuld getilgt
        tilgung = restschuld if restschuld < annuitaet else annuitaet - zinsen    

        anfangsschuld = restschuld
        jahr = ((j-1) // 12) + 1 # in welchem Monat befinden wir uns
        
        # Sondertilgungen im Dezember eines Jahres, wenn wir 
        # nicht in der Wartezeit sind
        if j % 12 == 0 and anfangsschuld > 0 and jahr > wartezeit:
            sondertilgung = sondert
        else:
            sondertilgung = 0

        # Restschuld_neu = Restschuld_alt minus Tilgung minus Sondertilgung
        restschuld = restschuld - tilgung - sondertilgung
         
        # Dataframe befüllen
        df = df.append({'Monat': j, 'Jahr': jahr,'Anfangsschuld': anfangsschuld, 
        'Zinsen':zinsen, 'Tilgung': tilgung, 'Sondertilgung': sondertilgung,
        'Restschuld': restschuld}, ignore_index=True)    
    
    # Indikatorspalte, "1" wenn der Kredit noch nicht abbezahlt ist, sonst "0"
    df['Indikator'] = np.where(df['Anfangsschuld']>0, 1, 0)
    # Umsortieren der Spalten
    df = df[['Monat', 'Jahr', 'Anfangsschuld', 'Zinsen', 'Tilgung', 'Sondertilgung', 'Restschuld', 'Indikator']]
    
    # Runden auf 2 Nachkommastellen
    for i in ['Anfangsschuld', 'Zinsen', 'Tilgung', 'Restschuld']:
        df[i] = df[i].apply(lambda x: round(x, 2))    
    
    # Monat als Index nutzen
    df.set_index('Monat', inplace=True)
    return df


tilgungsplan = tilgungsplan_df(100000, 1.0, 2.0, 5000, 0, 200)
#Wie lange läuft der Kredit
print('Gesamtlaufzeit:', round(tilgungsplan['Indikator'].sum(),1), 'Monate')

tilgungsplan.to_excel('tilgungsplan_gesamt.xlsx')