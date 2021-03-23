from mb7040 import MB7040

ultrasonic = MB7040()

while True:

    distance = ultrasonic.readDistance()
    print(distance, 'cm', '\t\t',  round(distance * 0.39370,2),'in')
    # time.sleep(0.1)     # Can be commented out because of the sleep in readDistance()