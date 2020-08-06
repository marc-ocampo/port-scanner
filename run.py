from inputparser import InputParser
from portscanner import PortScanner

import os

def trigger_port_scanner():
  print('-' * 60)
  print('Welcome to Port Scanner!')
  input_hosts_string = input('Enter host name to scan: ')
  input_ports_string = input('Enter ports to scan: ')
  print('-' * 60)

  input_parser = InputParser(input_hosts_string, input_ports_string)
  port_scanner = PortScanner(input_parser)

if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear')
  trigger_port_scanner()