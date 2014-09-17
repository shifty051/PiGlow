###############################################################
# Set the LEDs to turn on/off in pairs of 2 toward the centre
# shifty051
###############################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  
  piglow.orange(5)
  sleep(0.5)
  
  piglow.yellow(5)
  piglow.red(0)
  sleep(0.5)
  
  piglow.green(5)
  piglow.orange(0)
  sleep(0.5)
  
  piglow.blue(5)
  piglow.yellow(0)
  sleep(0.5)
  
  piglow.white(5)
  piglow.green(0)
  sleep(0.5)
  
  piglow.blue(0)
  sleep(0.5)
  
  piglow.white(0)
  piglow.red(5)
  sleep(0.5)
  
  
