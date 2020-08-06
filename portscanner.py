#!/usr/bin/env python

from inputparser import InputParser
import socket
import sys

class PortScanner(object):
  def __init__(self, input_parser):
    self.host_list = input_parser.get_target_hosts()
    self.port_list = input_parser.get_target_ports()
    self.scan_all_hosts()

  def scan_all_hosts(self):
    print('Scanning')
    for host in self.host_list:
      self.scan_all_ports_per_host(host)

  def scan_all_ports_per_host(self, host):
    self.open_port_list = []
    for port in self.port_list:
      self.scan_target_host_port(host, port)
    self.display_open_ports(host)

  def scan_target_host_port(self, host, port):
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((host, port))
      self.check_result(port, result)
      sock.close()
    except KeyboardInterrupt:
      print('User terminated the program.')
      sys.exit()
    except socket.gaiaerror:
      print('Hostname could not be resolved.')
      sys.exit()
    except socket.error:
      print('Could not connect to server.')
      sys.exit()

  def check_result(self, port, result):
    if 0 == result:
      service = '' #= grab_banner(sock)
      # TODO fetch banner here?
      self.open_port_list.append((port, service))

  def display_open_ports(self, host):
    print('-' * 60)
    print('Scan report for ' + host)
    if 0 == len(self.open_port_list):
      print('Unable to find open ports for ' + host + '.')
    else:
      for port_service_pair in self.open_port_list:
        print(str(port_service_pair[0]) + '/tcp open\r' + port_service_pair[1])
    print('-' * 60)

