import os
import subprocess
import time
from daemon import runner
import datetime
import re 

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/bandwidth_counter.pid'
        self.pidfile_timeout = 5
    def run(self):
        rx_megabits_new = 0
        tx_megabits_new = 0
        try:
                while True:
                        output = subprocess.Popen(['ifconfig', "wlan0"], stdout=subprocess.PIPE).communicate()[0]
                        rx_bytes = re.findall('RX bytes:([0-9]*) ', output)[0]
                        tx_bytes = re.findall('TX bytes:([0-9]*) ', output)[0]
                        rx_megabits = (((int(rx_bytes) * 8) / 1024) / 1024)
                        tx_megabits = (((int(tx_bytes) * 8) / 1024) / 1024)
                        current_rx_usage = rx_megabits - rx_megabits_new
                        current_tx_usage = tx_megabits - tx_megabits_new
                        rx_megabits_new = rx_megabits
                        tx_megabits_new = tx_megabits 
                        print 'average megabits received', current_rx_usage / 60
                        print 'average kilobits received', (current_rx_usage * 1024) / 60
                        print 'average megabits sent', current_tx_usage / 60
                        print 'average kilobits sent', (current_tx_usage * 1024) / 60
                        time.sleep(60)

        except Exception, e:
            raise


app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
