from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n=== Packet Captured ===")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

        if packet.payload:
            print("Payload:")
            print(bytes(packet.payload))

print("Starting packet capture... Press Ctrl+C to stop.")

sniff(prn=packet_callback, store=False)