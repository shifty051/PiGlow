#############################
# Calm LED effect for piglow
# shifty051
#############################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.red(5)
  sleep(2)
  
  piglow.orange(5)
  sleep(2)
  
  piglow.yellow(5)
  sleep(2)
  
  piglow.green(5)
  sleep(2)
  
  piglow.blue(5)
  sleep(2)
  
  piglow.white(5)
  sleep(2)
  
  piglow.blue(0)
  sleep(2)
  
  piglow.green(0)
  sleep(2)
  
  piglow.yellow(0)
  sleep(2)
  
  piglow.orange(0)
  sleep(2)
  
  piglow.red(0)
  sleep(2)
  
  
