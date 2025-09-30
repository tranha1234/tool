import re,os,time,re,json,uuid,random,sys
ban = """\033[1;32m

██╗  ██╗███╗   ██╗    ██╗   ██╗██╗██████╗ ██████╗ ██████╗  ██████╗ 
██║  ██║████╗  ██║    ██║   ██║██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
███████║██╔██╗ ██║    ██║   ██║██║██████╔╝██████╔╝██████╔╝██║   ██║
██╔══██║██║╚██╗██║    ╚██╗ ██╔╝██║██╔═══╝ ██╔═══╝ ██╔══██╗██║   ██║
██║  ██║██║ ╚████║     ╚████╔╝ ██║██║     ██║     ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                
                TOOL GHÉP CHUỖI + LỌC CHUỖI COOKIE                                                 
                        
                        AUTHOR : NAM DZ
"""
def banner():
    for h in ban:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.001)
banner()
def process_cookie(file_name):
    # Lấy đường dẫn file trong thư mục hiện tại
    file_path = os.path.join(os.getcwd(), file_name)

    # Đọc file cookie
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Chuẩn hóa: thay ":" thành "=" cho đồng bộ
    cookie_string = "; ".join(
        line.strip().replace(": ", "=").replace(":", "=")
        for line in lines if line.strip()
    )

    # Tìm đoạn từ c_user tới datr
    match = re.search(r"(c_user=.*?datr=[^;]+)", cookie_string)
    if match:
        result = match.group(1)
    else:
        result = "❌ Không tìm thấy c_user hoặc datr trong cookie!"

    print("\n✅ Kết quả cookie:")
    print(result)


if __name__ == "__main__":
    file_name = input("\nNhập tên file cookie (vd: cookie.txt): ").strip()  
    os.system("cls" if os.name == "nt" else "clear")
    process_cookie(file_name)
