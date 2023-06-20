import sys
import time
import random
from Adafruit_IO import MQTTClient
print("MQTT server")


AIO_USERNAME =  "votansang"
AIO_KEY = "aio_RLeh56n3hcao1wD5vg40ca9uIu0P"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("button1")
    client.subscribe("button2")


def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("sensor1", random.randint(0,40))
    client.publish("sensor2", random.randint(10,90))
    client.publish("sensor3", random.randint(10,90))
    pass