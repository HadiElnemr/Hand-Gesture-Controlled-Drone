import serial

esp32 = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def write_esp(x):
    #esp32.write(bytes(str(x), 'utf-8'))
    
