from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    """
    Analyzes and prints details of a captured packet.
    """
    print("-" * 80)
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        
        if TCP in packet:
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        
        elif UDP in packet:
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        
        elif ICMP in packet:
            print("Protocol: ICMP")
            print(f"Type: {packet[ICMP].type}")
            print(f"Code: {packet[ICMP].code}")

        # Display raw payload if present
        if packet.payload:
            print(f"Payload: {bytes(packet.payload).decode('utf-8', errors='ignore')}")
    else:
        print("Non-IP packet captured")

def start_sniffing(interface=None, packet_count=10):
    """
    Starts sniffing packets on the specified network interface.
    """
    print("Starting packet capture...")
    sniff(iface=interface, prn=analyze_packet, count=packet_count, store=False)
    print("Packet capture finished.")

# Main program
if __name__ == "__main__":
    print("Packet Network Analyzer")
    interface = input("Enter the network interface to sniff on (e.g., eth0, wlan0, lo): ")
    packet_count = int(input("Enter the number of packets to capture: "))
    
    try:
        start_sniffing(interface=interface, packet_count=packet_count)
    except KeyboardInterrupt:
        print("\nSniffing stopped by user.")
    except Exception as e:
        print(f"Error: {e}")