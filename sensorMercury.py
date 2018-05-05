# DualBot
#-------------------------------------------------------------------------------Title: Distance sensor with Arduino
#--Description: Este codigo permite imprimir la distancia que se esta midiendo -
#               con el sensor de distancia la imprime en centimetros
#-------------------------------------------------------------------------------Libraries
import serial, time
#-------------------------------------------------------------------------------Other definitions
Arduino=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=5)
Arduino.flushInput()
#-------------------------------------------------------------------------------Definitions (DEF)
def separar(data):
    if "Distancia" in data:
        label = data.split(":")
        dist = float(label[1])
        print "Distancia US: " + str(dist)
#-------------------------------------------------------------------------------The MAIN
if __name__ == "__main__":
    print('Inicializando Sensor ... ')
    while(True):
        try:
                data_Arduino=Arduino.readline()
                separar(data_Arduino)
        except KeyboardInterrupt:
                print "Algo va mal :( "
                break

