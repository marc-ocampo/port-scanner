# port-scanner

#######################################################################
# PROJECT : Port Scanner (ee298)
# AUTHOR  : Marc Stephen D. Ocampo (2006-03669)
#######################################################################
# TODO
# Use raw TCP packets instead of connect_ex
# Get services
# Identify remote OS
# UDP scan
#######################################################################
REQUIREMENTS:
- python 2.7
- ipcalc (https://pypi.python.org/pypi/ipcalc)



Inputs:
- host name e.g. www.google.com
- ip address e.g. 1.1.1.1
- ip range e.g. 1.1.1.1-10
- network e.g. 1.1.1.0/24

TCP Scanning
- default is the 1000 ports that is being used by NMAP
- specify port e.g. 80
- specify port range e.g. 90-10000


ADDITIONALS:
UDP Scanning
- bonus 15%
- at least port 53 and 161

Service Name / Banner Grabbing
- bonus 15%

OS Detection
- bonus 15%
