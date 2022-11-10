import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import csv
import datetime
import random
import math

time.sleep(5)

i2c = busio.I2C(board.SCL,board.SDA)
#Initialisierung AD-Wandler
ads = ADS.ADS1115(i2c)
#Setzen der Eingänge des AD-Wandlers
chan = AnalogIn(ads,ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)
#PGA, 2/3 = +- 6,144V 1bit = 0,1875mV
ads.gain = 2/3

filename = '/home/pi/Documents/Skripte/' + 'messwerte' + str(random.randint(1,10000)) + '.csv'
header_csv = ['messwert','SpannungLuft', 'SpannungTemp','LuftfeuchtigkeitRel', 'Temperatur']
file = open(filename, 'w')

writer = csv.writer(file)
writer.writerow(header_csv)

print(f'{chan.voltage}')
time.sleep(2)
print(f'{chan2.voltage}')
time.sleep(2)
    
for value in range(1,101):
    new_row = [value, round(chan.voltage,3), round(chan2.voltage,3), round(chan.voltage / 0.03, 2)]
    
    r_ntc = ((5.19 - chan2.voltage) / chan2.voltage)  * 5100
        
    #Steinhart-hart equation
    temp_kelvin = 1 / ( 0.0007799 + 0.00027267* math.log(r_ntc) + 0.0000000803 * math.pow(math.log(r_ntc), 3))
    temp_celsius = temp_kelvin - 273.15

    new_row.append(round(temp_celsius, 2))
    
    writer.writerow(new_row)
    
    time.sleep(60)
    
    
    

file.close()