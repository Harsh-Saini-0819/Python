# Python-Packet-sniffer

A simple Python-based network tool that captures and analyzes live IP traffic.

🚀FEATURES :

Real-time Capture: Identifies TCP, UDP, and ICMP protocols.
Traffic Analysis: Extracts source/destination IP addresses and calculates payload sizes.
Lightweight: Uses the Scapy library for efficient packet processing.


⚠️PRE_REQUISITES :

install scapy using - pip install scapy
install Npcap from npcap.com
Run terminal as Administrator

📂CONFIGURATION :

Modify the sniff() function at the bottom of the script to change:
    count: Number of packets to capture.
    iface: The specific network interface to monitor (e.g., "eth0" or "Wi-Fi").