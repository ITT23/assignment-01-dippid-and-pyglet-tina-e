from DIPPID import SensorUDP

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


def handle_acc(data):
    if sensor.has_capability('accelerometer'):
        acc_x = float(sensor.get_value('accelerometer')['x'])
        acc_y = float(sensor.get_value('accelerometer')['x'])
        acc_z = float(sensor.get_value('accelerometer')['z'])
        print(f'x: {acc_x}, y: {acc_y}, z: {acc_z}')


def handle_btn(data):
    if sensor.has_capability('button1'):
        btn_state = sensor.get_value('button1')['state']
        print(f'button1: {btn_state}')


sensor.register_callback('accelerometer', handle_acc)
sensor.register_callback('button1', handle_btn)
