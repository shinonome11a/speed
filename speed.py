#!/usr/bin/env python3
import subprocess
import time
import sys
import os

args = sys.argv
if(len(args) != 2):
   print('Invalid argment')
   print('"speed.py <interface name>"')
   sys.exit(1)


try:
   res = str(subprocess.check_output(['ip', '-s', 'link', 'show', 'dev', args[1]]).decode())
except:
   print("Command error.")
   sys.exit(1)
rx = float(res.split('\n')[3].split()[0])
tx = float(res.split('\n')[5].split()[0])
rx_init = rx
tx_init = tx
start = 'start at: ' + str(subprocess.check_output(['date']).decode())

os.system('clear')
print('Please wati ...\r',end='')
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
      rx_bites = (rx - rx_init)
      tx_bites = (tx - tx_init)

      print('Interface: ' + args[1])
      print(start)
      if(rx_speed / 1000000000 > 1):
         print('RX speed: ' + str(rx_speed / 1000000000) + ' Gbps                   ')
      elif(rx_speed / 1000000 > 1):
         print('RX speed: ' + str(rx_speed / 1000000) + ' Mbps                   ')
      elif(rx_speed / 1000 > 1):
         print('RX speed: ' + str(rx_speed / 1000) + ' kbps                   ')
      else:
         print('RX speed: ' + str(rx_speed) + ' bps                   ')
      if(tx_speed / 1000000000 > 1):
         print('TX speed: ' + str(tx_speed / 1000000000) + ' Gbps                   ')
      elif(tx_speed / 1000000 > 1):
         print('TX speed: ' + str(tx_speed / 1000000) + ' Mbps                   ')
      elif(tx_speed / 1000 > 1):
         print('TX speed: ' + str(tx_speed / 1000) + ' kbps                   ')
      else:
         print('TX speed: ' + str(tx_speed) + ' bps                   ')
      
      if(rx_bites / 1000000000000 > 1):
         print('RX bites: ' + str(rx_bites / 1000000000000) + ' TB                   ')
      elif(rx_bites / 1000000000 > 1):
         print('RX bites: ' + str(rx_bites / 1000000000) + ' GB                   ')
      elif(rx_bites / 1000000 > 1):
         print('RX bites: ' + str(rx_bites / 1000000) + ' MB                   ')
      elif(rx_bites / 1000 > 1):
         print('RX bites: ' + str(rx_bites / 1000) + ' kB                   ')
      else:
         print('RX bites: ' + str(rx_bites) + ' B                   ')
      if(tx_bites / 1000000000000 > 1):
         print('TX bites: ' + str(tx_bites / 1000000000000) + ' TB                   ')
      elif(tx_bites / 1000000000 > 1):
         print('TX bites: ' + str(tx_bites / 1000000000) + ' GB                   ')
      elif(tx_bites / 1000000 > 1):
         print('TX bites: ' + str(tx_bites / 1000000) + ' MB                   ')
      elif(tx_bites / 1000 > 1):
         print('TX bites: ' + str(tx_bites / 1000) + ' kB                   ')
      else:
         print('TX bites: ' + str(tx_bites) + ' B                   ')
      
      if(rx / 1000000000000 > 1):
         print('RX total: ' + str(rx / 1000000000000) + ' TB                   ')
      elif(rx / 1000000000 > 1):
         print('RX total: ' + str(rx / 1000000000) + ' GB                   ')
      elif(rx / 1000000 > 1):
         print('RX: total' + str(rx / 1000000) + ' MB                   ')
      elif(rx / 1000 > 1):
         print('RX: total' + str(rx / 1000) + ' kB                   ')
      else:
         print('RX total: ' + str(rx) + ' B                   ')
      
      if(tx / 1000000000000 > 1):
         print('TX total: ' + str(tx / 1000000000000) + ' TB                   ')
      elif(tx / 1000000000 > 1):
         print('TX total: ' + str(tx / 1000000000) + ' GB                   ')
      elif(tx / 1000000 > 1):
         print('TX total: ' + str(tx / 1000000) + ' MB                   ')
      elif(tx / 1000 > 1):
         print('TX total: ' + str(tx / 1000) + ' kB                   ')
      else:
         print('TX total: ' + str(tx) + ' B                   ')

      print("\033[9A",end="")
      time.sleep(1)
except KeyboardInterrupt:
   os.system('clear')
   sys.exit(0)
