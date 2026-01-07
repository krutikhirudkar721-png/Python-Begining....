# Python Begining.
# PERSINAL INFORMATION PROGRAM

import time
import sys

# --- 1. My Personal Data ---
# I used a dictionary here to keep things organized
my_info = {
    "Name": "Krutik Hirudkar",
    "Age": 20,
    "Location": "India 🇮🇳",
    "Hobby": "Exploring new things 🔍",
    "Subject": "Math 📐",
    "Future Goal": "Become a good engineer 🚀",
    "Favorite Food": "Pizza 🍕",
    "Favorite Color": "Blue 🟦"
}

# --- 2. My Engineering Progress Logic ---
# I added this function to show I can write my own logic
def show_progress(goal_name, current_percent):
    print(f"\n📊 Current Goal: {goal_name}")
    bar_size = 20
    filled = int(bar_size * current_percent / 100)
    bar = "█" * filled + "-" * (bar_size - filled)
    print(f"[{bar}] {current_percent}% Complete")

# --- 3. The Main Display ---
def main():
    print("==========================================")
    print(f"👋 WELCOME TO {my_info['Name'].upper()}'S PROFILE")
    print("==========================================\n")
    
    # Printing info using a simple loop
    for key, value in my_info.items():
        print(f"➤ {key:<15}: {value}")
        time.sleep(0.1)  # Adding a tiny delay to make it look like a real terminal loading

    # Adding a special section for my coding status
    likes_coding = True
    status = "YES! 💻" if likes_coding else "Not yet"
    print(f"➤ Likes Coding   : {status}")

    # Showing my real-time progress
    show_progress("Improving Python Skills", 65) 

    print("\n" + "="*42)
    print("🚀 Built by Krutik | Follow for more projects!")
    print("="*42)

if __name__ == "__main__":
    main()

