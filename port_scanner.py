#!/usr/bin/env python3
"""
PORT SCANNER - Network Security Tool
Author: Rishabh Raj
Purpose: Educational port scanning tool
Phase 2: Core scanning logic and service detection
"""

import socket
from datetime import datetime

class PortScanner:
    """Port Scanner Tool - Phase 2: Scanning Logic"""
    
    def __init__(self):
        self.open_ports = []
        self.closed_ports = []
        self.target = None
        self.target_ip = None
        self.start_time = None
        self.end_time = None
        
        # Common services and their ports
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
        print("Author: Rishabh Raj | Phase 2: Scanning Logic")
        print("="*60 + "\n")
    
    def resolve_ip(self, target):
        """Convert domain to IP if needed"""
        try:
            ip = socket.gethostbyname(target)
            print(f"✓ Resolved: {target} → {ip}\n")
            return ip
        except socket.gaierror:
            print(f"❌ Error: Could not resolve '{target}'")
            return None
        except socket.error:
            print(f"❌ Error: Could not connect to '{target}'")
            return None
    
    def get_service_name(self, port):
        """Get service name for port"""
        return self.services.get(port, "Unknown")
    
    def scan_port(self, target_ip, port):
        """Scan single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            
            result = sock.connect_ex((target_ip, port))
            sock.close()
            
            return result == 0  # True if open, False if closed
        except socket.error:
            return False
    
    def scan_range(self, target, start_port, end_port):
        """Scan port range"""
        self.target = target
        
        # Resolve target if it's a domain
        self.target_ip = self.resolve_ip(target)
        if not self.target_ip:
            return False
        
        self.start_time = datetime.now()
        
        print(f"Scanning ports {start_port}-{end_port}...")
        print("="*60 + "\n")
        
        # Scan each port
        for port in range(start_port, end_port + 1):
            if self.scan_port(self.target_ip, port):
                service = self.get_service_name(port)
                print(f"✓ Port {port:<6} : {service:<15} [OPEN]")
                self.open_ports.append((port, service))
            
            # Show progress every 100 ports
            if port % 100 == 0 and port != end_port:
                elapsed = (datetime.now() - self.start_time).total_seconds()
                print(f"  └─ Progress: {port}/{end_port} ({elapsed:.1f}s)")
        
        self.end_time = datetime.now()
        return True
    
    def display_results(self):
        """Display scan results"""
        print("\n" + "="*60)
        print("📊 SCAN RESULTS")
        print("="*60 + "\n")
        
        if self.open_ports:
            print(f"✓ Found {len(self.open_ports)} OPEN port(s):\n")
            for port, service in sorted(self.open_ports):
                print(f"  Port {port:<6} : {service}")
        else:
            print("❌ No open ports found\n")
        
        print(f"\n✗ Closed ports scanned: {len(self.closed_ports)}")
        
        # Calculate scan time
        scan_time = self.end_time - self.start_time
        print(f"\n⏱️  Scan Time: {scan_time.total_seconds():.2f} seconds")
        print("="*60 + "\n")
    
    def run(self):
        """Main function"""
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
            
            # Run scan
            if self.scan_range(target, start_port, end_port):
                self.display_results()
        
        except ValueError:
            print("❌ Invalid input! Please enter numbers for ports.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Scan interrupted by user")
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    scanner = PortScanner()
    scanner.run()


if __name__ == "__main__":
    main()