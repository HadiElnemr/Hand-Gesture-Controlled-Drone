import serial
import time

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
