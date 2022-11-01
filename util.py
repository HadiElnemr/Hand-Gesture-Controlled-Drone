import serial
import time
try:
    esp32 = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
except:
    pass
def write_esp(x):
    esp32.write(bytes(x, 'utf-8'))
