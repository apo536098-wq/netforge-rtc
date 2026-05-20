# NetForge-RTC: WebRTC Packet Manipulation & Protocol Fuzzing Framework

This framework is developed as a graduation project for the Cybersecurity Technology program. It explores input validation, buffer management vulnerabilities, and packet injection scenarios in real-time communication protocols (WebRTC/RTP/RTCP), mapping out theoretical concepts derived from critical CVEs like CVE-2025-4122.

## 🎯 Project Objectives
- **Packet Injection:** Crafting custom RTP/RTCP headers using layer-3/4 packet crafting engines.
- **Protocol Fuzzing:** Testing application-level protocol parsers by mutating length indicators (e.g., Extension Header Length).
- **Anomalies Analysis:** Observing boundary check failures and boundary-handling mechanics in a restricted test lab environment (`BGT-Pentest-LAB`).

## 🛠️ Requirements & Setup
The core automation relies on Python 3 and the Scapy networking engine.

```bash
# Clone the repository
git clone [https://github.com/apo536098-wq/netforge-rtc.git](https://github.com/apo536098-wq/netforge-rtc.git)
cd netforge-rtc

# Install dependencies
pip install -r requirements.txt

# NetForge-RTC: WebRTC Packet Manipulation & Protocol Fuzzing Framework

This framework is developed as a graduation project for the Cybersecurity Technology program. It explores input validation, buffer management vulnerabilities, and packet injection scenarios in real-time communication protocols (WebRTC/RTP/RTCP), mapping out theoretical concepts derived from critical CVEs like CVE-2025-4122.

## 🎯 Project Objectives
- **Packet Injection:** Crafting custom RTP/RTCP headers using layer-3/4 packet crafting engines.
- **Protocol Fuzzing:** Testing application-level protocol parsers by mutating length indicators (e.g., Extension Header Length).
- **Anomalies Analysis:** Observing boundary check failures and boundary-handling mechanics in a restricted test lab environment (`BGT-Pentest-LAB`).

## 🛠️ Requirements & Setup
The core automation relies on Python 3 and the Scapy networking engine.

```bash
# Clone the repository
git clone [https://github.com/apo536098-wq/netforge-rtc.git](https://github.com/apo536098-wq/netforge-rtc.git)
cd netforge-rtc

# Install dependencies
pip install -r requirements.txt
