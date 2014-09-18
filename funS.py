########################################################################################
# A fun set of patterns that progress sequentially
# The first sequence is a modified version of 'spiralS' where the LEDs brighten and dim;
# The second sequence

# shifty051
########################################################################################

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
  piglow.led(3,1)
  sleep(0.05)
  
  piglow.led(14,1)
  piglow.led(3,2)
  sleep(0.05)
  
  piglow.led(14,0)
  piglow.led(3,2)
  sleep(0.05)
  
  piglow.led(3,3)
  sleep(0.05)
  
  piglow.led(3,4)
  sleep(0.05)
  
  piglow.led(3,3)
  sleep(0.05)
  
  piglow.led(3,2)
  piglow.led(9,1)
  sleep(0.05)
  
  piglow.led(3,1)
  piglow.led(9,2)
  sleep(0.05)
  
  piglow.led(3,0)
  piglow.led(9,3)
  sleep(0.05)
  
  piglow.led(9,4)
  sleep(0.05)
  
  piglow.led(9,3)
  sleep(0.05)
  
  piglow.led(9,2)
  piglow.led(15,1)
  sleep(0.05)
  
  piglow.led(9,1)
  piglow.led(15,2)
  sleep(0.05)
  
  piglow.led(9,0)
  piglow.led(15,3)
  sleep(0.05)
  
  piglow.led(15,4)
  sleep(0.05)
  
  piglow.led(15,3)
  sleep(0.05)

  piglow.led(15,2)
  piglow.led(4,1)
  sleep(0.05)  
  
  piglow.led(15,1)
  piglow.led(4,2)
  sleep(0.05) 
  
  piglow.led(15,0)
  piglow.led(4,3)
  sleep(0.05) 
  
  piglow.led(4,4)
  sleep(0.05) 
  
  piglow.led(4,3)
  sleep(0.05) 
  
  piglow.led(4,2)
  piglow.led(10,1)
  sleep(0.05) 
  
  piglow.led(4,1)
  piglow.led(10,2)
  sleep(0.05) 
  
  piglow.led(4,0)
  piglow.led(10,3)
  sleep(0.05) 
  
  piglow.led(10,4)
  sleep(0.05) 
  
  piglow.led(10,3)
  sleep(0.05) 
  
  piglow.led(10,2)
  piglow.led(16,1)
  sleep(0.05) 
  
  piglow.led(10,1)
  piglow.led(16,2)
  sleep(0.05)
  
  piglow.led(10,0)
  piglow.led(16,3)
  sleep(0.05)
  
  piglow.led(16,4)
  sleep(0.05)
  
  piglow.led(16,3)
  sleep(0.05)
  
  piglow.led(16,2)
  piglow.led(5,1)
  sleep(0.05)
  
  piglow.led(16,1)
  piglow.led(5,2)
  sleep(0.05)

  piglow.led(16,0)
  piglow.led(5,3)
  sleep(0.05)
  
  piglow.led(5,4)
  sleep(0.05)
  
  piglow.led(5,3)
  sleep(0.05)
  
  piglow.led(5,2)
  piglow.led(11,1)
  sleep(0.05)
  
  piglow.led(5,1)
  piglow.led(11,2)
  sleep(0.05)
  
  piglow.led(5,0)
  piglow.led(11,3)
  sleep(0.05)
  
  piglow.led(11,4)
  sleep(0.05)
  
  piglow.led(11,3)
  sleep(0.05)
  
  piglow.led(11,2)
  piglow.led(17,1)
  sleep(0.05)
  
  piglow.led(11,1)
  piglow.led(17,2)
  sleep(0.05)
  
  piglow.led(11,0)
  piglow.led(17,3)
  sleep(0.05)
  
  piglow.led(17,4)
  sleep(0.05)
  
  piglow.led(17,3)
  sleep(0.05)
  
  piglow.led(17,2)
  piglow.led(6,1)
  sleep(0.05)
  
  piglow.led(17,1)
  piglow.led(6,2)
  sleep(0.05)
  
  piglow.led(17,0)
  piglow.led(6,3)
  sleep(0.05)
  
  piglow.led(6,4)
  sleep(0.05)
  
  piglow.led(6,3)
  sleep(0.05)
  
  piglow.led(6,2)
  piglow.led(12,1)
  sleep(0.05)
  
  piglow.led(6,1)
  piglow.led(12,2)
  sleep(0.05)
  
  piglow.led(6,0)
  piglow.led(12,3)
  sleep(0.05)
  
  piglow.led(12,4)
  sleep(0.05)
  
  piglow.led(12,3)
  sleep(0.05)
  
  piglow.led(12,2)
  piglow.led(18,1)
  sleep(0.05)

  piglow.led(12,1)
  piglow.led(18,2)
  sleep(0.05)
  
  piglow.led(12,0)
  piglow.led(18,3)
  sleep(0.05)
  
  piglow.led(18,4)
  sleep(0.05)
  
  piglow.led(18,3)
  sleep(0.05)
  
  piglow.led(18,2)
  sleep(0.05)

  piglow.led(18,1)
  sleep(0.05)
  
  piglow.led(18,0)
  sleep(0.05)
  
  
  
  piglow.red(1)
  sleep(0.05)
  
  piglow.red(2)
  sleep(0.05)
  
  piglow.red(3)
  piglow.orange(1)
  sleep(0.05)
  
  piglow.red(4)
  piglow.orange(2)
  sleep(0.05)
  
  piglow.orange(3)
  piglow.yellow(1)
  sleep(0.05)
  
  piglow.orange(4)
  piglow.yellow(2)
  sleep(0.05)
  
  piglow.yellow(3)
  piglow.green(1)
  sleep(0.05)
  
  piglow.yellow(4)
  piglow.green(2)
  sleep(0.05)
  
  piglow.green(3)
  piglow.blue(1)
  sleep(0.05)
  
  piglow.green(4)
  piglow.blue(2)
  sleep(0.05)
  
  piglow.blue(3)
  piglow.white(1)
  sleep(0.05)
  
  piglow.blue(4)
  piglow.white(2)
  sleep(0.05)
  
  piglow.white(3)
  sleep(0.05)
  
  piglow.white(4)
  sleep(0.05)
  
  piglow.white(5)
  sleep(0.05)
  
  piglow.white(6)
  sleep(0.05)
  
  piglow.white(7)
  sleep(0.05)
  
  piglow.white(8)
  sleep(2)
  
  piglow.white(7)
  sleep(0.05)
  
  piglow.white(6)
  sleep(0.05)
  
  piglow.blue(1)
  piglow.white(5)
  sleep(0.05)
  
  piglow.blue(2)
  piglow.white(4)
  sleep(0.05)
  
  piglow.blue(3)
  piglow.green(1)
  sleep(0.05)
  
  piglow.blue(4)
  piglow.green(2)
  sleep(0.05)
  
  piglow.green(3)
  piglow.yellow(1)
  sleep(0.05)
  
  piglow.green(4)
  piglow.yellow(2)
  sleep(0.05)
  
  piglow.yellow(3)
  piglow.orange(1)
  sleep(0.05)
  
  piglow.yellow(4)
  piglow.orange(2)
  sleep(0.05)
  
  piglow.orange(3)
  piglow.red(1)
  sleep(0.05)
  
  piglow.orange(4)
  piglow.red(2)
  sleep(0.05)
  
  piglow.red(3)
  sleep(0.05)
  
  piglow.red(4)
  sleep(1.5)
  
  piglow.led(6,0)
  sleep(0.05)
  
  piglow.led(12,0)
  sleep(0.05)
  
  piglow.led(18,0)
  sleep(0.05)
  
  piglow.led(5,0)
  sleep(0.05)
  
  piglow.led(11,0)
  sleep(0.05)
  
  piglow.led(17,0)
  sleep(0.05)
  
  piglow.led(4,0)
  sleep(0.05)
  
  piglow.led(10,0)
  sleep(0.05)
  
  piglow.led(16,0)
  sleep(0.05)
  
  piglow.led(3,0)
  sleep(0.05)
  
  piglow.led(9,0)
  sleep(0.05)
  
  piglow.led(15,0)
  sleep(0.05)
  
  piglow.led(2,0)
  sleep(0.05)
  
  piglow.led(8,0)
  sleep(0.05)
  
  piglow.led(14,0)
  sleep(0.05)
  
  piglow.led(1,0)
  sleep(0.05)
  
  piglow.led(7,0)
  sleep(0.05)
  
  piglow.led(13,5)
  sleep(0.1)
  
  piglow.led(13,6)
  sleep(0.1)
  
  piglow.led(13,7)
  sleep(2)
  
  piglow.led(13,6)
  sleep(0.05)
  
  
  
  
  
  
  
  
  
  
  
  
  
