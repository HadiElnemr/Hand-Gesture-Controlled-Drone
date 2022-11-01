import serial
import time
# try:
esp32 = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
# except:
    # print('Connection with esp not found')

def write_esp(x):
    # try:
    esp32.write(bytes(x, 'utf-8'))
    # except:
    # print('Connection not found')