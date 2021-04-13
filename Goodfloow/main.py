import time
from machine import I2C
from machine import Pin
# #Classe a créer à coté ou importer le driver
# import sensorName
import numpy as np
import pandas as pd

#Usefull link
#https://docs.micropython.org/en/latest/library/machine.html
#https://readthedocs.org/projects/micropython-pfalcon/downloads/pdf/latest/

# i2c = I2C(0, I2C.MASTER, baudrate=100000)
# sensor = sensorName.SENSORNAME(i2c, addr=i2c.scan()[0])
# #Le pin est à définir
# #Doc : https://docs.micropython.org/en/latest/library/pyb.Pin.html
# #TODO

wakePin = Pin(14, mode = Pin.OUT)
wakePin = Pin.low()


#En attendant on fournis les données via un fichier.csv
donnees_data_frame = pd.read_csv ('data/collecte_IoT.csv', delimiter=";")

# extraction des données du data frame
donnees_ensemble_total = donnees_data_frame.values

# mélange du tableau numpy  (mélange des lignes)
#np.random.shuffle(donnees_ensemble_total)

print (donnees_ensemble_total)
nombre_lignes_base=donnees_ensemble_total.shape[0]
nombre_colonnes_base=donnees_ensemble_total.shape[1]

accel_x = donnees_ensemble_total[:,4]
accel_y = donnees_ensemble_total[:,5]
accel_z = donnees_ensemble_total[:,6]
print("x :\n")
print(accel_x)
i = 0
while(True):
        data = accel_x[i]
        print(data)
        #Lecture des données de l'accéléromètre
        #TODO
        time.sleep(10)
        i = i +1

    #Condition à définir
    #TODO
    if accel_x > 10 :
        #Wake up du reste des composants
        #TODO
        wakePin.high()









