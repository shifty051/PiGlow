#########################################################
# Set the Piglow To breathe function ##
# shifty051
#########################################################

  from piglow import PiGlow
  from time import sleep

  piglow = PiGlow()
  piglow.all(0)

  while True:
    piglow.red(5)
    sleep(3)
    
    piglow.orange(5)
    sleep(3)
    
    piglow.yellow(5)
    sleep(3)
    
    piglow.green(5)
    sleep(3)
    
    piglow.blue(5)
    sleep(3)
    
    piglow.white(5)
    sleep(3)
    
    
    
