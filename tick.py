#############################
# Calm LED effect for piglow
# shifty051
#############################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:

  piglow.red(5)
  sleep(5)
