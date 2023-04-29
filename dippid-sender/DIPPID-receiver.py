from DIPPID import SensorUDP

'''
this file is just for testing DIPPID-sender.py
'''

PORT = 5700
sensor = SensorUDP(PORT)


def handle_acc(data):
    acc_x = float(data['x'])
    acc_y = float(data['y'])
    acc_z = float(data['z'])
    print(f'x: {acc_x}, y: {acc_y}, z: {acc_z}')


def handle_btn(data):
    btn_state = data['state']
    print(f'button1: {btn_state}')


sensor.register_callback('accelerometer', handle_acc)
sensor.register_callback('button1', handle_btn)
