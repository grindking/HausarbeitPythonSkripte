import pandas as pd
import math


#print(type(s[1]))

#Funktion um den Mittelwert zu berechnen
def berechne_mittelwert(daten):
    summe = 0

    for index in range(0,100):
        summe += daten[index]

    return summe / len(daten)

#Funktion um die Standardunsicherheit zu berechnen
def berechne_standardunsicherheit(daten, mittelwert):
    summe = 0
    for index in range(0,100):
        summe += (daten[index] - mittelwert)**2
    return 1 / math.sqrt(len(daten)) * math.sqrt(1 / (len(daten) - 1) * summe)


if __name__ == '__main__':
    messwert_dateien = ['messwerteBalkonAbends.csv', 'messwerteBadezimmer.csv','messwerteWohnzimmer.csv','messwerteBalkonMittags.csv','messwerteKeller.csv']

    for index, datei in enumerate(messwert_dateien):
        df = pd.read_csv(datei)
        temp_daten = df['Temperatur']
        luftfeucht_daten = df['LuftfeuchtigkeitRel']
        emp_mittelwert_temp = berechne_mittelwert(temp_daten)
        stand_unsicherheit_temp = berechne_standardunsicherheit(temp_daten, emp_mittelwert_temp)

        emp_mittelwert_luft = berechne_mittelwert(luftfeucht_daten)
        stand_unsicherheit_luft = berechne_standardunsicherheit(luftfeucht_daten, emp_mittelwert_luft)

        print(f'\n{index} {datei}\nEmpirischer Mittelwert Temperatur: {emp_mittelwert_temp}\tEmpirische Standardunsicherheit: {stand_unsicherheit_temp}\nEmpirischer Mittelwert Luftfeuchtigkeit: {emp_mittelwert_luft}\tEmpirische Standardunsicherheit: {stand_unsicherheit_luft}')

"""
Ausgabe:
0 messwerteBalkonAbends.csv
Empirischer Mittelwert Temperatur: 20.342299999999994   Empirische Standardunsicherheit: 0.06748779987014794       
Empirischer Mittelwert Luftfeuchtigkeit: 65.63940000000004      Empirische Standardunsicherheit: 0.3524492891383686

1 messwerteBadezimmer.csv
Empirischer Mittelwert Temperatur: 26.1621      Empirische Standardunsicherheit: 0.044375417482742374
Empirischer Mittelwert Luftfeuchtigkeit: 58.78810000000001      Empirische Standardunsicherheit: 0.12146660138706958

2 messwerteWohnzimmer.csv
Empirischer Mittelwert Temperatur: 29.423       Empirische Standardunsicherheit: 0.03207677028503949
Empirischer Mittelwert Luftfeuchtigkeit: 39.68910000000001      Empirische Standardunsicherheit: 0.12688793234085494

3 messwerteBalkonMittags.csv
Empirischer Mittelwert Temperatur: 31.530099999999997   Empirische Standardunsicherheit: 0.2741328843514187
Empirischer Mittelwert Luftfeuchtigkeit: 26.422900000000006     Empirische Standardunsicherheit: 0.35283937155767087

4 messwerteKeller.csv
Empirischer Mittelwert Temperatur: 25.265200000000018   Empirische Standardunsicherheit: 0.008719512543135586
Empirischer Mittelwert Luftfeuchtigkeit: 44.9481        Empirische Standardunsicherheit: 0.04797846633984077"""