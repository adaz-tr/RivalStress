import socket
import time
import sys
import os

# Windows terminal için UTF-8 ve renk desteği
if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    sys.stdout.reconfigure(encoding='utf-8')

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = f"""{Colors.BOLD}
\033[38;5;51m    ██████╗ {Colors.RESET}\033[38;5;87m██╗{Colors.RESET}\033[38;5;123m██╗   ██╗{Colors.RESET}\033[38;5;159m █████╗ {Colors.RESET}\033[38;5;195m██╗     {Colors.RESET}
\033[38;5;45m    ██╔══██╗{Colors.RESET}\033[38;5;81m██║{Colors.RESET}\033[38;5;117m██║   ██║{Colors.RESET}\033[38;5;153m██╔══██╗{Colors.RESET}\033[38;5;189m██║     {Colors.RESET}
\033[38;5;39m    ██████╔╝{Colors.RESET}\033[38;5;75m██║{Colors.RESET}\033[38;5;111m██║   ██║{Colors.RESET}\033[38;5;147m███████║{Colors.RESET}\033[38;5;183m██║     {Colors.RESET}
\033[38;5;33m    ██╔══██╗{Colors.RESET}\033[38;5;69m██║{Colors.RESET}\033[38;5;105m╚██╗ ██╔╝{Colors.RESET}\033[38;5;141m██╔══██║{Colors.RESET}\033[38;5;177m██║     {Colors.RESET}
\033[38;5;27m    ██║  ██║{Colors.RESET}\033[38;5;63m██║{Colors.RESET}\033[38;5;99m ╚████╔╝ {Colors.RESET}\033[38;5;135m██║  ██║{Colors.RESET}\033[38;5;171m███████╗{Colors.RESET}
\033[38;5;21m    ╚═╝  ╚═╝{Colors.RESET}\033[38;5;57m╚═╝{Colors.RESET}\033[38;5;93m  ╚═══╝  {Colors.RESET}\033[38;5;129m╚═╝  ╚═╝{Colors.RESET}\033[38;5;165m╚══════╝{Colors.RESET}

\033[38;5;196m╔═══════════════════════════════════════════════════════════════╗{Colors.RESET}
\033[38;5;196m║{Colors.RESET}                \033[38;5;226m{Colors.BOLD}📡 RIVAL PACKET RECEIVER 📡{Colors.RESET}                \033[38;5;196m║{Colors.RESET}
\033[38;5;196m║{Colors.RESET}                \033[38;5;208mDeveloped by \033[38;5;51m{Colors.BOLD}ADAZ_TR{Colors.RESET}                \033[38;5;196m║{Colors.RESET}
\033[38;5;196m╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def start_receiver(port=25565):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024) # 1MB safe buffer
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except: pass

    sock.settimeout(0.5) 
    
    try:
        # Önce tüm arayüzlere (0.0.0.0) bağlanmayı dene
        sock.bind(('0.0.0.0', port))
    except:
        try:
            # Alternatif olarak localhost'u dene
            sock.bind(('127.0.0.1', port))
        except Exception as e:
            print(f"\n{Colors.RED}❌ Hata: Port {port} bağlanamadı. {e}{Colors.RESET}")
            return

    print_banner()
    print(f"\033[38;5;51m📍 {Colors.BOLD}Port {port} dinleniyor...{Colors.RESET}")
    print(f"\033[38;5;240m[!] Eğer 127.0.0.1 paketlerini göremiyorsanız, stress aracı hedefini 'localhost' yapın.{Colors.RESET}")
    print(f"\033[38;5;240m[!] NOT: Çok yüksek hızlar işlemciyi kilitlerse paketler görünmeyebilir.{Colors.RESET}\n")

    total_received = 0
    total_bytes = 0
    start_time = time.time()
    last_check_time = start_time
    packets_in_last_second = 0
    bytes_in_last_second = 0
    last_addr = "Yok"
    first_packet_received = False
    heartbeat_chars = ["|", "/", "-", "\\"]
    hb_idx = 0

    try:
        while True:
            try:
                data, addr = sock.recvfrom(65535)
                
                if not first_packet_received:
                    first_packet_received = True
                    now = time.strftime("%H:%M:%S")
                    print(f"\n\n\033[38;5;46m{Colors.BOLD}[🚀] İLK PAKET YAKALANDI! - {now} - {addr[0]}:{addr[1]}{Colors.RESET}")
                
                total_received += 1
                packets_in_last_second += 1
                total_bytes += len(data)
                bytes_in_last_second += len(data)
                last_addr = f"{addr[0]}:{addr[1]}"
            except socket.timeout:
                pass

            current_time = time.time()
            if current_time - last_check_time >= 1.0:
                elapsed = current_time - start_time
                pps = packets_in_last_second / (current_time - last_check_time)
                mbps = (bytes_in_last_second * 8) / (current_time - last_check_time) / 1_000_000
                total_mb = total_bytes / 1_000_000
                
                hb = heartbeat_chars[hb_idx % 4]
                hb_idx += 1
                
                # İlk paket gelene kadar KIRMIZI, gelince YEŞİL
                status_color = "\033[38;5;46m" if first_packet_received else "\033[38;5;196m"
                
                stats_line = (
                    f"\r{status_color}{hb}{Colors.RESET} "
                    f"\033[38;5;51m📦 Alınan: \033[38;5;226m{total_received:,}{Colors.RESET} pk | "
                    f"\033[38;5;51m📈 Hız: \033[38;5;46m{pps:,.0f}{Colors.RESET} pps | "
                    f"\033[38;5;51m🌐 Bant: \033[38;5;201m{mbps:.2f}{Colors.RESET} Mbps | "
                    f"\033[38;5;250m📡 Son: \033[38;5;255m{last_addr}{Colors.RESET}"
                )
                print(stats_line, end="", flush=True)
                
                packets_in_last_second = 0
                bytes_in_last_second = 0
                last_check_time = current_time

    except KeyboardInterrupt:
        print(f"\n\n\033[44;37m{Colors.BOLD}  📊 ANALİZ RAPORU  {Colors.RESET}")
        print(f"\033[38;5;51m{'═' * 63}{Colors.RESET}")
        print(f"\033[38;5;46m✅ Toplam Paket: {total_received:,}{Colors.RESET}")
        print(f"\033[38;5;87m📦 Toplam Boyut: {total_bytes / 1_000_000:.2f} MB{Colors.RESET}")
        print(f"\033[38;5;226m📈 Ortalama Hız: {total_received / (time.time() - start_time) if time.time() - start_time > 0 else 0:,.0f} pps{Colors.RESET}")
        print(f"\033[38;5;51m{'═' * 63}{Colors.RESET}")
        sock.close()

if __name__ == "__main__":
    try:
        print_banner()
        p_input = input(f"\033[38;5;51m[\033[38;5;87m?\033[38;5;51m]{Colors.RESET} \033[38;5;159mDinlenecek Port (Varsayılan 25565): \033[38;5;226m{Colors.RESET}").strip()
        port = int(p_input) if p_input else 25565
        start_receiver(port)
    except ValueError:
        print(f"\n{Colors.RED}❌ Hata: Port numarası rakam olmalıdır!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ HATA OLUŞTU: {e}{Colors.RESET}")
    finally:
        print()
        input(f"\033[38;5;244mKapatmak için ENTER'a basın...{Colors.RESET}")
