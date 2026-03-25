# Port Scanner 🔍

**Educational Port Scanning Tool for Network Security Learning**

## Project Status: 🟢 Phase 3 (CSV Export Complete!)

## What This Project Teaches

### Phase 1: Project Structure ✅
- Project organization
- Git initialization
- Professional documentation
- README creation

### Phase 2: Core Scanning Logic ✅
- **Network Fundamentals**
  - What ports are (network doors)
  - TCP/IP protocols
  - How services listen on ports
  - Socket programming basics

- **Python Skills**
  - Socket library usage
  - Network connections
  - Error handling
  - Timeout management

- **Security Concepts**
  - Port scanning methodology
  - Service enumeration
  - Open vs closed ports
  - Network reconnaissance

### Phase 3: CSV Export & Data Management ✅ (NEW!)
- **File Handling (Python)**
  - Creating folders automatically
  - Writing data to files
  - File path management
  - Error handling in file operations

- **CSV Module (Python)**
  - Structured data format
  - CSV Writer usage
  - Header creation
  - Data row insertion

- **Datetime Module (Python)**
  - Timestamp generation
  - Filename organization
  - Chronological tracking
  - Professional naming conventions

- **Real-world Security Skills**
  - How SOC analysts save reports
  - Vulnerability data storage
  - Professional documentation
  - Compliance report creation
  - Data organization for analysis

## How It Works

### User Input
```
Enter target (IP or domain): 127.0.0.1
Enter start port (default 1): 1
Enter end port (default 1000): 100
```

### Scanning Process
```
1. Resolve domain to IP (if needed)
2. Create results/ folder
3. For each port in range:
   - Try to connect
   - If connection succeeds → PORT OPEN
   - If connection fails → PORT CLOSED
4. Collect all open ports
5. Save to CSV file with timestamp
6. Display results
```

### Output Example

**Terminal Output:**
```
🔍 PORT SCANNER - Network Security Tool
============================================================

Enter target (IP or domain): 127.0.0.1
Enter start port (default 1): 1
Enter end port (default 1000): 100

✓ Resolved: 127.0.0.1 → 127.0.0.1

Scanning ports 1-100...
============================================================
✓ Port 22    : SSH        [OPEN]
✓ Port 80    : HTTP       [OPEN]
✓ Port 443   : HTTPS      [OPEN]

============================================================
📊 SCAN RESULTS
============================================================

✓ Found 3 OPEN port(s):

  Port 22   : SSH
  Port 80   : HTTP
  Port 443  : HTTPS

✗ Closed ports scanned: 97

⏱️  Scan Time: 45.23 seconds

✓ Results saved to: results/scan_127_0_0_1_2026-03-25_10-30-45.csv
============================================================
```

**CSV File Output (Open in Excel):**
```
Port,Service,Status
22,SSH,OPEN
80,HTTP,OPEN
443,HTTPS,OPEN
```

## Supported Services

| Port | Service | Purpose |
|------|---------|---------|
| 21 | FTP | File Transfer |
| 22 | SSH | Remote Access |
| 25 | SMTP | Email Sending |
| 53 | DNS | Domain Resolution |
| 80 | HTTP | Web Server |
| 110 | POP3 | Email Retrieval |
| 143 | IMAP | Email Access |
| 443 | HTTPS | Secure Web |
| 3306 | MySQL | Database |
| 5432 | PostgreSQL | Database |
| 8080 | HTTP-Alt | Alternate Web |

## Project Structure

```
PortScanner-Tool/
├── README.md                              # This file
├── requirements.txt                       # Dependencies
├── port_scanner.py                        # Main scanner code
└── results/                               # CSV exports folder
    ├── scan_127_0_0_1_2026-03-25_10-30-45.csv
    ├── scan_192_168_1_1_2026-03-25_11-15-22.csv
    └── scan_192_168_122_100_2026-03-25_12-45-10.csv
```

## Key Features Explained

### 1. Automatic Folder Creation
```python
def create_results_folder(self):
    if not os.path.exists(self.results_folder):
        os.makedirs(self.results_folder)
```
- Checks if results/ folder exists
- Creates it automatically if missing
- Prevents errors when saving CSV

**Why?** Professional tools organize output files. Keeps project clean!

### 2. Port Scanning Logic
```python
def scan_port(self, target_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    return result == 0
```
- Creates network socket (connection endpoint)
- Tries to connect to port
- Waits 1 second max (timeout)
- Returns True if successful (OPEN)

**Why?** This is how real network scanning works!

### 3. Service Identification
```python
self.services = {
    22: 'SSH',
    80: 'HTTP',
    443: 'HTTPS',
    3306: 'MySQL'
}
```
- Maps port numbers to service names
- Makes results human-readable
- Shows what's running on each port

**Why?** Security teams need to know WHAT service is open, not just the port!

### 4. CSV Export (PHASE 3)
```python
def save_to_csv(self, target, open_ports):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"scan_{target.replace('.', '_')}_{timestamp}.csv"
    
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Port', 'Service', 'Status'])
        writer.writeheader()
        for port in open_ports:
            writer.writerow({'Port': port, 'Service': service, 'Status': 'OPEN'})
```

**What happens:**
1. Creates timestamp (2026-03-25_10-30-45)
2. Creates filename: scan_127_0_0_1_2026-03-25_10-30-45.csv
3. Opens CSV file for writing
4. Writes header row: Port, Service, Status
5. Writes each open port as a row
6. Saves to results/ folder

**Why?** Professional reports! Data can be:
- Opened in Excel
- Shared with team
- Analyzed over time
- Used for compliance

## Phase 3 Learning Outcomes

### What You Learned ✅

**Python File Operations:**
- `os.path.exists()` - Check if folder exists
- `os.makedirs()` - Create folders
- `open()` - Write to files
- Context managers (`with` statement) - Safe file handling

**CSV Module:**
- `csv.DictWriter()` - Write structured data
- `writeheader()` - Create column headers
- `writerow()` - Add data rows
- Dictionary format - Easy data structure

**Datetime Module:**
- `datetime.now()` - Get current time
- `strftime()` - Format time as string
- Filename timestamps - Professional organization

**Security Concepts:**
- Report generation
- Data persistence
- Professional documentation
- Compliance tracking

### Real-world Application

**How SOC Analysts Use This:**
1. Scan network with tools like Nmap
2. Save results to CSV/JSON
3. Open in Excel for analysis
4. Create reports for management
5. Track changes over time
6. Document findings for compliance

**This project mimics that workflow!**

## How to Use

### Installation
```bash
# No external dependencies needed!
# Python built-in libraries only:
# - socket (networking)
# - time (timing)
# - os (file operations)
# - csv (data export)
# - datetime (timestamps)
```

### Run Scanner
```bash
python3 port_scanner.py
```

### Example Scan
```
Enter target (IP or domain): 192.168.1.1
Enter start port (default 1): 1
Enter end port (default 1000): 100
```

### View Results
1. Check terminal output for quick results
2. Open CSV file in Excel for detailed analysis:
   - `results/scan_192_168_1_1_2026-03-25_10-30-45.csv`
3. Share CSV with team for collaboration

## Phase 3 vs Phase 2

| Feature | Phase 2 | Phase 3 |
|---------|---------|---------|
| Scan ports | ✅ | ✅ |
| Display results | ✅ | ✅ |
| Save to file | ❌ | ✅ NEW! |
| Professional report | ❌ | ✅ NEW! |
| Data analysis | ❌ | ✅ NEW! |
| Excel integration | ❌ | ✅ NEW! |
| Automation ready | ❌ | ✅ NEW! |

## Important Notes

⚠️ **Legal Notice**
- Only scan networks/systems you own or have explicit permission
- Unauthorized port scanning may be illegal
- This is an educational tool for learning

🔒 **Security Best Practices**
- Don't share CSV files with sensitive IP addresses
- Keep results folder private
- Use .gitignore to prevent accidental commits

## Technologies Used

- **Python 3** - Main programming language
- **Socket Library** - Network communication
- **CSV Module** - Data export
- **Datetime Module** - Timestamps
- **OS Module** - File operations
- **Git** - Version control

## Project Timeline

```
Phase 1: ✅ Project Structure (Complete)
Phase 2: ✅ Scanning Logic (Complete)
Phase 3: ✅ CSV Export (Complete) ← YOU ARE HERE!
Phase 4: 🔄 Advanced Features (Next)
        - Threading for speed
        - Vulnerability detection
        - Email reports
        - Database integration
```

## How This Project Helps Your Career 🎯

### For SOC Analyst Roles
✅ Demonstrates network scanning knowledge
✅ Shows data management skills
✅ Proves report generation ability
✅ Shows automation understanding
✅ Real security tool experience

### For Cybersecurity Roles
✅ Network reconnaissance experience
✅ Data processing capability
✅ Professional documentation skills
✅ Python programming ability
✅ Real-world project portfolio

## What Employers See

```
"PortScanner Project"
       ↓
"This person can:"
  ✅ Write network scanning tools
  ✅ Manage security data
  ✅ Create professional reports
  ✅ Code in Python
  ✅ Handle file operations
  ✅ Use version control (Git)
       ↓
"Perfect for SOC Analyst role!"
```

## Next Steps

After Phase 3, you'll learn in Phase 4:
1. **Threading** - Scan 1000+ ports in seconds!
2. **Vulnerability Detection** - Identify weak services
3. **Email Reports** - Automatic report sending
4. **Database Integration** - Store results permanently

## Author

**Rishabh Raj** - Aspiring SOC Analyst
- Building portfolio projects phase by phase
- Learning real cybersecurity tools
- Documenting learning journey

## Resources

- Python Socket Documentation: https://docs.python.org/3/library/socket.html
- CSV Module Guide: https://docs.python.org/3/library/csv.html
- Port Numbers: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

## Happy Learning! 🚀

This project shows you how real security tools work. Keep building, keep learning! 💪

---

*Last Updated: Phase 3 - CSV Export Implementation*