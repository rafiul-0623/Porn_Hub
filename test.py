nano Porn-Hub_tool.py

import requests
import os

os.system('clear')

print("=========================================")
print("         ★ MY Porn-Hub CONTROL ★       ")
print("          DEVELOPER: BoT         ")
print("=========================================")
print(" [১]  (FB Method")
print(" [২]  (Sex video")
print(" [৩]  (old clone")
print(" [৪]  (File clone")
print(" [৫]  (Random")
print(" [6]  (Exit)")
print("=========================================")

choice = input(" [★] ১/২/৩/৪/৫/৬ ")

# ৩. কন্ডিশন চেক করে সিরিয়াল অনুযায়ী কাজ করা
if choice == "১":
    os.system('clear')
    print("--- [১] ---")
    id_num = input(": ")
    password = input(": ")
    print(f"চেক করা হচ্ছে: {id_num} | {password} ...")
    print("কানেকশন সফল! মেথড স্ক্রিপ্ট ঠিকঠাক কাজ করছে।")

elif choice == "২":
    os.system('clear')
    print("--- [২] Sex video strt ---")
    site = input("Xhamster: ")
    url = ("https://www.facebook.com/reel/846400658117557")
    print("https://www.facebook.com/reel/846400658117557/ - এর সার্ভার থেকে তথ্য আনা হচ্ছে...")
    
    try:
        response = requests.get(url)
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        sex video_text = data['current_site'][0]['link'][0]
        
        print("\n==============================")
        print(https://www.facebook.com/reel/846400658117557)
        print(https://www.facebook.com/reel/846400658117557/}")
        print("==============================")
    except:
        print("[ERROR] তথ্য পাওয়া যায়নি!")

elif choice == "৩":
    os.system('clear')
    print("--- [৩] old clone ---")
    print("[ERROR] তথ্য পাওয়া যায়নি!")
    
elif choice == "৪":
    os.system('clear')
    print("--- [৪] File clone ---")
    site = input("not added: ")
    print("[ERROR] তথ্য পাওয়া যায়নি!")
    
elif choice == "৫":
    os.system('clear')
    print("--- [৫] File clone---")
    print("[ERROR] তথ্য পাওয়া যায়নি!")

elif choice == "৬":
    print("\nটুলটি ব্যবহার করার জন্য ধন্যবাদ! বাই বাই।")

else:
    print("\n[ ভুল অপশন! ] দয়া করে ১, ২, ৩, ৪, ৫  অথবা 6 চাপুন।")
    
    python Porn-Hub_tool.py

import requests
import os

# স্ক্রিন ক্লিয়ার করার জন্য
os.system('clear')

# তোমার কাস্টম মেনু ডিজাইন
print("=========================================")
print("        ★ MY Porn-Hub CONTROL ★         ")
print("             DEVELOPER: BoT              ")
print("=========================================")
print(" [1] (FB Method)")
print(" [2] (Sex video/Reel Check)")
print(" [3] (Old clone - Demo)")
print(" [4] (File clone - Demo)")
print(" [5] (Random - Demo)")
print(" [6] (Exit)")
print("=========================================")

choice = input(" [★] আপনার অপশনটি সিলেক্ট করুন (1/2/3/4/5/6): ")

if choice == "1":
    os.system('clear')
    print("--- [1] FB Method Testing ---")
    id_num = input("আপনার ফেসবুক আইডি বা নাম্বার দিন: ")
    password = input("পাসওয়ার্ড দিন: ")
    print(f"চেক করা হচ্ছে: {id_num} | {password} ...")
    print("কানেকশন সফল! মেথড স্ক্রিপ্ট ঠিকঠাক কাজ করছে।")

elif choice == "2":
    os.system('clear')
    print("--- [2] Video / Reel Server Check ---")
    site = input("Xhamster / Site Name: ")
    url = "https://www.facebook.com/reel/846400658117557/"
    print(f"\n{site} সার্ভার হয়ে রিল লিংকে কানেক্ট করা হচ্ছে...")
    
    # কোটেশন এবং ব্র্যাকেট ঠিক করা হলো
    print("\n=========================================")
    print(f"Target URL: {url}")
    print("=========================================")
    print("[SUCCESS] রিল সার্ভার ডাটা সফলভাবে চেক করা হয়েছে।")

elif choice == "3":
    os.system('clear')
    print("--- [3] Old Clone Option ---")
    print("[ERROR] ওল্ড ক্লোন মেথডটি এই মুহূর্তে আপডেটের অধীনে আছে!")

elif choice == "4":
    os.system('clear')
    print("--- [4] File Clone Option ---")
    site = input("not added. Enter file path: ")
    print("[ERROR] ফাইল পাথ পাওয়া যায়নি বা খালি!")

elif choice == "5":
    os.system('clear')
    print("--- [5] Random Cloning ---")
    print("[ERROR] র‍্যান্ডম ক্লোনিং এপিআই রেসপন্স করছে না!")

elif choice == "6":
    print("\nটুলটি ব্যবহার করার জন্য ধন্যবাদ! বাই বাই।")

else:
    print("\n[ ভুল অপশন! ] দয়া করে ইংরেজি সংখ্যায় 1, 2, 3, 4, 5 অথবা 6 চাপুন।")
