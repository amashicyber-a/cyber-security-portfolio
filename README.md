# cyber-security-portfolio
Hands-on cybersecurity projects including phishing simulation, network analysis, and intrusion detection.
# Cyber Security Portfolio – Amashi

## About Me
I am a second-year Cyber Security student at Victoria University Sydney. I am building hands-on skills in phishing simulation, network analysis, and intrusion detection.

My goal is to become a SOC Analyst in Australia, with a strong interest in banking security.

## Projects

### Phishing Attack Simulation
This project simulates a phishing attack targeting a banking system.

### Tools Used
- Kali Linux
- Flask
- Wireshark
- Suricata
- iptables
- OpenSSL

## Incident Analysis (SOC Perspective)

This project simulates a phishing attack targeting a banking system.

### Indicators of Compromise (IoCs)
- Suspicious HTTP POST request containing credentials
- Unencrypted traffic over port 80
- Repeated login attempts detected

### Detection
- Suricata IDS generated alerts for login activity

### Response
- Firewall rules blocked access to the malicious server

### Prevention
- HTTPS encryption implemented
- Recommendation: Multi-Factor Authentication (MFA)

## Attack Flow
Attacker → Phishing Page → Victim Login → Data Capture → IDS Alert → Firewall Block → HTTPS Secure

## Professional Security Statement
Network traffic analysis revealed credential transmission in plaintext over HTTP, indicating a critical security vulnerability.

## Real-World Banking Impact
This type of attack can lead to unauthorized banking access, financial loss, and reputational damage.

