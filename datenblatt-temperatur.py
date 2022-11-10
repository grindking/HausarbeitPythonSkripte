import math

temperaturwerte = [20,26,29,32,25] #Mittelwerte der Temperatur, gerundet
r_ntc_norm = [12150.5, 9624.8,8593.4,7688.2,10000.0] #Aus dem Datenblatt entnommen
r_ntc_max = [12296.0, 9724.8,8692.5,7785.5,10100.0]#Aus dem Datenblatt entnommen
r_ntc_min = [12005.6,9524.9,8494.6,7591.3,9900.0]#Aus dem Datenblatt entnommen
result_norm = []
result_max = []

unsicherheiten = []
unsicherheiten_ausgangsgroeße = []


#Berechnung der Standardunsicherheiten
for index in range(0,5):

    unsicherheiten.append((r_ntc_max[index] - r_ntc_min[index]) / math.sqrt(3))

#Funktion zur Berechnung der Sensitivität
def berechne_sensitivität(widerstand):
    return (3*0.0000000803*math.pow(math.log(widerstand), 2) + 0.00027267) / (widerstand*(0.0000000803*math.pow(math.log(widerstand), 3)+0.00027267*math.log(widerstand)+0.0007799)**2)


for index in range(0,5):
    unsicherheiten_ausgangsgroeße.append(math.sqrt((berechne_sensitivität(r_ntc_norm[index])*unsicherheiten[index])**2))
    print(f"{temperaturwerte[index]}°C +- {unsicherheiten_ausgangsgroeße[index]}°C")


"""Ausgabe:
20°C +- 0.348613196257399°C
26°C +- 0.3143462513077727°C
29°C +- 0.3549708217424341°C
32°C +- 0.39645750138929525°C
25°C +- 0.30085788991819395°C"""
