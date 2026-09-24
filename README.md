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
