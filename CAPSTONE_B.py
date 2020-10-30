"""
Linear Actuators will be labeled as the following: A-B-C-D
A: Channels 7-8  Power: 6
B: Channels 1-2  Power: 3
C: Channels 15-16 Power:  14
D: Channels 9-10  Power: 11
8 positions: North will be in the AD side and so on
No matter what, channels 3-6-11-14 channels will turn on to operate
Always two pairs will be activated
When the function GPIO.OUT is written, the relay turns ON
GPIO.IN turns the relay off
"""
import RPi.GPIO as GPIO
import time


pinList = [2, 3, 4, 6, 7, 8, 9, 10, 11, 14, 15, 16]  # Relays
# GPIO 4 = RELAY 1; there is no GPIO 1
GPIO.setmode(GPIO.BCM)
"""for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, 1)  #GPIO.output( pin#, High/Low)"""

Chan_List_A = (7, 8)  # Linear Actuator A
Chan_List_B = (2, 3)  # Linear Actuator B #Relay 2-3
Chan_List_C = (14, 15)  # Linear Actuator C
Chan_List_D = (9, 10)  # Linear Actuator D

Chan_List_ON = (4, 6, 11, 16)  # All Linear Actuators Switches #relay 1-6-11-16

Chan_List_ALL = pinList

# Chan_List_ALL = (2, 3, 4, 6, 7, 8, 9, 10, 11, 14, 15, 16)


def Move(Direction):

    # GPIO.OUT = ON
    # GPIO.IN = OFF

    # Variable Declaration
    North = "N"  # Linear Actuator A-D
    South = "S"  # Linear Actuator B-C
    East = "E"  # Linear Actuator A-B
    West = "W"  # Linear Actuator D-C

    North_East = "NE"  # Linear Actuator A
    North_West = "NW"  # Linear Actuator D
    South_East = "SE"  # Linear Actuator B
    South_West = "SW"  # Linear Actuator C

    # Time Delay
    Reset = 6
    Switch_ON = 0.25
    ON = 4
    Corner = 1
    Corner_ON = 2.5

    """Before executing any direction, the pannel will reset at the bottom"""
    # Reset position

    GPIO.setup(Chan_List_ON, GPIO.OUT)
    time.sleep(Reset)
    print("Reset")
    GPIO.setup(Chan_List_ON, GPIO.IN)
    time.sleep(1)
    print(Direction)

    # Moving the panel
    if Direction == North:

        # Retract
        GPIO.setup(Chan_List_A, GPIO.OUT)
        GPIO.setup(Chan_List_D, GPIO.OUT)
        # Extend
        GPIO.setup(Chan_List_B, GPIO.IN)
        GPIO.setup(Chan_List_C, GPIO.IN)
        time.sleep(Switch_ON)
        # Closed the circuit
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        # Delay
        time.sleep(ON)

        return GPIO.setup(pinList, GPIO.IN)

    if Direction == South:

        # Retract
        GPIO.setup(Chan_List_B, GPIO.OUT)
        GPIO.setup(Chan_List_C, GPIO.OUT)
        # Extend
        GPIO.setup(Chan_List_A, GPIO.IN)
        GPIO.setup(Chan_List_D, GPIO.IN)
        time.sleep(Switch_ON)
        # Closed the circuit
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        # Delay
        time.sleep(ON)
        return GPIO.setup(pinList, GPIO.IN)

    if Direction == East:

        # Retract
        GPIO.setup(Chan_List_A, GPIO.OUT)
        GPIO.setup(Chan_List_B, GPIO.OUT)
        # Extend
        GPIO.setup(Chan_List_D, GPIO.IN)
        GPIO.setup(Chan_List_C, GPIO.IN)
        time.sleep(Switch_ON)
        # Closed the circuit
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        # Delay
        time.sleep(ON)

        return GPIO.setup(pinList, GPIO.IN)

    if Direction == West:

        # Retract
        GPIO.setup(Chan_List_C, GPIO.OUT)
        GPIO.setup(Chan_List_D, GPIO.OUT)
        # Extend
        GPIO.setup(Chan_List_B, GPIO.IN)
        GPIO.setup(Chan_List_A, GPIO.IN)
        time.sleep(Switch_ON)
        # Closed the circuit
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        # Delay
        time.sleep(ON)

        return GPIO.setup(pinList, GPIO.IN)

    # Corner Positions
    if Direction == North_East:
        # Retract
        GPIO.setup(Chan_List_A, GPIO.IN)
        GPIO.setup(Chan_List_C, GPIO.OUT)
        time.sleep(Switch_ON)
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        time.sleep(Corner)
        GPIO.setup(Chan_List_B, GPIO.OUT)
        time.sleep(Corner)
        GPIO.setup(Chan_List_D, GPIO.OUT)
        time.sleep(Corner_ON)

        return GPIO.setup(pinList, GPIO.IN)

    if Direction == North_West:
        # Retract
        GPIO.setup(Chan_List_D, GPIO.IN)
        GPIO.setup(Chan_List_B, GPIO.OUT)
        time.sleep(Switch_ON)
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        time.sleep(Corner)
        GPIO.setup(Chan_List_C, GPIO.OUT)
        time.sleep(Corner)
        GPIO.setup(Chan_List_A, GPIO.OUT)
        time.sleep(Corner_ON)

        return GPIO.setup(pinList, GPIO.IN)

    if Direction == South_East:
        # Retract
        GPIO.setup(Chan_List_B, GPIO.IN)
        GPIO.setup(Chan_List_D, GPIO.OUT)
        time.sleep(Switch_ON)
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        time.sleep(Corner)
        GPIO.setup(Chan_List_A, GPIO.OUT)
        time.sleep(Corner)
        GPIO.setup(Chan_List_C, GPIO.OUT)
        time.sleep(Corner_ON)

        return GPIO.setup(pinList, GPIO.IN)

    if Direction == South_West:
        # Retract
        GPIO.setup(Chan_List_C, GPIO.IN)
        GPIO.setup(Chan_List_A, GPIO.OUT)
        time.sleep(Switch_ON)
        GPIO.setup(Chan_List_ON, GPIO.OUT)

        time.sleep(Corner)
        GPIO.setup(Chan_List_D, GPIO.OUT)
        time.sleep(Corner)
        GPIO.setup(Chan_List_B, GPIO.OUT)
        time.sleep(Corner_ON)

        return GPIO.setup(pinList, GPIO.IN)


def main():
    # Variable Declaration
    North = "N"  # Linear Actuator A-D
    South = "S"  # Linear Actuator B-C
    East = "E"  # Linear Actuator A-B
    West = "W"  # Linear Actuator D-C

    North_East = "NE"  # Linear Actuator A
    North_West = "NW"  # Linear Actuator D
    South_East = "SE"  # Linear Actuator B
    South_West = "SW"  # Linear Actuator C

    # Test Move function
    List = ["N", "S", "W", "E", "NE", "NW", "SE", "SW"]
    for i in List:
        Move(i)
    GPIO.cleanup()


main()
