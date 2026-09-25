# 🗺️ Spoofie: iOS Location Spoofer with Visual Map Interface

A lightweight, Python-based desktop application that lets you spoof your iPhone's GPS location using an interactive web map interface. Powered by `pymobiledevice3` and `FastAPI` / `Folium`.

## Features
* 🗺️ **Interactive Web Map:** Click anywhere on a Leaflet map to select a custom latitude and longitude.
* 🔌 **USB Tethered Sync:** Pushes mock GPS coordinates directly to your connected iPhone via Apple's DVT developer protocols.
* ⚡ **Real-Time Update:** Instant system-wide location override for Find My, Apple Maps, and other services.

---

## Prerequisites

1. **A Host Computer:** A Windows PC (with iTunes/Apple Devices installed) or a Mac.
2. **Python 3.8+** installed on your computer.
3. **An iPhone** running iOS with **Developer Mode** enabled (`Settings > Privacy & Security > Developer Mode`).
   - Enable Developer Mode (No Xcode/Mac Required)
      - Modern iOS versions require Developer Mode to be active. You can enable this directly from your PC using pymobiledevice3:
      - python -m pymobiledevice3 amfi enable-developer-mode
      - Next Steps: Restart your iPhone when prompted, unlock it with your passcode, and tap "Turn On" on the system prompt that appears on your phone screen.
         - If it says: failed to connect to usbmuxd socket
            - Install iTunes from the Microsoft Store (this installs the necessary Apple device drivers for Windows).
            - Open the Windows Start Menu, type Services, and open the app.
            - Find Apple Mobile Device Service, right-click it, and click Start (or Restart).
            - Unplug your iPhone, plug it back in, unlock it, and tap Trust.
            - Run your command again in PowerShell: 
---

## Project Structure

Create a folder on your computer named `ios-location-spoofer` and add two files inside it:
1. `requirements.txt`
2. `app.py`

---

### 1. `requirements.txt`
```text
pymobiledevice3
fastapi
uvicorn
folium
pydantic
```

---

## Step-by-Step Installation & Execution

1. **Install dependencies:**  
   Open your command line inside your project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

2. Connect your iPhone:
   - Plug your iPhone into your computer using a USB cable.
   - Unlock your phone and tap "Trust" when prompted.
   - Ensure Developer Mode is turned on (Settings > Privacy & Security > Developer Mode).


3. Run the local app server:
   ```bash
   python app.py
   ```

4. Use your custom tool:
   - Open a web browser on your computer and go to: http://127.0.0.1:8000
   - An interactive map will load. Click on any street or building to instantly spoof your iPhone's global location!



## Prerequisites for Windows Users
Because this tool communicates directly with iOS developer testing sockets, it relies on system-level libraries that require a C compiler on Windows. 

### If you encounter a `Microsoft Visual C++ 14.0 or greater is required` error during `pip install`:
1. Download and install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. During installation, check the box for **"Desktop development with C++"**.
3. Complete the installation and restart your terminal:
   - cd spoofie
   - Set-ExecutionPolicy Unrestricted -Scope Process;
   - pip install -r requirements.txt
   - python app.py
  
### If you are using Python 3.14 (cp314)
   - deactivate
   - Remove-Item -Recurse -Force venv
   - py -3.12 -m venv venv
   - Set-ExecutionPolicy Unrestricted -Scope Process; .\venv\Scripts\Activate.ps1
   - pip install -r requirements.txt
   - python app.py
