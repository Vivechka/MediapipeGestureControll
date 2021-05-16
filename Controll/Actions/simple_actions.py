import serial

def low_light():
    serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialPort.write(str.encode('10\n'))
    print("Low light enabled!")
    
def bright_light():
    serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialPort.write(str.encode('255\n'))
    print("Bright light enabled!")
    
def disable_light():
    serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialPort.write(str.encode('00\n'))
    print("Light disabled!")