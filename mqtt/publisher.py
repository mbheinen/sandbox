import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

broker = "mqtt.eclipseprojects.io" 

client = mqtt.Client("Publisher")
client.connect(broker) 

topic = "random/temperature"

while True:
    randNumber = uniform(65.0, 66.0)
    client.publish(topic, randNumber)
    print("Published " + str(randNumber) + " to topic " + topic)
    time.sleep(1)