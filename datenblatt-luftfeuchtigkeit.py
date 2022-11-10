import math

####Dieses Skript berechnet die Standardabweichung der absoluten Luftfeuchtigkeit mit den Daten aus dem Datenblatt des Sensors####

rel_luftfeuchtigkeit = [0.66,0.59,0.40,0.26,0.45]
abs_luftfeuchtigkeit = []
temperaturwerte = [20,26,29,32,25]

unsicherheit_rh = 0.02 / math.sqrt(3)
unsicherheiten_temperatur = [0.348613196257399, 0.3143462513077727, 0.3549708217424341, 0.39645750138929525, 0.30085788991819395]

luftfeuchtigkeit_sensitivitaeten = []
temperatur_sensitivitaeten = []
komb_unsicherheiten = []
def berechne_sensitivitaet_rel_luftfeuchtigkeit(temperatur):
    return (611.2*math.exp((17.62*temperatur)/(243.12+temperatur))) / (461.52*(273.15+temperatur))

for index in range(0,5):
    luftfeuchtigkeit_sensitivitaeten.append(berechne_sensitivitaet_rel_luftfeuchtigkeit(temperaturwerte[index]))


def berechne_sensitivitaet_temperatur(luftfeuchtigkeit, temperatur):
    return (611.2*luftfeuchtigkeit *math.exp((17.62*temperatur)/(243.12+temperatur))*(math.pow(temperatur,2) + (2 - 17.62)*243.12*temperatur-17.62*243.12*273.15+ (243.12**2))) / (461.52*((temperatur+243.12)**2)*((temperatur+273.15)**2))

for index in range(0,5):
    temperatur_sensitivitaeten.append(berechne_sensitivitaet_temperatur(rel_luftfeuchtigkeit[index],temperaturwerte[index]))

for index in range(0,5):
    komb_unsicherheiten.append(math.sqrt((luftfeuchtigkeit_sensitivitaeten[index]*unsicherheit_rh)**2+(temperatur_sensitivitaeten[index]*unsicherheiten_temperatur[index])**2))

for index in range(0,5):
    abs_luftfeuchtigkeit.append((rel_luftfeuchtigkeit[index]*611.2*math.exp((17.62*temperaturwerte[index])/(243.12+temperaturwerte[index]))) / (461.52 * (temperaturwerte[index] + 273.15)))

    print(f"{abs_luftfeuchtigkeit[index]*1000}g/m^3 +- {komb_unsicherheiten[index]*1000} g/m^3")

"""Ausgabe:
11.378972339858509g/m^3 +- 0.3056464277577874 g/m^3
14.33014279720327g/m^3 +- 0.3766267745373669 g/m^3
11.464030183871987g/m^3 +- 0.39847304283433066 g/m^3
8.760123426486896g/m^3 +- 0.4308719130938288 g/m^3
10.33432413458244g/m^3 +- 0.31763261343035454 g/m^3"""