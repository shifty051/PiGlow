###############################################################
# Set the LEDs to turn on/off in pairs of 2 toward the centre
# shifty051
###############################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.red(1)
  sleep(0.1)
  
  piglow.red(2)
  sleep(0.1)
  
  piglow.red(3)
  piglow.orange(1)
  sleep(0.1)
  
  piglow.red(4)
  piglow.orange(2)
  sleep(0.1)
  
  piglow.red(3)
  piglow.orange(3)
  sleep(0.1)
  
  piglow.red(2)
  piglow.orange(4)
  sleep(0.1)
  
  piglow.red(1)
  piglow.orange(3)
  piglow.yellow(1)
  sleep(0.1)
  
  piglow.red(0)
  piglow.orange(2)
  piglow.yellow(2)
  sleep(0.1)
  
  piglow.orange(1)
  piglow.yellow(3)
  piglow.green(1)
  sleep(0.1)
  
  piglow.orange(0)
  piglow.yellow(4)
  piglow.green(2)
  sleep(0.1)
  
  piglow.yellow(3)
  piglow.green(3)
  sleep(0.1)
  
  piglow.yellow(2)
  piglow.green(4)
  sleep(0.1)
  
  piglow.yellow(1)
  piglow.green(3)
  piglow.blue(1)
  sleep(0.1)
  
  piglow.yellow(0)
  piglow.green(2)
  piglow.blue(2)
  sleep(0.1)
  
  piglow.green(1)
  piglow.blue(3)
  piglow.white(1)
  sleep(0.1)
  
  piglow.green(0)
  piglow.blue(4)
  piglow.white(2)
  sleep(0.1)
  
  piglow.blue(3)
  piglow.white(3)
  sleep(0.1)
  
  piglow.blue(2)
  piglow.white(4)
  sleep(0.1)
  
  piglow.blue(1)
  piglow.white(3)
  sleep(0.1)
  
  piglow.blue(0)
  piglow.white(2)
  sleep(0.1)
  
  piglow.white(1)
  sleep(0.1)
  
  piglow.white(0)
  sleep(0.1)
  
