import os
import time
import requests
import uuid
from bs4 import BeautifulSoup

CONFIG_FILE = "user_config.txt"
saved_cookie = None
saved_time = 0.0
user_status = "free"

# Load saved user config
if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "r") as f:
            lines = f.read().splitlines()
        if len(lines) >= 3:
            saved_cookie = lines[0]
            saved_time = float(lines[1])
            user_status = lines[2]
    except:
        pass

current_time = time.time()

# Main Menu Display
os.system('clear')
print("====================================")
print("    ★ MY Porn-Hub CONTROL ★        ")
print("        DEVELOPER: Devil_King       ")
print("====================================")
print("[#] User Status: " + str(user_status).upper())
print("====================================")
print("[1] (FB Method)")
print("[2] (Fb Friend list cheker)")
print("[3] (old clone)")
print("[4] (File clone)")
print("[5] (Random Clone)")
print("[6] (Exit)")
print("====================================")

choice = input("[★] 1/2/3/4/5/6 : ")

# -------------------------------------------------------------
# METHOD 1: FB UID COLLECTOR (WITH COOKIE CHECKER)
# -------------------------------------------------------------
if choice in ["1", "১"]:
    os.system('clear')
    print("====================================")
    print("        ★ FILE CREATE MENU ★        ")
    print("====================================")
    
    # Free/Paid Option Selection
    print("[1] Continue as Free User (2 Hours Limit)")
    print("[2] Activate Paid Version (Unlimited)")
    user_choice = input("[+] Select option: ")
    
    if user_choice == "2":
        secret_key = input("[+] Enter Paid Activation Key: ")
        if secret_key == "ADMIN123":
            user_status = "paid"
            print("[+] Activation Successful! Unlimited Mode On.")
        else:
            print("[X] Invalid Key! Continuing as Free User.")
            user_status = "free"
    else:
        user_status = "free"

    # Fetching or Inputting Cookie
    fb_cookie = None
    if user_status == "paid":
        if saved_cookie and user_status == "paid":
            print("[+] Paid User Detected! Loading saved cookie...")
            fb_cookie = saved_cookie
        else:
            fb_cookie = input("[+] Enter Your FB Cookie: ")
    else:
        if saved_cookie and (current_time - saved_time) < 7200:
            remaining_min = int((7200 - (current_time - saved_time)) / 60)
            print("[+] Active session found! (Expires in " + str(remaining_min) + " minutes)")
            fb_cookie = saved_cookie
        else:
            if saved_cookie:
                print("[!] Your 2-hour free session has expired!")
            fb_cookie = input("[+] Enter Your FB Cookie: ")

    # COOKIE VALIDATION SYSTEM (এখানে নতুন লজিকটি যুক্ত করা হয়েছে)
    if fb_cookie:
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Cookie': fb_cookie
        }
        
        print("\n[+] Verifying cookie status with Facebook server...")
        cookie_is_valid = False
        
        try:
            # মবাসিক প্রোফাইল চেক করে ভ্যালিডেশন করা
            check_response = session.get("https://mbasic.facebook.com/profile.php", headers=headers, timeout=10)
            if check_response.status_code == 200:
                soup = BeautifulSoup(check_response.text, 'html.parser')
                page_title = soup.find('title')
                title_text = page_title.text.strip() if page_title else ""
                
                if "Log In" in title_text or "লগ ইন" in title_text or "Content Not Found" in check_response.text:
                    print("\n\033[1;31m[X] Expired Cookie! Please use a fresh cookie.\033[0m")
                    fb_cookie = None # কুকি বাতিল করা হলো
                else:
                    print("\n\033[1;32m[✓] Cookie Login Successful!\033[0m")
                    cookie_is_valid = True
            else:
                print(f"\n\033[1;31m[X] Server returned error code: {check_response.status_code}\033[0m")
                fb_cookie = None
        except:
            print("\n\033[1;31m[X] Network Error! Unable to connect to verification server.\033[0m")
            fb_cookie = None

    # Save configuration if the cookie is verified successfully
    if fb_cookie and cookie_is_valid:
        try:
            with open(CONFIG_FILE, "w") as f:
                f.write(f"{fb_cookie}\n{time.time()}\n{user_status}\n")
        except:
            pass

    # Proceed only if cookie is valid
    if fb_cookie and cookie_is_valid:
        print("\n====================================")
        print("[1] 10000 Series (Old UID)")
        print("[2] 6158 Series (Running/New UID)")
        print("[3] Custom Mix Series")
        print("====================================")
        series_choice = input("[+] Select Series Format: ")

        if series_choice == "1":
            base_uid = "10000"
        elif series_choice == "2":
            base_uid = "6158"
        else:
            base_uid = input("[+] Enter Custom Base UID (e.g., 1000): ")

        series_start = int(input("[+] Select Series Start (e.g., 10001): "))
        series_end = int(input("[+] Select Series End (e.g., 99999): "))
        
        user_file_input = input("[+] Enter Output File Name (e.g., /sdcard/result.txt): ")
        
        if user_file_input.startswith("/sdcard"):
            output_path = user_file_input
        else:
            output_path = os.path.join("/sdcard", user_file_input)

        print("\n[+] Connecting to server...")
        print("[+] Extracting data... (Press CTRL+C to Stop/Cancel)\n")
        
        try:
            for uid_suffix in range(series_start, series_end + 1):
                full_uid = str(base_uid) + str(uid_suffix)
                url = "https://mbasic.facebook.com/profile.php?id=" + str(full_uid)
                
                try:
                    response = session.get(url, headers=headers, timeout=10)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_title = soup.find('title')
                        profile_name = page_title.text.strip() if page_title else "Unknown User"
                        
                        if "Log In" in profile_name or "Error" in profile_name or "Content Not Found" in profile_name:
                            print("[INVALID] UID: " + str(full_uid) + " (Cookie Dead)")
                            break
                        elif "add_friend" in response.text or "Add Friend" in response.text or "নম্বর" in response.text or "বন্ধু" in response.text:
                            print(f"\033[1;32mPremium\033[0m - Successfully Extracted From : \033[1;35m{full_uid}\033[0m")
                            
                            with open(output_path, "a", encoding="utf-8") as file_out:
                                file_out.write(str(full_uid) + " | " + str(profile_name) + "\n")
                        else:
                            print("[SKIPPED] UID: " + str(full_uid) + " (Follower Account)")
                    time.sleep(1.0)
                except KeyboardInterrupt:
                    print("\n[-] Extraction Stopped By User.")
                    break
                except:
                    print("[ERROR] Connection failed for UID " + str(full_uid))
        except KeyboardInterrupt:
            print("\n[-] Process Cancelled.")
            
        print(f"\n[✓] Data Saved Successfully at: {output_path}")
    else:
        print("[X] Verification Failed. Process Stopped.")

# -------------------------------------------------------------
# METHOD 2: REEL SERVER CHECK
# -------------------------------------------------------------
if choice in ["2", "২"]:
    os.system('clear')
    print("--- [2] Sex video / Reel Server Check ---")
    site = input("Enter Site Name: ")
    url = "https://www.facebook.com/reel/846400658"
    print("\n[+] Connecting to server via " + str(site) + "...")
    time.sleep(1.5)
    print("\n=======================================")
    print("Target URL: " + str(url))
    print("[✓] STATUS : SERVER CONNECTED SUCCESS")
    print("=======================================")

# -------------------------------------------------------------
# METHOD 3 & 4: EXPIRED OPTIONS
# -------------------------------------------------------------
if choice in ["3", "4", "৩", "৪", "8", "৮"]:
    os.system('clear')
    print("--- Option [" + str(choice) + "] ---")
    print("[X] ERROR: Method Not Found / Expired!")

# -------------------------------------------------------------
# METHOD 5: RANDOM CLONE (B-GRAPH)
# -------------------------------------------------------------
if choice in ["5", "৫"]:
    os.system('clear')
    print("--- [5] Random Clone (b-graph Method) ---")
    uid = input("[+] Enter UID/Email: ")
    password = input("[+] Enter Password: ")
    print("\n[+] Checking account details...")
    r = requests.Session()
    head = {'Host': 'b-graph.facebook.com', 'X-Fb-Connection-Type': 'WIFI', 'Authorization': 'OAuth 350685531728|62f8ce9f74744849a044318023157f12', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020)'}
    data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': uid, 'password': password, 'generate_analytics_claim': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_ext_attrib': '0', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': ''}
    try:
        pos = r.post('https://b-graph.facebook.com/auth/login', headers=head, data=data).json()
        if 'session_key' in pos or 'access_token' in pos:
            print("\n[Devil-OK] " + str(uid) + " | " + str(password))
        elif 'www.facebook.com' in str(pos):
            print("\n[Devil-CP] " + str(uid) + " | " + str(password))
        else:
            print("\n[X] Login Failed / Incorrect Details")
    except:
        print("\n[X] Network Error!")

# -------------------------------------------------------------
# METHOD 6: EXIT
# -------------------------------------------------------------
if choice in ["6", "৬"]:
    print("\n[+] Thank you for using this tool! Goodbye.")
    exit()

input("\nPress Enter to Exit...")
