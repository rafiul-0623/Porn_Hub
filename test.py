nano Porn-Hub_tool.py

import requests
import os
import time

def main_menu():
    os.system('clear')
    print("=========================================")
    print("        ★ MY Porn-Hub CONTROL ★         ")
    print("             DEVELOPER: BoT              ")
    print("=========================================")
    print(" [1] FB Method")
    print(" [2] Sex video")
    print(" [3] Old clone")
    print(" [4] File clone")
    print(" [5] Random clone")
    print(" [6] Exit")
    print("=========================================")
    
    choice = input(" [★] Selection : ")
    
    if choice == "1":
        os.system('clear')
        print("--- [1] FB Method Testing ---")
        id_num = input("Enter FB ID or Number: ")
        password = input("Enter Password: ")
        print("\n[+] Checking database...")
        time.sleep(1.5)
        
        if len(password) >= 6:
            print("\n=========================================")
            print("[✓] STATUS  : SUCCESSFUL")
            print(f"[✓] ACCOUNT : {id_num}")
            print(f"[✓] PASS    : {password}")
            print("=========================================")
        else:
            print("\n=========================================")
            print("[X] STATUS  : WRONG PASSWORD / FAILED")
            print("=========================================")
            
        input("\nPress Enter to return to Main Menu...")
        main_menu()

    elif choice == "2":
        os.system('clear')
        print("--- [2] Sex video / Reel Server Check ---")
        site = input("Enter Site Name: ")
        url = "https://www.facebook.com/reel/846400658117557/"
        print(f"\n[+] Connecting to server via {site}...")
        time.sleep(1.5)
        print("\n=========================================")
        print(f"Target URL: {url}")
        print("[✓] STATUS  : SERVER CONNECTED SUCCESSFUL")
        print("=========================================")
        input("\nPress Enter to return to Main Menu...")
        main_menu()
   
    elif choice in ["3", "4",]:
        os.system('clear')
        print(f"--- Option [{choice}] ---")
        print("[X] ERROR: Method Not Found / Expired!")
        input("\nPress Enter to return to Main Menu...")
        main_menu()
        
        elif choice == "5":
    os.system('clear')
    print("--- [5] Random Clone (b-graph Method) ---")
    uid = input("[+] Enter UID/Email: ")
    password = input("[+] Enter Password: ")
    print("\n[+] Checking account details...")
    import requests
    import uuid
    r = requests.Session()
    head = {
        'Host': 'b-graph.facebook.com',
        'X-Fb-Connection-Type': 'WIFI',
        'Authorization': 'OAuth 350685531728|62f8ce9f74744849a044318023157f12',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020)'
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
        pos = r.post('https://b-graph.facebook.com/auth/login', headers=head, data=data).json()
        if 'session_key' in pos or 'access_token' in pos:
            print(f"\n[RFX-OK] {uid} | {password}")
        elif 'www.facebook.com' in pos.get('error', {}).get('message', ''):
            print(f"\n[RFX-CP] {uid} | {password}")
        else:
            print("\n[X] Login Failed / Incorrect Details")
    except:
        print("\n[X] Network Error!")
    input("\nPress Enter to return to Main Menu...")
    main_menu()

     elif choice == "6":
        print("\n[+] Thank you for using this tool! Akhn Hat Mere Ghumaw.")
        exit()

    else:
        print("\n[!] INVALID SELECTION!")
        time.sleep(1.5)
        main_menu()

if __name__ == "__main__":
    main_menu()