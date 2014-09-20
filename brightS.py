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
  
  piglow.led(7,3)
  piglow.led(13,1)
  sleep(0.1)
  
  piglow.led(7,4)
  piglow.led(13,2)
  sleep(0.1)
  
  piglow.led(13,3)
  piglow.led(2,1)
  sleep(0.1)
  
  piglow.led(13,4)
  piglow.led(2,2)
  sleep(0.1)
  
  piglow.led(2,3)
  piglow.led(8,1)
  sleep(0.1)
  
  piglow.led(2,4)
  piglow.led(8,2)
  sleep(0.1)
  
  piglow.led(8,3)
  piglow.led(14,1)
  sleep(0.1)
  
  piglow.led(8,4)
  piglow.led(14,2)
  sleep(0.1)
  
  piglow.led(14,3)
  piglow.led(3,1)
  sleep(0.1)
  
  piglow.led(14,4)
  piglow.led(3,2)
  sleep(0.1)
  
  piglow.led(3,3)
  piglow.led(9,1)
  sleep(0.1)
  
  piglow.led(3,4)
  piglow.led(9,2)
  sleep(0.1)
  
  piglow.led(9,3)
  piglow.led(15,1)
  sleep(0.1)
  
  piglow.led(9,4)
  piglow.led(15,2)
  sleep(0.1)
  
  piglow.led(15,3)
  piglow.led(4,1)
  sleep(0.1)
  
  piglow.led(15,4)
  piglow.led(4,2)
  sleep(0.1)
  
  piglow.led(4,3)
  piglow.led(10,1)
  sleep(0.1)
  
  piglow.led(4,4)
  piglow.led(10,2)
  sleep(0.1)
  
  piglow.led(10,3)
  piglow.led(16,1)
  sleep(0.1)
  
  piglow.led(10,4)
  piglow.led(16,2)
  sleep(0.1)
  
  piglow.led(16,3)
  piglow.led(5,1)
  sleep(0.1)
  
  piglow.led(16,4)
  piglow.led(5,2)
  sleep(0.1)
  
  piglow.led(5,3)
  piglow.led(11,1)
  sleep(0.1)
  
  piglow.led(5,4)
  piglow.led(11,2)
  sleep(0.1)
  
  piglow.led(11,3)
  piglow.led(17,1)
  sleep(0.1)
  
  piglow.led(11,4)
  piglow.led(17,2)
  sleep(0.1)
  
  piglow.led(17,3)
  piglow.led(6,1)
  sleep(0.1)
  
  piglow.led(17,4)
  piglow.led(6,2)
  sleep(0.1)
  
  piglow.led(6,3)
  piglow.led(12,1)
  sleep(0.1)
  
  piglow.led(6,4)
  piglow.led(12,2)
  sleep(0.1)
  
  piglow.led(12,3)
  piglow.led(18,1)
  sleep(0.1)
  
  piglow.led(12,4)
  piglow.led(18,2)
  sleep(0.1)
  
  piglow.led(18,3)
  sleep(0.1)
  
  piglow.led(18,4)
  sleep(0.1)
  
  
  piglow.all(4)
  sleep(0.1)
  
  piglow.all(3)
  sleep(0.1)
  
  piglow.all(2)
  sleep(0.1)
  
  piglow.all(1)
  sleep(0.1)
  
  piglow.all(0)
  sleep(1)
  
  piglow.arm1(1)
  sleep(0.1)
  
  piglow.arm1(2)
  sleep(0.1)
  
  piglow.arm1(3)
  piglow.arm2(1)
  sleep(0.1)
  
  piglow.arm1(2)
  piglow.arm2(2)
  sleep(0.1)
  
  piglow.arm1(1)
  piglow.arm2(3)
  piglow.arm3(1)
  sleep(0.1)
  
  piglow.arm1(0)
  piglow.arm2(2)
  piglow.arm3(2)
  sleep(0.1)
  
  piglow.arm2(1)
  piglow.arm3(3)
  sleep(0.1)
  
  piglow.arm2(0)
  piglow.arm3(2)
  sleep(0.1)
  
  
  
  
  
  
  
  
  
