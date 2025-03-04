import subprocess
import winreg
import os
import shutil
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Gets the current width of the terminal."""
    return shutil.get_terminal_size((80, 20)).columns

def print_banner():
    """Prints a centered ASCII banner."""
    banner_lines = [
        " .d8888b. 88888888888 8888888 8888888888 8888888888 ",
        "d88P  Y88b    888       888   888        888        ",
        "Y88b.         888       888   888        888        ",
        " \"Y888b.      888       888   8888888    8888888    ",
        "    \"Y88b.    888       888   888        888        ",
        "      \"888    888       888   888        888        ",
        "Y88b  d88P    888       888   888        888        ",
        " \"Y8888P\"     888     8888888 888        888        ",
        "",
        "Windows System Hardening Checker",
        "     by Malachi Rewane"
    ]

    width = get_terminal_width()
    for line in banner_lines:
        print(line.center(width))

    print("-" * width)

def loading_screen():
    """Display a loading screen with dots and a message."""
    print("Please ensure this script is running as Administrator.")
    time.sleep(3)
    for i in range(8):
        clear_screen()
        print("Loading" + "." * (i % 4 + 1))
        time.sleep(1)

def check_firewall():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True)
        return "Firewall is enabled" if "State ON" in result.stdout else "Firewall is disabled"
    except Exception as e:
        return f"Error checking firewall: {e}"

def check_antivirus():
    try:
        result = subprocess.run(['wmic', 'antivirusproduct', 'get', 'displayName'], capture_output=True, text=True)
        
        if 'displayName' in result.stdout:
            return "Antivirus is installed"
        else:
            return "No antivirus detected. The antivirus may not be installed, or it may not be registered in the system registry."
    except FileNotFoundError:
        return "Error checking antivirus: File not found. This may be due to missing `wmic` tool or lack of system permissions."
    except PermissionError:
        return "Error checking antivirus: Permission error. Please run the script as an administrator to access the required system tools."
    except Exception as e:
        return f"Error checking antivirus: {e}. This could be due to missing registry keys, issues accessing `wmic`, or problems with the antivirus software itself."

def check_uac():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
        value, _ = winreg.QueryValueEx(key, "EnableLUA")
        return "UAC is enabled" if value == 1 else "UAC is disabled"
    except Exception as e:
        return f"Error checking UAC: {e}"

def check_windows_update():
    try:
        result = subprocess.run(['sc', 'query', 'wuauserv'], capture_output=True, text=True)
        return "Windows Update service is running" if "RUNNING" in result.stdout else "Windows Update service is not running"
    except Exception as e:
        return f"Error checking Windows Update: {e}"

def check_remote_desktop():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Control\\Terminal Server")
        value, _ = winreg.QueryValueEx(key, "fDenyTSConnections")
        return "Remote Desktop is disabled" if value == 1 else "Remote Desktop is enabled"
    except Exception as e:
        return f"Error checking Remote Desktop: {e}"

def main():
    if os.name != 'nt':
        print("This script is only for Windows systems.")
        return
    
    loading_screen()

    while True:
        clear_screen()
        print_banner()
        print("Choose an option:".center(get_terminal_width()))
        print("1. Check Firewall".center(get_terminal_width()))
        print("2. Check Antivirus".center(get_terminal_width()))
        print("3. Check UAC (User Account Control)".center(get_terminal_width()))
        print("4. Check Windows Update Service".center(get_terminal_width()))
        print("5. Check Remote Desktop Status".center(get_terminal_width()))
        print("6. Run All Checks".center(get_terminal_width()))
        print("7. Exit".center(get_terminal_width()))
        
        choice = input("\nEnter your choice (1-7): ")

        clear_screen()
        
        if choice == '1':
            print(check_firewall().center(get_terminal_width()))
        elif choice == '2':
            print(check_antivirus().center(get_terminal_width()))
        elif choice == '3':
            print(check_uac().center(get_terminal_width()))
        elif choice == '4':
            print(check_windows_update().center(get_terminal_width()))
        elif choice == '5':
            print(check_remote_desktop().center(get_terminal_width()))
        elif choice == '6':
            print("\nRunning all security checks...\n")
            print(check_firewall().center(get_terminal_width()))
            print(check_antivirus().center(get_terminal_width()))
            print(check_uac().center(get_terminal_width()))
            print(check_windows_update().center(get_terminal_width()))
            print(check_remote_desktop().center(get_terminal_width()))
        elif choice == '7':
            print("Exiting... Stay secure! 🔒")
            os.system('exit')
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")
        
        input("\nPress Enter to return to menu...")

    os.system('exit')

if __name__ == "__main__":
    main()
