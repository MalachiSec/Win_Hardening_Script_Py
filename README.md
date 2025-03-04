<p align="center">
<img src="https://github.com/MalachiSec/Win_Hardening_Script_Py/blob/284e625406735644b86054ff93f30eb1f3cabfb2/Screenshot%202025-03-04%20054850.png"/>
</p>

# Windows System Hardening Checker 

This Python script helps you check and secure key security settings on your Windows system. The tool performs several checks related to system hardening and security:

- Firewall status
- Antivirus status
- UAC (User Account Control) status
- Windows Update service status
- Remote Desktop status

It can also run all checks in one go or execute them individually.

## Features

- **Firewall check:** Verifies if the firewall is enabled.
- **Antivirus check:** Detects if antivirus software is installed.
- **UAC check:** Checks whether UAC (User Account Control) is enabled.
- **Windows Update check:** Verifies if Windows Update service is running.
- **Remote Desktop check:** Ensures that Remote Desktop is disabled.

## Prerequisites

- Python 3.x
- Administrator privileges for some system checks

## Usage

### Running the Script

1. Open Command Prompt **as Administrator**.
2. Navigate to the directory where your script is located.
3. Run the script using the following command:

   ```bash
   python hardening_check.py
