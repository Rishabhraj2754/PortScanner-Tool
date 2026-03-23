#!/usr/bin/env python3
"""
PORT SCANNER - Network Security Tool
Author: Rishabh Raj
Purpose: Educational port scanning tool for learning network security
"""

import socket
import sys
from datetime import datetime
import csv
import os

class PortScanner:
    """
    Port Scanner Tool
    Scans target IP/domain for open ports
    """
    
    def __init__(self):
        self.open_ports = []
        self.closed_ports = []
        self.start_time = None
        self.end_time = None
        
        # Common ports and their services
        self.services = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            465: 'SMTP-SSL',
            587: 'SMTP',
            993: 'IMAP-SSL',
            995: 'POP3-SSL',
            3306: 'MySQL',
            5432: 'PostgreSQL',
            5900: 'VNC',
            8080: 'HTTP-Proxy',
            8443: 'HTTPS-Alt'
        }
    
    def display_banner(self):
        """Display welcome banner"""
        print("\n" + "="*60)
        print("🔍 PORT SCANNER - Network Security Tool")
        print("="*60)
        print("Author: Rishabh Raj")
        print("Purpose: Educational Network Scanning")
        print("="*60 + "\n")
    
    def get_service_name(self, port):
        """Get service name for port"""
        return self.services.get(port, "Unknown")
    
    def resolve_ip(self, target):
        """Convert domain to IP if needed"""
        try:
            # If it's a domain, convert to IP
            ip = socket.gethostbyname(target)
            return ip
        except socket.gaierror:
            print(f"❌ Error: Could not resolve '{target}'")
            return None
        except socket.error:
            print(f"❌ Error: Could not connect to '{target}'")
            return None
    
    def scan_port(self, target_ip, port):
        """Scan single port"""
        try:
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            
            # Try to connect
            result = sock.connect_ex((target_ip, port))
            sock.close()
            
            if result == 0:
                return True  # Port is open
            else:
                return False  # Port is closed
        except socket.error as e:
            return False
    
    def scan_range(self, target, start_port, end_port):
        """Scan port range"""
        self.start_time = datetime.now()
        
        # Resolve target if it's a domain
        target_ip = self.resolve_ip(target)
        if not target_ip:
            return False
        
        print(f"Target: {target} ({target_ip})")
        print(f"Scanning ports {start_port}-{end_port}...")
        print("="*60)
        
        # Scan each port
        for port in range(start_port, end_port + 1):
            if self.scan_port(target_ip, port):
                service = self.get_service_name(port)
                print(f"✓ Port {port:<6} : {service:<15} [OPEN]")
                self.open_ports.append((port, service))
            else:
                # Don't print closed ports (too much output)
                self.closed_ports.append(port)
            
            # Show progress every 100 ports
            if port % 100 == 0:
                print(f"  Progress: {port}/{end_port}")
        
        self.end_time = datetime.now()
        return True
    
    def display_results(self):
        """Display scan results"""
        print("\n" + "="*60)
        print("📊 SCAN RESULTS")
        print("="*60)
        
        if self.open_ports:
            print(f"\n✓ Found {len(self.open_ports)} OPEN port(s):\n")
            for port, service in self.open_ports:
                print(f"  Port {port:<6} : {service}")
        else:
            print("\n❌ No open ports found")
        
        print(f"\n✗ Closed ports: {len(self.closed_ports)}")
        
        # Calculate scan time
        scan_time = self.end_time - self.start_time
        print(f"\n⏱️  Scan Time: {scan_time.total_seconds():.2f} seconds")
        print("="*60 + "\n")
    
    def save_to_csv(self, target):
        """Save results to CSV file"""
        # Create results directory if it doesn't exist
        if not os.path.exists('results'):
            os.makedirs('results')
        
        # Create filename
        filename = f"results/scan_{target.replace('.', '_')}.csv"
        
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Port', 'Service', 'Status'])
                
                for port, service in self.open_ports:
                    writer.writerow([port, service, 'OPEN'])
            
            print(f"✓ Results saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    def run(self):
        """Main scanning function"""
        self.display_banner()
        
        try:
            # Get target
            target = input("Enter target (IP or domain): ").strip()
            if not target:
                print("❌ Target cannot be empty!")
                return
            
            # Get port range
            start_port_input = input("Enter start port (default 1): ").strip()
            start_port = int(start_port_input) if start_port_input else 1
            
            end_port_input = input("Enter end port (default 1000): ").strip()
            end_port = int(end_port_input) if end_port_input else 1000
            
            # Validate ports
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("❌ Invalid port range! Ports must be 1-65535")
                return
            
            print("\n" + "="*60)
            
            # Run scan
            if self.scan_range(target, start_port, end_port):
                self.display_results()
                
                # Save to CSV
                if self.open_ports:
                    save = input("Save results to CSV? (y/n): ").strip().lower()
                    if save == 'y':
                        self.save_to_csv(target)
        
        except ValueError:
            print("❌ Invalid input! Please enter numbers for ports.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Scan interrupted by user")
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """Main entry point"""
    scanner = PortScanner()
    scanner.run()


if __name__ == "__main__":
    main()