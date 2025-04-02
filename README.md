```markdown
# VMware Horizon Client Automation Script

Automate VMware Horizon Client login and virtual machine launch using Python and PyAutoGUI.

## Overview

This script automates the process of:
1. Launching VMware Horizon Client
2. Selecting a pre-configured account
3. Logging in with stored credentials
4. Launching the HD Platinum virtual machine

Uses Windows credential manager for secure password storage and image recognition for UI navigation.

## Features

- 🔒 Secure credential storage using `keyring`
- 🖥️ Image recognition for UI navigation
- ⏱️ Configurable timeouts and retries
- 🚀 Automatic VM launch
- ⚠️ Built-in failsafe (move mouse to corner to abort)

## Prerequisites

- Python 3.7+
- VMware Horizon Client installed
- Windows OS
- Monitor resolution: 1920x1080 (or customize image templates)

## Installation

1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/vmware-automation.git
   cd vmware-automation
   ```

2. Install dependencies:
   ```bash
   pip install pyautogui opencv-python keyring
   ```

## Setup

1. **Store Credentials** (first-time setup):
   ```bash
   python vmware_auto.py --set-password
   ```
   - Follow prompts to enter password and account number
   - Credentials stored in Windows Credential Manager

2. **Create Image Templates**:
   - Capture screenshots of these UI elements:
     - `cloud_icon.png` - VMware cloud connection icon
     - `hd_text.png` - "HD Platinum" text in VM list
   - Save images in project root directory

## Usage

```bash
python vmware_auto.py
```

**Script Flow:**
1. Opens Start Menu and launches VMware Horizon Client
2. Double-clicks cloud connection icon
3. Enters stored account number
4. Automates login process
5. Launches HD Platinum VM
6. Provides real-time status updates in console

## Configuration

| File           | Description                                  |
|----------------|----------------------------------------------|
| `cloud_icon.png` | VMware Horizon cloud connection icon (70% confidence) |
| `hd_text.png`    | HD Platinum VM text (80% confidence)         |

**Adjustable Parameters:**
```python
# In script:
pyautogui.PAUSE = 0.5  # Delay between actions
timeout=30             # Image search timeout
confidence=0.8         # Image recognition accuracy
```

## Safety Features

- Failsafe enabled: Move mouse to any corner to abort
- Built-in delays between actions
- Clear console feedback for each step
- Error handling with descriptive messages

## Troubleshooting

**Common Issues:**
1. *"Image not found" errors*
   - Check image file names and paths
   - Adjust confidence threshold:
     ```python
     wait_and_click('image.png', confidence=0.7)
     ```
   - Update screenshot templates for your resolution

2. *Timing issues*
   - Increase sleep durations:
     ```python
     time.sleep(5)  # Increase as needed
     ```

3. *Credential errors*
   - Re-run setup:
     ```bash
     python vmware_auto.py --set-password
     ```

## License

MIT License
