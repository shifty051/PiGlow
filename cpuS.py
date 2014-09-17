########################################################################
# Custom CPU Activity Monitor 
# This code was adapted from Jason Barnett's code. (@Boeeerb)
# All credit goes to him. I simply changed the values to suit my purpose.
# Requires psutil - sudo apt-get install python-psutil ##
# Shifty051 
########################################################################

from piglow import PiGlow
from time import sleep
import psutil

piglow = PiGlow()

while True:
  
  cpu = psutil.cpu_percent()
  piglow.all(0)

  if cpu < 5:
    piglow.red(10)

  elif cpu < 20:
    piglow.red(1)
    piglow.orange(1)

  elif 20 < cpu < 49:
    piglow.red(1)
    piglow.orange(1)
    piglow.yellow(1)

  elif cpu < 60:
    piglow.red(1)
    piglow.orange(1)
    piglow.yellow(1)
    piglow.green(1)

  elif cpu < 80:
    piglow.red(10)
    piglow.orange(1)
    piglow.yellow(1)
    piglow.green(1)
    piglow.blue(1)

  else:
    piglow.white(1)
    sleep(1)

