import requests, time, sys, os
from rich.panel import Panel
from rich.console import Console
from colorama import Fore, Style, init as cinit

cinit(autoreset=True)
console = Console()

API_URL = "http://10.210.157.77:5000" 

def call_api(choice, link):
    params = {"choice": choice, "link": link}
    r = requests.get(API_URL, params=params, timeout=60)
    try:
        return r.json()
    except Exception:
        return {"status":"error","message":"Không parse được JSON","raw":r.text}

def countdown(seconds):
    for i in range(seconds, 0, -1):
        mm, ss = divmod(i, 60)
        sys.stdout.write(f"\r{Fore.YELLOW}{Style.BRIGHT}Delay {mm:02d}:{ss:02d}...{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r" + " " * 50 + "\r")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    menu = """[1] View TikTok  
[2] Like TikTok  
[3] Follow TikTok  
[4] Like Fanpage Facebook  
[5] Like Instagram"""
    console.print(Panel(menu, title="", border_style="yellow"))

    choice = input(Fore.YELLOW + "👉 Chọn (1-5): " + Style.RESET_ALL).strip()  
    link = input("Nhap link di thang em: ")
  
    while True:
        result = call_api(choice, link)
        print(f"Ket qua: {result} ")   
        if "Lên đơn thành công" in result:
            print("Buff success 🤡")
        if "delay" in result:
            print("Dang countdown...")
            countdown(result["delay"])
            continue
        if "Bạn đang có đơn đang chạy miễn phí, vui lòng chờ đơn hàng chạy xong rồi mới mua tiếp." in result:
            print("Dang countdown...")
            countdown(600)
            continue 
        if "Kênh này có video đang trong quá trình tăng. Vui lòng mua lại sau khi đơn đã báo trạng thái " in result:
            print("Dang countdown...")
            countdown(600)
            continue 
        if "bạn đang có tiến trình lên đơn với dịch vụ này, vui lòng chờ hoàn thành tiến trình cũ trước khi tạo đơn hàng mới" in result: 
            print("Dang countdown...")
            countdown(600)
            continue 

        else:
           countdown(20)
           continue 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}{Style.BRIGHT}⏹ Dừng bởi người dùng.{Style.RESET_ALL}")
