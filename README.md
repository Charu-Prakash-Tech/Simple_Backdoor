# Simple Backdoor

Simple Backdoor is a Python-based project that demonstrates remote command execution using a client-server architecture. It uses socket programming for communication and the `subprocess` module to execute system commands. 

---

## ⚠️ Disclaimer
This project is **strictly for educational purposes only**. It is designed to help users understand the basics of socket programming and subprocess usage in Python. **Misusing this tool for malicious or unauthorized activities is illegal and unethical. Always ensure you have proper permissions before using it.**

---

## How It Works
1. The **server** listens for incoming connections on a specified IP address and port.
2. The **client** connects to the server and sends system commands as encoded messages.
3. The server executes the received commands on the local system and returns the results to the client.

---

## Usage Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/simple-backdoor.git
cd simple-backdoor
