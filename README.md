# port-scanner

## REQUIREMENTS:
- python 3.8
- ipcalc (https://pypi.python.org/pypi/ipcalc)

## MECHANICS
### Inputs:
- host name e.g. www.google.com
- ip address e.g. 1.1.1.1
- ip range e.g. 1.1.1.1-10
- network e.g. 1.1.1.0/24

### TCP Scanning
- default is the 1000 ports that is being used by NMAP
- specify port e.g. 80
- specify port range e.g. 90-10000

## For improvement
- Use of raw TCP packets instead of connect_ex
- Get services (banner grabbing)
- Identify remote OS
- UDP scanning
- threading for shorter scanning time