# Port Tarayıcı

Bu Python programı, belirli bir IP adresindeki belirli bir port aralığını tarayarak açık portları tespit eder. Port tarama işlemi paralel olarak gerçekleştirilir, bu da işlemi hızlandırır.

**Özellikler:**

- Hedef IP adresi belirlenebilir.
- Tarama yapılacak port aralığı belirtilebilir.
- Açık olan portlar ekranda listelenir.
  
## Gereksinimler

- Python 3.9 veya daha üst sürümler
- `socket` ve `threading` kütüphaneleri (Python'un standart kütüphaneleridir, ekstra yükleme gerektirmez).
  
## Kullanım

1. `port_tarayici` klasörünü bilgisayarınıza indirin.
2. Terminal veya komut istemcisinde klasörün içindeki Main.py dosyasını çalıştırın:
    ```bash
    python Main.py
    ```
3. Hedef IP adresini ve port aralığını girin.
4. Program, belirtilen port aralığını tarar ve açık portları ekranda listeler.

## Kod Yapısı

- Main.py: Bu dosya, programın ana işlevselliğini içerir. Kullanıcıdan IP adresi ve port aralığı alır, ardından belirtilen aralıkta portları paralel olarak tarar ve açık olanları ekranda gösterir.

