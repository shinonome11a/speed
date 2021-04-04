#!/usr/bin/env python3
import subprocess
import time
import sys
import os

args = sys.argv
if(len(args) != 2):
   print('Invalid argment')
   print('"/path/to/speed.py <interface name (ex: enp0s1)>"')
   sys.exit(1)

print('Please wati ...\r',end='')

try:
   res = str(subprocess.check_output(['ip', '-s', 'link', 'show', 'dev', args[1]]).decode())
except:
   print("Command error.")
   sys.exit(1)
rx = float(res.split('\n')[3].split()[0])
tx = float(res.split('\n')[5].split()[0])

os.system('clear')
time.sleep(1)
try:
   while True:
      rx_old = rx
      tx_old = tx

      try:
         res = str(subprocess.check_output(['ip', '-s', 'link', 'show', 'dev', args[1]]).decode())
      except:
         print("Commnad error.")
         sys.exit(1)
      rx = float(res.split('\n')[3].split()[0])
      tx = float(res.split('\n')[5].split()[0])

      rx_speed = (rx - rx_old) * 8
      tx_speed = (tx - tx_old) * 8

      print('Interface: ' + args[1])
      if(rx_speed / 1000000000 > 1 or tx_speed / 1000000000 > 1):
         print('RX speed: ' + str(rx_speed / 1000000000) + ' Gbps                   ')
         print('TX speed: ' + str(tx_speed / 1000000000) + ' Gbps                   ')
      elif(rx_speed / 1000000 > 1 or tx_speed / 1000000 > 1):
         print('RX speed: ' + str(rx_speed / 1000000) + ' Mbps                   ')
         print('TX speed: ' + str(tx_speed / 1000000) + ' Mbps                   ')
      elif(rx_speed / 1000 > 1 or tx_speed / 1000 > 1):
         print('RX speed: ' + str(rx_speed / 1000) + ' kbps                   ')
         print('TX speed: ' + str(tx_speed / 1000) + ' kbps                   ')
      else:
         print('RX speed: ' + str(rx_speed) + ' bps                   ')
         print('TX speed: ' + str(tx_speed) + ' bps                   ')

      print("\033[3A",end="")
      time.sleep(1)
except KeyboardInterrupt:
   os.system('clear')
   sys.exit(0)
