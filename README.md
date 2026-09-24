# spoofie
## iOS Location Spoofer with Visual Map Interface

A lightweight, Python-based desktop application that lets you spoof your iPhone's GPS location using an interactive web map interface. Powered by pymobiledevice3 and FastAPI / Folium.

Features

🗺️ Interactive Web Map: Click anywhere on a Leaflet map to select a custom latitude and longitude.

🔌 USB Tethered Sync: Pushes mock GPS coordinates directly to your connected iPhone via Apple's DVT developer protocols.

⚡ Real-Time Update: Instant system-wide location override for Find My, Apple Maps, and other services.

Prerequisites

A Host Computer: A Windows PC (with iTunes/Apple Devices installed) or a Mac.

Python 3.8+ installed on your computer.

An iPhone running iOS with Developer Mode enabled (Settings > Privacy & Security > Developer Mode).

Project Structure

Create a folder on your computer named ios-location-spoofer and add the following files:

ios-location-spoofer/
├── requirements.txt
└── app.py

Installation
1. Clone or Download the Repository

Clone the repository and enter the project directory:

git clone <your-repository-url>
cd ios-location-spoofer

2. Install Dependencies

Open a terminal inside the project directory and run:

pip install -r requirements.txt

Requirements
requirements.txt
pymobiledevice3
fastapi
uvicorn
folium
pydantic

Connect Your iPhone

Connect your iPhone to your computer using a USB cable.

Unlock your iPhone.

Tap Trust when prompted.

Make sure Developer Mode is enabled:

Settings → Privacy & Security → Developer Mode

Running the Application
1. Start the Local Server

From the project directory, run:

python app.py


The application should start a local web server.

2. Open the Web Interface

Open a web browser on your computer and navigate to:

http://127.0.0.1:8000


An interactive map should load in your browser.

3. Select a Location

Use the interactive map to select a location. The application will use the selected latitude and longitude for the connected iPhone.

Note: Keep your iPhone connected to the computer via USB while using the application.

Troubleshooting
iPhone is not detected

Make sure:

Your iPhone is unlocked.

The USB cable supports data transfer.

You selected Trust This Computer on the iPhone.

Developer Mode is enabled.

Apple Devices/iTunes is installed on Windows when required.

The web interface doesn't load

Verify that the server is running:

python app.py


Then open:

http://127.0.0.1:8000


If port 8000 is already in use, stop the other application using it or configure your app to use a different port.

Usage

Once the application is running:

Connect your iPhone via USB.

Start the Python server.

Open the local web interface.

Select a location on the map.

The application will attempt to send the selected coordinates to the connected device.

Disclaimer

This project is intended for development, testing, and educational purposes. Location spoofing may affect location-based applications and services in unexpected ways.
