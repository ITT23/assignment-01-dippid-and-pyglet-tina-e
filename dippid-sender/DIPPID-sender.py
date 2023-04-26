import socket
import time
import math
import random

IP = '127.0.0.1'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def simulate_accelerometer():
    for i in range(-5, 5):
        x = 0.5 * math.sin(i)
        y = math.sin(0.2 * i)
        z = math.sin(i) + 2
        message_acc = '{"accelerometer" : ' + f'{{"x":{x},"y":{y},"z":{z}}}' + '}'
        sock.sendto(message_acc.encode(), (IP, PORT))
        time.sleep(0.1)


def simulate_button1():
    random_btn_state = random.randint(0, 5)
    message_btn = None
    if random_btn_state > 2:
        return
    elif random_btn_state == 0:
        message_btn = '{"button1" : {"state" : "btn_down"}}'
    elif random_btn_state == 1:
        message_btn = '{"button1" : {"state" : "btn_pressed"}}'
    elif random_btn_state == 2:
        message_btn = '{"button1" : {"state" : "btn_up"}}'
    sock.sendto(message_btn.encode(), (IP, PORT))
    time.sleep(0.5)


while True:
    simulate_accelerometer()
    simulate_button1()

