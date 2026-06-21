# RIVAL STRESS

<div align="center">

```
    ██████╗ ██╗██╗   ██╗ █████╗ ██╗     
    ██╔══██╗██║██║   ██║██╔══██╗██║     
    ██████╔╝██║██║   ██║███████║██║     
    ██╔══██╗██║╚██╗ ██╔╝██╔══██║██║     
    ██║  ██║██║ ╚████╔╝ ██║  ██║███████╗
    ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
```

---


## ⚠️ Disclaimer

This project was developed solely for educational, research, performance testing, and software engineering purposes.

The project is intended to demonstrate concepts such as:

* Network programming
* Multi-threading and concurrency
* Performance measurement and monitoring
* Terminal user interface development
* System architecture and testing methodologies

The author does not encourage, endorse, or take responsibility for any misuse of this software. Users are solely responsible for ensuring that all activities involving this project comply with applicable laws, regulations, and the authorization policies of the systems they interact with.

By using this software, you acknowledge that it is provided **"as is"**, without any warranty of any kind, and that the author shall not be held liable for any direct, indirect, incidental, or consequential damages arising from its use.

**This repository is published for educational and testing purposes only.**





**Ultra Premium Minecraft Server Ağ Yönetim ve İşlem Aracı**

*Developed by ADAZ_TR*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📋 İçindekiler

- [Sistem Özellikleri](#-sistem-özellikleri)
- [Sistem Gereksinimleri](#-sistem-gereksinimleri)
- [Kurulum Yapılandırması](#-kurulum-yapılandırması)
- [İşlem Akışı](#-işlem-akışı)
- [Teknik Parametreler](#-teknik-parametreler)
- [Mimari Detaylar](#-mimari-detaylar)
- [Performans Metrikleri](#-performans-metrikleri)
- [Sıkça Sorulan Sorular](#-sss)

---

## ✨ Sistem Özellikleri

### 🎨 **Arayüz Yönetimi**
- ✅ **Gradient ASCII Engine** - 256 renk derinlikli görselleştirme
- ✅ **Gerçek Zamanlı Veri İzleme** - Milisaniyelik işlem takibi
- ✅ **Dinamik Terminal Çıktısı** - Optimize edilmiş görsel geri bildirim
- ✅ **İstatistiksel Analiz Modülü** - Anlık ağ verisi hesaplama

### 🚀 **Performans Motoru**
- ✅ **Asenkron Thread Yönetimi** - 200 eşzamanlı işlem kapasitesi
- ✅ **Paket Boyutu Optimizasyonu** - Özel yapılandırılabilir veri blokları
- ✅ **Kesintisiz Veri Akışı** - Yüksek frekanslı UDP paket dağıtımı
- ✅ **DNS Çözümleme Katmanı** - Dinamik hostname çözümleme

### 🔧 **Teknik Altyapı**
- ✅ **UDP Protokol Yönetimi** - Ağ katmanı veri iletimi
- ✅ **Multi-Threading Mimarisi** - Kaynak kullanım optimizasyonu
- ✅ **Hata Yakalama Sistemi** - Gelişmiş exception yönetimi
- ✅ **Çapraz Platform Desteği** - Modüler işletim sistemi uyumluluğu

---

## 💻 Sistem Gereksinimleri

### **Donanım Gereksinimleri**
```
- İşlemci: Eşzamanlı thread yönetimini destekleyen modern işlemci
- Bellek: 2 GB ve üzeri RAM
- Bağlantı: Veri akışı hızına uygun ağ kartı
```

### **Yazılım Gereksinimleri**
```
- Çalışma Zamanı: Python 3.8 veya üzeri
- İşletim Sistemi: Windows 10/11, Linux, macOS
- Terminal: ANSI renk kodlarını destekleyen modern konsol
```

---

## 📦 Kurulum Yapılandırması

### **1. Çalışma Zamanı Kurulumu**

#### Windows (PowerShell):
```powershell
winget install Python.Python.3.10
```

#### Linux (Shell):
```bash
sudo apt update && sudo apt install python3
```

### **2. Dosya Yapılandırması**

```bash
# Proje dizinine erişim
cd rival-stress

# Standart kütüphanelerin kontrolü
python --version
```

---

## 🎮 İşlem Akışı

### **Başlatma Talimatları**

```powershell
# Standart Başlatma
python rival_stress.py
```

### **Yapılandırma Adımları**

1. **Hedef Belirleme**
   - Hedef makine adresi ve port girişi gerçekleştirilir.

2. **Parametre Ayarları**
   - Veri bloğu boyutu, işlem sayısı (thread) ve işlem süresi belirlenir.

3. **Doğrulama**
   - Belirlenen konfigürasyon onaylanarak işlem sırasına alınır.

4. **Veri Analizi**
   - İşlem sonrasında elde edilen pps ve Mbps değerleri raporlanır.

---

## ⚙️ Teknik Parametreler

### **Konfigürasyon Tablosu**

| Parametre | Minimum | Maksimum | Varsayılan | İşlev |
|-----------|---------|----------|------------|-------|
| **Paket Boyutu** | 1 byte | 65,507 byte | 32,768 byte | Ağ katmanı veri yoğunluğu |
| **Thread Sayısı** | 1 | 200 | 50 | Eşzamanlı işlem yoğunluğu |
| **İşlem Süresi** | 1 saniye | 120 saniye | 30 saniye | Toplam işlem periyodu |

---

## 🔬 Mimari Detaylar

### **İletişim Katmanı**
- **Protokol**: UDP (User Datagram Protocol) - Bağlantısız veri iletimi
- **Veri Yapısı**: Ham veri bloğu (Raw socket stream)

### **Sistem Mimarisi**
```
┌─────────────────────────────────────────┐
│         RIVAL STRESS SYSTEM             │
├─────────────────────────────────────────┤
│  Kontrol Merkezi (Main Thread)          │
│  ├─ DNS Çözümleme Modülü                │
│  ├─ Konfigürasyon Denetleyici           │
│  └─ İstatistik Toplayıcı                │
│                                         │
│  Veri İşleyiciler (Worker Threads)      │
│  ├─ Thread 1 → Socket Operations        │
│  ├─ Thread 2 → Socket Operations        │
│  └─ ...                                 │
│                                         │
│  Görsel İzleme (Monitor Thread)         │
│  └─ Dinamik İşlem Çubuğu                │
└─────────────────────────────────────────┘
```

---

## 📊 Performans Metrikleri

### **Veri Analiz Tablosu**

| Metrik | Teknik Tanım | Birim |
|--------|--------------|-------|
| **PPS** | Saniyedeki Paket Sayısı | packets/second |
| **Mbps** | Megabit İletim Hızı | megabits/second |
| **Veri Hacmi** | Toplam İletilen Veri | MB/GB |

---

## 🛠️ İşlem Kanıtı ve Doğrulama

Sistemin gerçekten paket gönderdiğini kanıtlamak için 3 farklı yöntem kullanabilirsiniz:

### **Yöntem 1: Yerel Yakalayıcı (Receiver Check)**
Proje içindeki `receiver_check.py` scriptini kullanarak paketlerin ulaştığını anlık olarak görebilirsiniz:
1. Bir terminal açın ve çalıştırın: `python receiver_check.py` (Port: 9999 seçin)
2. İkinci bir terminal açın ve `rival_stress.py` çalıştırın.
3. Hedef IP olarak `127.0.0.1`, Port olarak `9999` girin.
4. Yakalayıcı terminalinde paketlerin saniyede binlerce kez aktığını göreceksiniz.

### **Yöntem 2: Windows Kaynak İzleyicisi**
Herhangi bir ek program indirmeden doğrulamak için:
1. `Ctrl + Shift + Esc` ile Görev Yöneticisi'ni açın.
2. **Performans** sekmesine geçin ve alt kısımdaki **"Kaynak İzleyicisini Aç"** bağlantısına tıklayın.
3. **Ağ** sekmesine gelin.
4. `python.exe` sürecinin saniyede kaç **Bayt/sn** veri gönderdiğini "Ağ Etkinliği" kısmından görebilirsiniz.

### **Yöntem 3: Wireshark**
En kesin kanıt yöntemidir:
1. [Wireshark](https://www.wireshark.org/) indirin ve ağ kartınızı dinlemeye başlayın.
2. Filtre kısmına `udp.port == 25565` yazın.
3. İşlemi başlattığınızda ağ kartınızdan çıkan binlerce UDP paketini, kaynak ve hedef adresleriyle birlikte canlı olarak görebilirsiniz.

---

## 🛠️ Sorun Giderme

### **Sistemsel Durumlar**

#### **DNS Çözümleme Sorunları**
- Adresin erişilebilirliğini ve DNS sunucu yanıtlarını kontrol ediniz.

#### **Performans Kayıpları**
- Ağ kartı kapasitesini ve işlemci thread limitlerini gözden geçiriniz.

---

## 💡 Sıkça Sorulan Sorular

**S: Maksimum işlem kapasitesi nedir?**  
C: Donanım ve ağ bant genişliği limitlerine bağlı olarak değişkenlik gösterir.

**S: Neden sadece UDP kullanılıyor?**  
C: Düşük gecikmeli ve yüksek hacimli veri akışını simüle etmek için optimize edilmiştir.

**S: Sistem kaynaklarını nasıl etkiler?**  
C: Multi-threading yapısı sayesinde işlemci çekirdeklerine dağıtılmış, dengeli bir yük oluşturur.


---

## 👨‍💻 Geliştirici

**ADAZ_TR**

- Discord: adaz_tr
- Herhangi bir sorunda ulaşabilirsiniz.

---

## 🙏 Teşekkürler

RIVAL STRESS kullandığınız için teşekkürler! 

<div align="center">

** RIVAL STRESS - Ultra Premium Sistem İşlem Aracı **

*Made with ❤️ by ADAZ_TR*

</div>
