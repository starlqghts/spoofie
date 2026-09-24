🗺️ spoofie
iOS Location Spoofer with Visual Map Interface

A lightweight, Python-based desktop application that lets you spoof your iPhone's GPS location using an interactive web map interface.

Built with pymobiledevice3, FastAPI, and Folium.

✨ Features

🗺️ Interactive Web Map — Click anywhere on a Leaflet map to select a custom latitude and longitude.

🔌 USB Tethered Sync — Communicates with a connected iPhone over USB.

⚡ Real-Time Updates — Quickly apply new coordinates without restarting the application.

🌐 Local Web Interface — Simple browser-based interface running locally on your computer.

📋 Prerequisites

Before getting started, make sure you have:

A Windows PC or Mac.

Python 3.8+ installed.

An iPhone with Developer Mode enabled.

A USB cable capable of data transfer.

Enable Developer Mode

On your iPhone, go to:

Settings > Privacy & Security > Developer Mode

Enable Developer Mode and restart your iPhone if prompted.

📁 Project Structure

Create a folder named ios-location-spoofer:

ios-location-spoofer/
├── app.py
├── requirements.txt
└── README.md

📦 Installation
1. Clone the Repository
git clone <your-repository-url>
cd ios-location-spoofer

2. Install Dependencies
pip install -r requirements.txt

📄 requirements.txt
pymobiledevice3
fastapi
uvicorn
folium
pydantic

📱 Connect Your iPhone

Connect your iPhone to your computer using a USB cable.

Unlock your iPhone.

Tap Trust when prompted.

Make sure Developer Mode is enabled.

Make sure your computer can communicate with the connected device.

🚀 Running the Application

Start the local server from the project directory:

python app.py


Then open your browser and go to:

http://127.0.0.1:8000

🗺️ Using the Map

Once the web interface loads:

Navigate around the interactive map.

Click on a street or building.

Select your desired location.

The application will use the selected coordinates for the connected iPhone.

Keep your iPhone connected via USB while using the application.

🔧 Troubleshooting
iPhone Not Detected

Make sure:

Your iPhone is unlocked.

Your USB cable supports data transfer.

You selected Trust This Computer.

Developer Mode is enabled.

Required Apple device software/drivers are installed.

Web Interface Doesn't Load

Make sure the server is running:

python app.py


Then visit:

http://127.0.0.1:8000

Dependency Errors

Try upgrading pip:

python -m pip install --upgrade pip


Then reinstall the dependencies:

pip install -r requirements.txt

🛠️ Tech Stack

🐍 Python

⚡ FastAPI

🗺️ Folium

📱 pymobiledevice3

🌐 Leaflet

🔌 Apple DVT Developer Protocols

⚠️ Disclaimer

This project is intended for development, testing, and educational purposes.

Use this software only with devices you own or have permission to modify. Location spoofing may affect location-based applications and services and may violate their terms of service.

The authors are not responsible for misuse of this software or any consequences resulting from its use.

📜 License

Add your preferred license here.

For example:

MIT License
