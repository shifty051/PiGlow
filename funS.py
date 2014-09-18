##################################################################
# A fun set of patterns that progress sequentially
# shifty051
##################################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.led(1,1)
  piglow.led(18,0)
  sleep(0.05)
  
  piglow.led(1,2)
  sleep(0.05)
  
  piglow.led(1,3)
  sleep(0.05)
  
  piglow.led(1,4)
  sleep(0.05)
  
  piglow.led(1,3)
  sleep(0.05)
  
  piglow.led(1,2)
  piglow.led(7,1)
  sleep(0.05)
  
  piglow.led(1,1)
  piglow.led(7,2)
  sleep(0.05)

  piglow.led(1,0)
  piglow.led(7,2)
  sleep(0.05)
  
  piglow.led(7,3)
  sleep(0.05)
  
  piglow.led(7,4)
  sleep(0.05)
  
  piglow.led(7,3)
  sleep(0.05)

  piglow.led(7,2)
  piglow.led(13,1)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(13,2)
  sleep(0.05)
  
  piglow.led(7,0)
  piglow.led(13,3)
  sleep(0.05)
  
  piglow.led(13,4)
  sleep(0.05)
  
  piglow.led(13,3)
  sleep(0.05)
  
  piglow.led(13,2)
  piglow.led(2,1)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(2,2)
  sleep(0.05)
  
  piglow.led(13,0)
  piglow.led(2,3)
  sleep(0.05)
  
  piglow.led(2,4)
  sleep(0.05)
  
  piglow.led(2,3)
  sleep(0.05)
  
  piglow.led(2,2)
  piglow.led(8,1)
  sleep(0.05)
  
  piglow.led(2,1)
  piglow.led(8,2)
  sleep(0.05)
  
  piglow.led(2,0)
  piglow.led(8,3)
  sleep(0.05)
  
  piglow.led(8,4)
  sleep(0.05)
  
  piglow.led(8,3)
  sleep(0.05)
  
  piglow.led(8,2)
  piglow.led(14,1)
  sleep(0.05)
  
  piglow.led(8,1)
  piglow.led(14,2)
  sleep(0.05)
  
  piglow.led(8,0)
  piglow.led(14,3)
  sleep(0.05)
  
  piglow.led(14,4)
  sleep(0.05)

  piglow.led(14,3)
  sleep(0.05)
  
  piglow.led(14,2)
  sleep(0.05)
  
  
  
  
  
  
  
  piglow.led(14,1)
  piglow.led(8,0)
  sleep(0.1)

  piglow.led(3,1)
  piglow.led(14,0)
  sleep(0.1)

  piglow.led(9,1)
  piglow.led(3,0)
  sleep(0.1)

  piglow.led(15,1)
  piglow.led(9,0)
  sleep(0.1)

  piglow.led(4,1)
  piglow.led(15,0)
  sleep(0.1)

  piglow.led(10,1)
  piglow.led(4,0)
  sleep(0.1)

  piglow.led(16,1)
  piglow.led(10,0)
  sleep(0.1)

  piglow.led(5,1)
  piglow.led(16,0)
  sleep(0.1)

  piglow.led(11,1)
  piglow.led(5,0)
  sleep(0.1)

  piglow.led(17,1)
  piglow.led(11,0)
  sleep(0.1)

  piglow.led(6,1)
  piglow.led(17,0)
  sleep(0.1)

  piglow.led(12,1)
  piglow.led(6,0)
  sleep(0.1)

  piglow.led(18,1)
  piglow.led(12,0)
  sleep(0.1)
