#!/usr/bin/python3

# Import external libraries
import time
from smbus2 import SMBus


class MB7040:

    def __init__(self, address=0x70, bus=3):

        self.bus = SMBus(bus)
        self.address = address
        self.distance = 0

        self.readDistance()

    def readDistance(self):

        self.bus.write_byte_data(0x70, 224, 81)
        # self.distance = self.bus.read_i2c_block_data(self.address, 225, 2)
        self.distance = self.bus.read_i2c_block_data(0x70, 225, 2)

        return self.distance

if __name__ == "__main__":

    ultrasonic = MB7040(bus=3)

    while True:

        print(ultrasonic.distance())
        time.sleep(0.1)