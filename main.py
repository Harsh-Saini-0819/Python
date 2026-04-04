from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = "Other"

        # Identify the protocol
        if packet.haslayer(TCP):
            proto = "TCP"
            payload = len(packet[TCP].payload)
        elif packet.haslayer(UDP):
            proto = "UDP"
            payload = len(packet[UDP].payload)
        elif packet.haslayer(ICMP):
            proto = "ICMP"
            payload = len(packet[ICMP].payload)
        else:
            payload = "N/A"

        print(f"[{proto}] {src_ip} -> {dst_ip} | Size: {payload} bytes")
print("--- Starting Packet Sniffer ---")
print("Note: Run as sudo/Administrator to capture traffic.")
# sniff() arguments:
# prn: function to apply to each packet
sniff(prn=process_packet, store=0, count = 50)

