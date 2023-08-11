import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

broker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Subscriber")
client.connect(broker) 

client.loop_start()

client.subscribe("random/temperature")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()