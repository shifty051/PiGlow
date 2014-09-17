###############################################################
# Set the LEDs to turn on/off sequentially in a spiral fashion toward the centre
# This is a modified version of 'spiralS.py', where the LEDs remain on throughout the cycle.
# shifty051
###############################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.led(1,1)
  sleep(0.1)

  piglow.led(7,1)
  sleep(0.1)

  piglow.led(13,1)
  sleep(0.1)

  piglow.led(2,1)
  sleep(0.1)

  piglow.led(8,1)
  sleep(0.1)

  piglow.led(14,1)
  sleep(0.1)

  piglow.led(3,1)
  sleep(0.1)

  piglow.led(9,1)
  sleep(0.1)

  piglow.led(15,1)
  sleep(0.1)

  piglow.led(4,1)
  sleep(0.1)

  piglow.led(10,1)
  sleep(0.1)

  piglow.led(16,1)
  sleep(0.1)

  piglow.led(5,1)
  sleep(0.1)

  piglow.led(11,1)
  sleep(0.1)

  piglow.led(17,1)
  sleep(0.1)

  piglow.led(6,1)
  sleep(0.1)

  piglow.led(12,1)
  sleep(0.1)

  piglow.led(18,1)
  sleep(0.1)
  
  piglow.led1-led18(0)
  sleep(0.1)
