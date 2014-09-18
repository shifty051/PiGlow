########################################################################################
# A fun set of patterns that progress sequentially
# The first sequence is a modified version of 'spiralS' where the LEDs brighten and dim;
# The second sequence lights all LEDs by colour sequentially toward the centre by increasing brightness
# The third sequence turns off LEDs in a spiral pattern away from the centre


# shifty051
########################################################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.red(1)
  sleep(0.05)
  
  piglow.red(2)
  sleep(0.05)
  
  piglow.red(3)
  sleep(0.05)

  piglow.red(4)
  sleep(0.05)
  
  piglow.red(3)
  sleep(0.05)
  
  piglow.red(2)
  piglow.orange(1)
  sleep(0.05)
  
  piglow.red(1)
  piglow.orange(2)
  sleep(0.05)
  
  piglow.red(0)
  piglow.orange(3)
  sleep(0.05)
  
  piglow.orange(4)
  sleep(0.05)
  
  piglow.orange(3)
  sleep(0.05)
  
  piglow.orange(2)
  piglow.yellow(1)
  sleep(0.05)
  
  piglow.orange(1)
  piglow.yellow(2)
  sleep(0.05)
  
  piglow.orange(0)
  piglow.yellow(3)
  sleep(0.05)
  
  piglow.yellow(4)
  sleep(0.05)
  
  piglow.yellow(3)
  sleep(0.05)
  
  piglow.yellow(2)
  piglow.green(1)
  sleep(0.05)
  
  piglow.yellow(1)
  piglow.green(2)
  sleep(0.05)
  
  piglow.yellow(0)
  piglow.green(3)
  sleep(0.05)
  
  piglow.green(4)
  sleep(0.05)
  
  piglow.green(3)
  sleep(0.05)
  
  piglow.green(2)
  piglow.blue(1)
  sleep(0.05)
  
  piglow.green(1)
  piglow.blue(2)
  sleep(0.05)
  
  piglow.green(0)
  piglow.blue(3)
  sleep(0.05)
  
  piglow.blue(4)
  sleep(0.05)
  
  piglow.blue(3)
  sleep(0.05)
  
  piglow.blue(2)
  piglow.white(1)
  sleep(0.05)
  
  piglow.blue(1)
  pigloe.white(2)
  sleep(0.05)
  
  piglow.blue(0)
  pigloe.white(3)
  sleep(0.05)
  
  pigloe.white(4)
  sleep(2)
  
  
 
  
  
  
