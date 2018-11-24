import RPi.GPIO as GPIO
import dht11
from time import sleep
import paho.mqtt.publish as publish

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

dht = dht11.DHT11(pin = 24)

mqttHost = "mqtt.thingspeak.com"
channelID = "your channelID"
apiKey = "your apiKey"
tTransport = "websockets"
tPort = 80
tTLS = None
topic = "channels/" + channelID + "/publish/" + apiKey

def getSensorData():    
    r = dht.read()
    if r.is_valid():
        return(str(r.temperature), str(r.humidity))
    else:
        return(str(-1), str(-1))
   
while True:
    try:
        T, RH = getSensorData()
        print(T, RH)
        if T != '-1' and RH != '-1':
            tPayload = "field1=" + T + "&field2=" + RH            
            publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
            sleep(15)
        else:
            sleep(1)
    except:
        print('Error...')
        break       	  
		
