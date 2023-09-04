import nmap

nm = nmap.PortScanner()

target = input("Enter target IP address: ")
port_range = input("Enter port range to scan (e.g. 1-1024): ")

nm.scan(target, port_range)

for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        for port in lport:
            print('port : %s\tstate : %s' %
                  (port, nm[host][proto][port]['state']))
