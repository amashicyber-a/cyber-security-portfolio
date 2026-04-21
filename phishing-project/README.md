# Phishing Attack Simulation

## Overview
This project demonstrates how phishing attacks can capture user credentials in a simulated banking environment.

## Project Scenario
A fake FinSecure Bank login page was created using Flask to simulate credential harvesting. The project then applied multiple defensive controls to detect and prevent the attack.

## Tools Used
- Flask
- Kali Linux
- Wireshark
- Suricata
- iptables
- OpenSSL

## Attack Flow
Attacker → Phishing Page → Victim Login → Data Capture → IDS Alert → Firewall Block → HTTPS Secure

## Incident Analysis (SOC Perspective)

### Indicators of Compromise (IoCs)
- Suspicious HTTP POST request containing credentials
- Unencrypted traffic over port 80
- Repeated login attempts detected

### Detection
Suricata IDS generated alerts when suspicious login traffic was observed.

### Response
Firewall rules were applied to block access to the phishing server.

### Prevention
HTTPS encryption was implemented to protect credentials in transit.
Multi-Factor Authentication (MFA) is recommended.

## Real-World Banking Impact
This type of phishing attack can lead to unauthorized account access, financial fraud, and reputational damage.

## 📸 Project Screenshots

### 🚫 Port Block (iptables)
![Port Block](block%20port%208080.png)

### 🔐 Firewall Block
![Firewall](firewall%20block.png)

### 💻 Flask Credential Capture
![Flask](flask%20terminal%20log.png)

### 🔒 HTTPS Secure Page
![HTTPS](https.png)

### 📄 Login Result Page
![Login](login%20result%20page.png)

### 🌐 Nmap Scan
![Nmap](Nmap.png)

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/amashicyber-a/cyber-security-portfolio.git
cd cyber-security-portfolio/phishing-project
pip install flask
python3 app.py
```

Open browser:
http://127.0.0.1:8080

---

## 💻 Project Code

### 🔹 Flask Backend (app.py)

This file handles the web server and captures user credentials submitted through the phishing login page.

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')

    print(f"[Captured] Username: {username} | Password: {password}")

    return "Login Failed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### 🔹 Frontend Login Page (index.html)

```html
<form action="/login" method="post">
    <input type="text" name="username" placeholder="Enter Email" required>
    <input type="password" name="password" placeholder="Enter Password" required>
    <button type="submit">Login</button>
</form>
```

---

## What I Learned

- How phishing attacks capture user credentials
- Building a web application using Flask
- Monitoring network traffic using Wireshark
- Detecting attacks using Suricata IDS
- Implementing firewall rules using iptables
- Securing web applications using HTTPS

---

## Security Improvements

- Enforced HTTPS using SSL certificates
- Blocked malicious traffic using iptables firewall rules
- Detected suspicious activity using Suricata
- Identified open ports using Nmap
- Reduced attack surface by restricting unnecessary services

---

## ⚠️ Disclaimer

This project is created for educational purposes only. It demonstrates how phishing attacks work in a controlled environment to improve cybersecurity awareness and defense strategies.


