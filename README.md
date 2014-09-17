PiGlow
======

The following is a list of python scripts for the PiGlow Raspberry Pi addon by Pimoroni

Scripts
======

cpuS.py - A modified version of the cpu.py script from Jason Barnett (@Boeeerb). The brightness and sleep time values were           modified

softS.py -Cycles the LEDs sequentially from the outside toward the centre whilst gradually increasing/decreasing the                 brightness

tickS.py -Cyles the LEDs ON in sequential order. Once all are activated, cycles them OFF in reverse order (from the                  centre)

spiralS.py - Cycles the LEDs on/off in a spiral motion toward the centre. Each colour on each arm is turned on/off in                order 

spiralS-2.py - A modified version of spiralS.py. LEDs stay on as they are cycled until all LEDs have been activated, at                                 which they reset to default state. 

Requirements 
============

sudo apt-get install python-smbus
sudo apt-get install python-psutil

Functions
=========

from piglow import PiGlow 
piglow = PiGlow()

piglow.color([1-6],[0-255])    # where [color number (1=White, 2=Blue, 3=Green, 4=Yellow, 5=Orange, 6=Red)], [brightness level (0=off / 255=oh-god-my-eyes)]

                                
piglow.color([color],[0-255])  # "white", "blue", "green", "yellow", "orange", "red"

piglow.white([0-255])           # Control all the white LEDs

piglow.blue([0-255])            # Control all the blue LEDs

piglow.green([0-255])           # Control all the green LEDs

piglow.yellow([0-255])          # Control all the yellow LEDs

piglow.orange([0-255])          # Control all the orange LEDs

piglow.red([0-255])             # Control all the red LEDs

piglow.all([0-255])             # Control all LEDs together

piglow.led([1-18],[0-255])      # Control an individual LED by number

piglow.led1-led18([0-255])      # Control an individual LED by function

piglow.arm([1-3],[0-255])       # Control an arm of LEDs by number

piglow.arm1([0-255])            # Control the top arm (with PiGlow logo at the top)

piglow.arm2([0-255])            # Control the right arm (with PiGlow logo at the top)

piglow.arm3([0-255])            # Control the left arm (with PiGlow logo at the top)







