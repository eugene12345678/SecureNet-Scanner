import nmap

def scan_network(ip_range):
    scanner = nmap.PortScanner()
    scanner.scan(ip_range, arguments='-sV')  
    return scanner

def get_vulnerabilities(scan_results):
    # Extract open ports, services, versions, etc.
    vulnerabilities = []
    for host in scan_results.all_hosts():
        for port in scan_results[host].get('tcp', {}):
            service = scan_results[host]['tcp'][port]
            # Example vulnerability check based on service/version
            if service['state'] == 'open' and service.get('product') == 'Apache':
                if service.get('version', '0') < '2.4.49':
                    vulnerabilities.append(f"Apache version vulnerable on port {port}")
    return vulnerabilities