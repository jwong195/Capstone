'''
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
'''
import RPi.GPIO as GPIO
import time


pinList = [1, 2, 3, 6, 7, 8, 9, 10, 11, 14, 15, 16] #Relays

GPIO.setmode(GPIO.BCM)
'''for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, 1)  #GPIO.output( pin#, High/Low)'''

Chan_List_A = (7, 8)         #Linear Actuator A 
Chan_List_B = (1, 2)         #Linear Actuator B
Chan_List_C = (15, 16)       #Linear Actuator C
Chan_List_D = (9, 10)        #Linear Actuator D

Chan_List_ON = (3, 6, 11, 14)   #All Linear Actuators Switches

#Chan_List_ALL = (1, 2, 3, 6, 7, 8, 9, 10, 11, 14, 15, 16)

def Move(Direction):

    #Variable Declaration
    North = "N"     #Linear Actuator A-D
    South = "S"     #Linear Actuator B-C
    East = "E"      #Linear Actuator A-B
    West = "W"      #Linear Actuator D-C

    North_East = "NE"       #Linear Actuator A
    North_West = "NW"       #Linear Actuator D
    South_East = "SE"       #Linear Actuator B
    South_West = "SW"       #Linear Actuator C
   
    if Direction == North:

      #Retract
      GPIO.setup(Chan_List_A, GPIO.OUT)
      GPIO.setup(Chan_List_D, GPIO.OUT)
      #Extend
      GPIO.setup(Chan_List_B, GPIO.IN)
      GPIO.setup(Chan_List_C, GPIO.IN)
      time.sleep(1)

      #Closed the circuit
      GPIO.setup(Chan_List_ON, GPIO.OUT)

      #Delay
      time.sleep(4)

      return GPIO.output(pinList, GPIO.IN)

    if Direction == South:

      #Retract
      GPIO.setup(Chan_List_B, GPIO.OUT)
      GPIO.setup(Chan_List_C, GPIO.OUT)
      #Extend
      GPIO.setup(Chan_List_A, GPIO.IN)
      GPIO.setup(Chan_List_D, GPIO.IN)
      #Closed the circuit
      GPIO.setup(Chan_List_ON, GPIO.OUT)

      #Delay
      time.sleep(4)
      return GPIO.setup(pinList, GPIO.IN)

    if Direction == East:

      #Retract
      GPIO.setup(Chan_List_A, GPIO.OUT)
      GPIO.setup(Chan_List_B, GPIO.OUT)
      #Extend
      GPIO.setup(Chan_List_D, GPIO.IN)
      GPIO.setup(Chan_List_C, GPIO.IN)

      #Closed the circuit
      GPIO.setup(Chan_List_ON, GPIO.OUT)

      #Delay
      time.sleep(4)
      
      return GPIO.setup(pinList, GPIO.IN)

    if Direction == West:

      #Retract
      GPIO.setup(Chan_List_C, GPIO.OUT)
      GPIO.setup(Chan_List_D, GPIO.OUT)
      #Extend
      GPIO.setup(Chan_List_B, GPIO.IN)
      GPIO.setup(Chan_List_A, GPIO.IN)

      #Closed the circuit
      GPIO.setup(Chan_List_ON, GPIO.IN)

      #Delay
      time.sleep(4)

      return GPIO.setup(pinList, GPIO.IN)

'''
    #Corner Positions
    if Direction == North_East:
      #Retract
      GPIO.output(Chan_List_A, 0)

      #extent
      GPIO.output(Chan_List_C, 1)
      GPIO.output(Chan_List_B, 1)
      GPIO.output(Chan_List_D, 1)

      #Closed the circuit
      GPIO.output(Chan_List_ON, 1)

      time.sleep(4)
      
      return GPIO.output(pinList, 0)

    if Direction == North_West:
      
      return GPIO.output(pinList, 0)
    
    if Direction == South_East:
      
      return GPIO.output(pinList, 0)
    if Direction == South_West:
      
      return GPIO.output(pinList, 0)'''


def main():
  #Variable Declaration
  North = "N"     #Linear Actuator A-D
  South = "S"     #Linear Actuator B-C
  East = "E"      #Linear Actuator A-B
  West = "W"      #Linear Actuator D-C

  try:
    Move(North)
    time.sleep(2)
    Move(South)
    time.sleep(2)
    Move(West)
    time.sleep(2)
    Move(East)
#main()

    


# init list with pin numbers
'''
pinList = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(3, GPIO.LOW)
  print ("TWO")
  time.sleep(SleepTimeL);
  GPIO.output(4, GPIO.LOW)
  print ("THREE")
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  print ("FOUR")
  time.sleep(SleepTimeL);
  GPIO.output(27, GPIO.LOW)
  print ("FIVE")
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print ("SIX")
  time.sleep(SleepTimeL);
  GPIO.output(10, GPIO.LOW)
  print ("SEVEN")
  time.sleep(SleepTimeL);
  GPIO.output(9, GPIO.LOW)
  print ("EIGHT")
  time.sleep(SleepTimeL);
  GPIO.output(11, GPIO.LOW)
  print ("NINE")
  time.sleep(SleepTimeL);
  GPIO.output(5, GPIO.LOW)
  print ("TEN")
  time.sleep(SleepTimeL);
  GPIO.output(6, GPIO.LOW)
  print ("ELEVEN")
  time.sleep(SleepTimeL);
  GPIO.output(13, GPIO.LOW)
  print ("TWELVE")
  time.sleep(SleepTimeL);
  GPIO.output(19, GPIO.LOW)
  print ("THIRTEEN")
  time.sleep(SleepTimeL);
  GPIO.output(26, GPIO.LOW)
  print ("FOURTEEN")
  time.sleep(SleepTimeL);
  GPIO.output(21, GPIO.LOW)
  print ("FIFTEEN")
  time.sleep(SleepTimeL);
  GPIO.output(20, GPIO.LOW)
  print ("SIXTEEN")
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup() '''