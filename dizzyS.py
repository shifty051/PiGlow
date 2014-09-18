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

  piglow.led(1,1)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(1,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(7,0)
  sleep(0.05)
  
  piglow.led(1,1)
  piglow.led(13,0)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(1,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(7,0)
  sleep(0.05)
  
  piglow.led(1,1)
  piglow.led(13,0)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(1,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(7,0)
  sleep(0.05)
  
  
  piglow.led(1,1)
  piglow.led(2,1)
  piglow.led(13,0)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(8,1)
  piglow.led(1,0)
  piglow.led(2,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(14,1)
  piglow.led(7,0)
  piglow.led(8,0)
  sleep(0.05)
  
  piglow.led(1,1)
  piglow.led(2,1)
  piglow.led(13,0)
  piglow.led(14,0)
  sleep(0.05)
  
  piglow.led(7,1)
  piglow.led(8,1)
  piglow.led(1,0)
  piglow.led(2,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(14,1)
  piglow.led(7,0)
  piglow.led(8,0)
  sleep(0.05)
  
  piglow.led(1,1)
  piglow.led(2,1)
  piglow.led(13,0)
  piglow.led(14,0)
  sleep(0.5)
  
  piglow.led(7,1)
  piglow.led(8,1)
  piglow.led(1,0)
  piglow.led(2,0)
  sleep(0.05)
  
  piglow.led(13,1)
  piglow.led(14,1)
  piglow.led(7,0)
  piglow.led(8,0)
  sleep(0.05)
  
  
    

  
  
  
  
  
  
  
  
  
  
