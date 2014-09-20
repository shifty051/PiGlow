###############################################################
# Set the LEDs to turn on/off in pairs of 2 toward the centre, 
# whilst increasing and decreasing in brightness
# shifty051
###############################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

piglow.all(0)

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
  
  
  piglow.led(1,1)
  sleep(0.1)
  
  piglow.led(1,2)
  sleep(0.1)
  
  piglow.led(1,3)
  piglow.led(7,1)
  sleep(0.1)
  
  piglow.led(1,4)
  piglow.led(7,2)
  sleep(0.1)
  
  piglow.led(1,3)
  piglow.led(7,3)
  piglow.led(12,1)
  sleep(0.1)
  
  piglow.led(1,2)
  piglow.led(7,4)
  piglow.led(12,2)
  sleep(0.1)
  
  piglow.led(1,1)
  piglow.led(7,3)
  piglow.led(12,3)
  sleep(0.1)
  
  piglow.led(1,0)
  piglow.led(7,2)
  piglow.led(12,4)
  sleep(0.1)
  
  
