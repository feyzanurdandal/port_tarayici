import socket
import threading

def port_tarama(ip, baslangic_portu, bitis_portu):
    print(f"Port taraması başlatılıyor: {ip} adresi için {baslangic_portu}-{bitis_portu} aralığı.")
    acik_portlar = []

    def tarama(port):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        sonuc = soket.connect_ex((ip, port))
        if sonuc == 0:
            acik_portlar.append(port)
        soket.close()

    threadler = []
    for port in range(baslangic_portu, bitis_portu + 1):
        t = threading.Thread(target=tarama, args=(port,))
        threadler.append(t)
        t.start()

    for t in threadler:
        t.join()

    if acik_portlar:
        print(f"Açık portlar: {acik_portlar}")
    else:
        print("Açık port bulunamadı.")

ip_adresi = input("Hedef IP adresini girin: ")
baslangic_portu = int(input("Başlangıç portunu girin: "))
bitis_portu = int(input("Bitiş portunu girin: "))

port_tarama(ip_adresi, baslangic_portu, bitis_portu)
