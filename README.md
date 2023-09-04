Python Port Scanner
This is a simple port scanner written in Python that utilizes the nmap module.

Usage
To scan a target host:

Copy code

python portscanner.py <target_host>
To scan a target host on a specific port range:

Copy code

python portscanner.py <target_host> -p <port range>
For example:

Copy code

python portscanner.py 192.168.1.1 -p 1-1024
This will scan ports 1-1024 on 192.168.1.1 and output any open ports.

Requirements
Python 3
nmap module
Install with pip install python-nmap
Features
Scan a single target or multiple targets
Specify port range to scan
Output scan results showing open/closed ports
Option to output results to a file
Configurable timeout value for scans
Simple command line interface
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
nmap - Port scanning utility used by this scanner
python-nmap - Provides Python interface to Nmap
Let me know if you would like me to expand or modify this README further!