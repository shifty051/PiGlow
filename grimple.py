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

  for i > 4:
    piglow.led(1,1)
    sleep(0.5)
  
    piglow.led(7,1)
    piglow.led(1.0)
    sleep(0.5)
  
    piglow.led(13,1)
    piglow.led(7,0)
    sleep(0.5)
  
    i++

  
  
  
  
  
  
  
  
  
  
