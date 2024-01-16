import json
import sys
import paho.mqtt.client as paho


# callback for incoming MQTT Messages
def message_received(client, userdata, message):
    data = message.payload.decode("utf-8")
    print(json.loads(data))


# start the program
client_id = "SensorServer"
client = paho.Client(client_id)  # create new instance

try:
    client.connect("127.0.0.1", 1883)  # connect to broker
    client.subscribe("data/sensorclient")
except ConnectionRefusedError as cre:
    print("Verbindung verweigert")
    print("Exception: " + str(cre.__cause__))
    print("Class: " + str(cre.__class__))
    raise
except Exception as e:
    raise e


# start loop für  MQTT client
client.loop_start()  # start the loop

# callback for incoming MQTT Messages
client.on_message = message_received

while True:
    pass
