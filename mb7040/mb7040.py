#!/usr/bin/python3

# Import external libraries
import time
from smbus2 import SMBus


class MB7040:

    def __init__(self, address=0x70, bus=1):

        self.bus = SMBus(bus)
        self.address = address
        self.distance = 0

        self.readDistance()

    def readDistance(self):

        # Take a range reading
        self.bus.write_byte_data(self.address, 224, 81)

        # Wait 100ms for the range to be recorded and written (80ms min, 100ms recommended)
        time.sleep(0.1)

        # Report the last range value
        distance = self.bus.read_i2c_block_data(self.address, 225, 2)

        # Distance is a list of 2 bytes [MSB, LSB]
        # Shift MSB to left 8 bits and add LSB.
        self.distance = distance[1] + (distance[0] << 8)

        # Return distance
        return self.distance

if __name__ == "__main__":

    # Create ultrasonic sensor object
    ultrasonic = MB7040()

    while True:

        # Read distance from ultrasonic sensor
        distance = ultrasonic.readDistance()

        # Print out distance value (already in cm), and in inches by converting.
        print(distance, 'cm', '\t',  round(distance * 0.39370,2),'in')

        # Sleep
        # time.sleep(0.1)     # Can be commented out because of the sleep in readDistance()