#############################
# Set the LEDs to turn on/off in sequence piglow
# shifty051
#############################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.red(5)
  sleep(1)
  
  piglow.orange(5)
  sleep(1)
  
  piglow.yellow(5)
  sleep(1)
  
  piglow.green(5)
  sleep(1)
  
  piglow.blue(5)
  sleep(1)
  
  piglow.white(5)
  sleep(1)
  
  piglow.white(0)
  sleep(1)
  
  piglow.blue(0)
  sleep(1)
  
  piglow.green(0)
  sleep(1)
  
  piglow.yellow(0)
  sleep(1)
  
  piglow.orange(0)
  sleep(1)
  
  piglow.red(0)
  sleep(1)
  
  
