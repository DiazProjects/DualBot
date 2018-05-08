# DualBot
#-------------------------------------------------------------------------------Titulo: Car with Raspberry Pi 3 y PWM
#--Description: Estas lineas de codigo nos permiten controlar el carrito con ci-
#               erto tiempo (Un delay)
#-------------------------------------------------------------------------------Librerias
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
#-------------------------------------------------------------------------------Otras definciones
GPIO.setmode(GPIO.BCM)
                                                                                #--Aqui se declaran los pines utilizados como referencia para controlar el robot--#
pins = {
    18 : {'name' : '30 cm', 'state' : GPIO.LOW},
    23 : {'name' : '50 cm', 'state' : GPIO.LOW},
    24 : {'name' : 'Back', 'state' : GPIO.LOW},
    25 : {'name' : 'Right >>', 'state' : GPIO.LOW},
    26 : {'name' : '<< Left', 'state' : GPIO.LOW},
    12 : {'name' : 'LED', 'state' : GPIO.LOW}
   }
                                                                                #--Aqui inicializo todos los pines a utilizar--#
for pin in pins:
                                                                                #--Pines de Referencia--#
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.LOW)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.LOW)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, GPIO.LOW)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.LOW)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
                                                                                #--Pines PWM--#
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, GPIO.LOW)
                                                                                #--Aqui definimos los pines PWM a usar--#
pwm1 = GPIO.PWM(4,100)
pwm2 = GPIO.PWM(17,100)
pwm3 = GPIO.PWM(27,100)
pwm4 = GPIO.PWM(22,100)
#-------------------------------------------------------------------------------Deficiones (DEF)
@app.route("/")
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    templateData = {
        'pins' : pins
        }
    return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
    changePin = int(changePin)
    deviceName = pins[changePin]['name']
    if action == "on":
        if (deviceName == "30 cm"):                                             #--Me muevo hacia adelante 30 centimetros--#
            GPIO.output(changePin, GPIO.HIGH)
            pwm1.start(0)
            pwm2.start(70)
            pwm3.start(0)
            pwm4.start(75)
            time.sleep(0.5)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            pwm1.stop()
            pwm2.stop()
            pwm3.stop()
            pwm4.stop()
            GPIO.output(changePin, GPIO.LOW)
            message = "You advance " + deviceName
        if (deviceName == "50 cm"):                                             #--Me muevo hacia adelante 50 centimetros--#
            GPIO.output(changePin, GPIO.HIGH)
            pwm1.start(0)
            pwm2.start(90)
            pwm3.start(0)
            pwm4.start(65)
            time.sleep(1.7)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            pwm1.stop()
            pwm2.stop()
            pwm3.stop()
            pwm4.stop()
            GPIO.output(changePin, GPIO.LOW)
            message = "You advance " + deviceName
        elif (deviceName == "Back"):                                            #--Me muevo hacia atras--#
            GPIO.output(changePin, GPIO.HIGH)
            pwm1.start(70)
            pwm2.start(0)
            pwm3.start(70)
            pwm4.start(0)
            time.sleep(0.5)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            pwm1.stop()
            pwm2.stop()
            pwm3.stop()
            pwm4.stop()
            GPIO.output(changePin, GPIO.LOW)
            message = "You went " + deviceName
        elif (deviceName == "Right >>"):                                        #--Giro a la derecha--#
            GPIO.output(changePin, GPIO.HIGH)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(70)
            pwm4.start(0)
            time.sleep(0.4)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            pwm1.stop()
            pwm2.stop()
            pwm3.stop()
            pwm4.stop()
            GPIO.output(changePin, GPIO.LOW)
            message = "You moved to the " + deviceName
        elif (deviceName == "<< Left"):                                         #--Giro a la izquierda--#
            GPIO.output(changePin, GPIO.HIGH)
            pwm1.start(70)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            time.sleep(0.4)
            pwm1.start(0)
            pwm2.start(0)
            pwm3.start(0)
            pwm4.start(0)
            pwm1.stop()
            pwm2.stop()
            pwm3.stop()
            pwm4.stop()
            GPIO.output(changePin, GPIO.LOW)
            message = "You moved to the " + deviceName
        elif (deviceName == "LED"):                                             #--Enciendo un led--#
            GPIO.output(changePin, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            message = "Encendio " + deviceName
    if action == "off":                                                         #--Apago especificamente el led que encendi--#
        GPIO.output(changePin, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        message = "Unemployed"
    if action == "toggle":
        GPIO.output(changePin,not GPIO.input(changePin))
        message = "Toggled " + deviceName + "."

    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    templateData = {
        'message' : message,
        'pins' : pins
    }

    return render_template('main.html', **templateData)

#-------------------------------------------------------------------------------El MAIN
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

