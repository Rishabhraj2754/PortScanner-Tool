#!/usr/bin/env python3
"""
PORT SCANNER - Network Security Tool
Author: Rishabh Raj
Purpose: Educational port scanning tool
Phase 3: CSV Export and Data Management
"""

import socket
import time
import os
import csv
from datetime import datetime

class PortScanner:
    def __init__(self):
        """Initialize the port scanner with common service ports"""
        self.services = {
            21: 'FTP',
            22: 'SSH',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            465: 'SMTPS',
            587: 'SMTP',
            993: 'IMAPS',
            995: 'POP3S',
            3306: 'MySQL',
            5432: 'PostgreSQL',
            5900: 'VNC',
            8080: 'HTTP-Alt',
            8443: 'HTTPS-Alt',
            27017: 'MongoDB'
        }
        self.results_folder = 'results'
        self.create_results_folder()

    def create_results_folder(self):
        """Create results folder if it doesn't exist"""
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)
            print(f"✓ Created results folder: {self.results_folder}/")

    def resolve_ip(self, target):
        """Convert domain name to IP address"""
        try:
            ip = socket.gethostbyname(target)
            return ip
        except socket.gaierror:
            print(f"✗ Cannot resolve {target}")
            return None

    def scan_port(self, target_ip, port):
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            sock.close()
            return result == 0
        except Exception as e:
            return False

    def get_service_name(self, port):
        """Get service name for a port"""
        return self.services.get(port, "Unknown")

    def save_to_csv(self, target, open_ports):
        """Save scan results to CSV file"""
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"scan_{target.replace('.', '_')}_{timestamp}.csv"
        filepath = os.path.join(self.results_folder, filename)

        try:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Port', 'Service', 'Status']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header
                writer.writeheader()

                # Write open ports
                for port in open_ports:
                    service = self.get_service_name(port)
                    writer.writerow({
                        'Port': port,
                        'Service': service,
                        'Status': 'OPEN'
                    })

            return filepath
        except Exception as e:
            print(f"✗ Error saving CSV: {e}")
            return None

    def scan_target(self, target, start_port, end_port):
        """Scan target IP/domain for open ports"""
        print("\n" + "="*60)
        print("🔍 PORT SCANNER - Network Security Tool")
        print("="*60)

        # Resolve IP if domain is provided
        target_ip = self.resolve_ip(target)
        if not target_ip:
            return

        print(f"✓ Resolved: {target} → {target_ip}")
        print(f"\nScanning ports {start_port}-{end_port}...")
        print("="*60)

        # Scan ports
        start_time = time.time()
        open_ports = []

        for port in range(start_port, end_port + 1):
            if self.scan_port(target_ip, port):
                service = self.get_service_name(port)
                open_ports.append(port)
                print(f"✓ Port {port:5d} : {service:15s} [OPEN]")

        end_time = time.time()
        scan_time = end_time - start_time

        # Display results
        print("\n" + "="*60)
        print("📊 SCAN RESULTS")
        print("="*60)

        if open_ports:
            print(f"\n✓ Found {len(open_ports)} OPEN port(s):\n")
            for port in open_ports:
                service = self.get_service_name(port)
                print(f"  Port {port:5d} : {service}")
        else:
            print("\n✗ No open ports found")

        closed_ports = (end_port - start_port + 1) - len(open_ports)
        print(f"\n✗ Closed ports scanned: {closed_ports}")
        print(f"⏱️  Scan Time: {scan_time:.2f} seconds")

        # Save to CSV
        if open_ports:
            filepath = self.save_to_csv(target_ip, open_ports)
            if filepath:
                print(f"\n✓ Results saved to: {filepath}")
        else:
            print("\n⚠️  No open ports to save")

        print("="*60)

def main():
    """Main function"""
    scanner = PortScanner()

    print("\n🔍 PORT SCANNER - Network Security Tool")
    print("="*60)

    target = input("\nEnter target (IP or domain): ").strip()
    if not target:
        print("✗ Target cannot be empty")
        return

    try:
        start_port = int(input("Enter start port (default 1): ").strip() or "1")
        end_port = int(input("Enter end port (default 1000): ").strip() or "1000")

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("✗ Invalid port range")
            return

        scanner.scan_target(target, start_port, end_port)

    except ValueError:
        print("✗ Invalid input. Please enter valid numbers")

if __name__ == "__main__":
    main()