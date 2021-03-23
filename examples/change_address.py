from mb7040 import MB7040

ultrasonic = MB7040()

ultrasonic.changeAddress(0x10)

print('Sensor is now on address', hex(ultrasonic.address >> 1))
