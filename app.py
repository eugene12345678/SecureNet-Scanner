
from scanner.nmap_scanner import scan_network, get_vulnerabilities
from scanner.vulnerability_check import remediation_suggestions
from reports.generate_report import generate_report

def main():
    ip_range = input("Enter IP range to scan (e.g., 192.168.1.0/24): ")
    scan_results = scan_network(ip_range)
    vulnerabilities = get_vulnerabilities(scan_results)
    suggestions = remediation_suggestions(vulnerabilities)

    print("\nVulnerabilities Found:")
    for vuln in vulnerabilities:
        print(f"- {vuln}")

    print("\nRemediation Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")

    generate_report(ip_range, vulnerabilities)
    print("Report generated: scan_report.html")

if __name__ == "__main__":
    main()
