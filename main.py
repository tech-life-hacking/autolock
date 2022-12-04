from state import Context
import threading
import pubsub
import udp

IPADDRESS = 'IPADDRESS'
PORT = 50100

context = Context()

def turn(state):
    context.change_state(state)
    context.turn()

event_channel = pubsub.EventChannel()
event_channel.subscribe("turn", turn)

def rfid():
    recv = udp.Receiver(IPADDRESS, PORT)
    while True:
        try:
            event = recv.receive()
            print(event)
            if event == 'Open':
                event_channel.publish("turn", "Open")
            if event == 'Close':
                event_channel.publish("turn", "Close")
        except KeyboardInterrupt:
            recv.close()
            break

def keyinput():
    while True:
        try:
            var = input()
            if var == "o":
                event_channel.publish("turn", "Open")
            elif var == "c":
                event_channel.publish("turn", "Close")
        except KeyboardInterrupt:
            break

event_channel.publish("turn", "Close")
th_rfid = threading.Thread(target=rfid)
th_key = threading.Thread(target=keyinput)
th_rfid.start()
th_key.start()