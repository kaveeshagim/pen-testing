import nmap

scanner = nmap.PortScanner()

print("Welcome to the Network Scanner!")
print("<---------------------------------->")

ip_addr = input("Enter the IP address to scan: ")
print(f"Scanning {ip_addr}...")
type(ip_addr)

resp = input(""" /nPlease select the type of scan you want to perform: 
                 1. SYN ACK Scan
                 2. UDP Scan
                 3. Comprehensive Scan \n""")

print("Selected option:", resp)

if resp == "1":
    print("Nmap Version:", scanner.nmap_version())
    print("Performing SYN ACK Scan...")
    scanner.scan(ip_addr, '1-1024', '-v -sS') #to perform SYN ACK scan 
    # 1-1024 for ports
    # '-v' for verbose output, '-sS' for SYN scan
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_addr].state()) #to check if the host is up
    print(scanner[ip_addr].all_protocols()) #to check the protocols
    print("Open Ports:", scanner[ip_addr]['tcp'].keys()) #to check the open ports
elif resp == "2":
    print("Nmap Version:", scanner.nmap_version())
    print("Performing UDP Scan...")
    scanner.scan(ip_addr, '1-1024', '-v -sU') #to perform UDP scan
    # '-sU' for UDP scan
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports:", scanner[ip_addr]['udp'].keys())
elif resp == "3":
    print("Nmap Version:", scanner.nmap_version())
    print("Performing Comprehensive Scan...")
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -0') #to perform comprehensive scan
    # '-sV' for version detection, '-sC' for default scripts, '-A' for OS detection, '-0' for all ports
    # '-v' for verbose output, '-sS' for SYN scan
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())    
    print("Open Ports:", scanner[ip_addr]['tcp'].keys())
else:
    print("Invalid option selected. Please run the script again and select a valid option.")