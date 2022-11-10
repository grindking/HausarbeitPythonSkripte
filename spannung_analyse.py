import pandas as pd
import math

#in Volt
unsicherheit_quantisierungsabweichung = 0.000375 / math.sqrt(3)

#####KOPIERT AUS stat-analyse.py DAMIT ALLE SKRIPTE UNABHÄNGIG VONEINANDER SIND
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
###### ENDE

#Sensitivität der Spannung für die Temperatur
def berechne_sensitivität_temp_spannung(spannung):
    return 5.19*((3*0.0000000803*math.pow(math.log(((5.19-spannung)/spannung) *5100), 2) + 0.00027267)) / (spannung*(spannung-5.19)*(0.0000000803*math.pow(math.log(((5.19-spannung)/spannung) *5100), 3)+0.00027267*math.log(((5.19-spannung)/spannung) *5100)+0.0007799)**2)

#Sensitivität der Spannung für die Luftfeuchtigkeit
def berechne_sensitivität_luft_spannung(temperatur):
     return (611.2*math.exp((17.62*temperatur)/(243.12+temperatur))) / (461.52*(273.15+temperatur))

#Sensitivität der Temperatur für die Luftfeuchtigkeit
def berechne_sensitivitaet_temperatur(spannung, temperatur):
    return (611.2*(spannung/3) *math.exp((17.62*temperatur)/(243.12+temperatur))*(math.pow(temperatur,2) + (2 - 17.62)*243.12*temperatur-17.62*243.12*273.15+ (243.12**2))) / (461.52*((temperatur+243.12)**2)*((temperatur+273.15)**2))

if __name__ == '__main__':
    messwert_dateien = ['messwerteBalkonAbends.csv', 'messwerteBadezimmer.csv','messwerteWohnzimmer.csv','messwerteBalkonMittags.csv','messwerteKeller.csv']

    for index, datei in enumerate(messwert_dateien):
        df = pd.read_csv(datei)
        temp_spannung_daten = df['SpannungTemp']
        luftfeucht_spannung_daten = df['SpannungLuft']
        temp_daten = df['Temperatur']
        luftfeucht_daten = df['LuftfeuchtigkeitRel']
        emp_mittelwert_temp_spannung = berechne_mittelwert(temp_spannung_daten)
        stand_unsicherheit_temp_spannung = berechne_standardunsicherheit(temp_spannung_daten, emp_mittelwert_temp_spannung) + unsicherheit_quantisierungsabweichung

        emp_mittelwert_temp = berechne_mittelwert(temp_daten)
        stand_unsicherheit_temp = math.sqrt((berechne_sensitivität_temp_spannung(emp_mittelwert_temp_spannung)*stand_unsicherheit_temp_spannung)**2)
        print(datei)
        print(f"Temperatur: {emp_mittelwert_temp}°C +- {stand_unsicherheit_temp}°C")

        emp_mittelwert_luft_spannung = berechne_mittelwert(luftfeucht_spannung_daten)
        stand_unsicherheit_luft_spannung = berechne_standardunsicherheit(luftfeucht_spannung_daten, emp_mittelwert_luft_spannung) + unsicherheit_quantisierungsabweichung

        emp_mittelwert_luft = berechne_mittelwert(luftfeucht_daten)
        stand_unsicherheit_luft = math.sqrt((berechne_sensitivität_luft_spannung(emp_mittelwert_temp)*stand_unsicherheit_luft_spannung)**2+(berechne_sensitivitaet_temperatur(emp_mittelwert_luft_spannung,emp_mittelwert_temp)*stand_unsicherheit_temp)**2)
        abs_luftfeuchtigkeit =(((emp_mittelwert_luft /100)*611.2*math.exp((17.62*emp_mittelwert_temp)/(243.12+emp_mittelwert_temp))) / (461.52 * (emp_mittelwert_temp + 273.15)))

        print(f"Luftfeuchtigkeit: {abs_luftfeuchtigkeit*1000} +- {stand_unsicherheit_luft*1000} g/m^3\n")
        """Ausgabe:
        messwerteBalkonAbends.csv
Temperatur: 20.342299999999994°C +- 0.07309262621757005°C
Luftfeuchtigkeit: 11.545248841333246 +- 0.19607569970333943 g/m^3

messwerteBadezimmer.csv
Temperatur: 26.1621°C +- 0.04955101607608616°C
Luftfeuchtigkeit: 14.408344154752761 +- 0.10225286265891544 g/m^3

messwerteWohnzimmer.csv
Temperatur: 29.423°C +- 0.036596187626373386°C
Luftfeuchtigkeit: 11.639973577964165 +- 0.1201077272600597 g/m^3

messwerteBalkonMittags.csv
Temperatur: 31.530099999999997°C +- 0.278247708061568°C
Luftfeuchtigkeit: 8.681947347560062 +- 0.3779761716632471 g/m^3

messwerteKeller.csv
Temperatur: 25.265200000000018°C +- 0.01367696464327486°C
Luftfeuchtigkeit: 10.477343554729334 +- 0.03974406122723891 g/m^3"""