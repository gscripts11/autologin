import pyautogui
import time
import keyring
import sys
from getpass import getpass

# Safety feature - move mouse to corner to abort
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def wait_and_click(image_name, timeout=30, confidence=0.8, double_click=False):
    """Wait for an image to appear and click it"""
    print(f"Looking for {image_name}...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_name, confidence=confidence)
            if location:
                if double_click:
                    pyautogui.doubleClick(location)
                else:
                    pyautogui.click(location)
                return True
        except pyautogui.ImageNotFoundException:
            time.sleep(0.2)
            continue
    
    return False

def start_vmware():
    """Start VMware Horizon Client using Windows search"""
    print("Starting VMware Horizon Client...")
    pyautogui.press('win')
    time.sleep(0.5)
    
    pyautogui.typewrite('vmware horizon', interval=0.01)
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(2)
    
    print("Looking for cloud icon...")
    if not wait_and_click('cloud_icon.png', confidence=0.7, double_click=True):
        raise Exception("Couldn't find cloud icon")

def select_account():
    """Select the correct account"""
    account_number = keyring.get_password("vmware_auto", "account_number")
    if not account_number:
        raise Exception("No account number found. Please run with --set-password to set it up")
        
    print("Waiting for account selection...")
    time.sleep(4)
    print("Additional wait for screen to load...")
    time.sleep(4)  # Increased from 2 to 4 seconds
    
    pyautogui.typewrite(account_number, interval=0.01)
    pyautogui.press('enter')

def handle_login(password):
    """Handle the password entry"""
    print("Waiting for password field...")
    time.sleep(2)
    
    pyautogui.press('tab')
    time.sleep(0.5)
    
    print("Entering password...")
    pyautogui.typewrite(password, interval=0.01)
    time.sleep(0.5)
    pyautogui.press('enter')
    
    print("Waiting for login to complete...")
    time.sleep(3)

def launch_hd_platinum():
    """Launch the HD Platinum VM using image recognition"""
    print("Waiting for VMs to load...")
    time.sleep(5)
    
    print("Looking for HD Platinum...")
    try:
        location = pyautogui.locateCenterOnScreen('hd_text.png', confidence=0.8)
        if location:
            print("Found HD Platinum")
            pyautogui.moveTo(location.x, location.y, duration=0.2)
            pyautogui.doubleClick()
            return
        else:
            raise Exception("Could not find HD Platinum")
    except Exception as e:
        print(f"Search failed: {str(e)}")
        raise

def set_password():
    """Set up the password in the keyring"""
    password = getpass("Enter your password (it will be stored securely): ")
    account_number = getpass("Enter your account number (it will be stored securely): ")
    keyring.set_password("vmware_auto", "horizon_login", password)
    keyring.set_password("vmware_auto", "account_number", account_number)
    print("Password and account number saved securely.")
    return True

def main():
    """Main automation routine"""
    # Get password from keyring
    password = keyring.get_password("vmware_auto", "horizon_login")
    if not password:
        print("No password found. Please run the script with --set-password to set it up:")
        print("py vmware_auto.py --set-password")
        return

    try:
        print("Starting automation...")
        time.sleep(1)
        
        start_vmware()
        select_account()
        handle_login(password)
        launch_hd_platinum()
        print("Script completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("You can move your mouse to any corner of the screen to abort the script.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--set-password':
        set_password()
    else:
        main()
