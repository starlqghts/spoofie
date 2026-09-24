🗺️ spoofie
iOS Location Spoofing with an Interactive Map

spoofie is a lightweight Python application that provides a visual map interface for selecting custom GPS coordinates for a connected iPhone.

Built with Python, FastAPI, Folium, and pymobiledevice3.

⚠️ Development / Testing Project
Designed for development, testing, and educational use with devices you own or have permission to modify.

✨ Features
Feature	Description
🗺️ Interactive Map	Select a location visually using a Leaflet-powered map
📍 Custom Coordinates	Choose precise latitude and longitude coordinates
🔌 USB Connection	Communicates with a connected iPhone over USB
⚡ Fast Updates	Apply new coordinates without restarting the application
🐍 Python Based	Simple setup using a lightweight Python stack
💻 Local Web UI	Runs entirely through a local browser interface
🖥️ Prerequisites

Before getting started, make sure you have:

💻 Windows or macOS

🐍 Python 3.8+

📱 An iPhone

🔧 Developer Mode enabled

🔌 A USB cable capable of data transfer

Enable Developer Mode

On your iPhone, go to:

Settings
└── Privacy & Security
    └── Developer Mode


Enable Developer Mode and restart the device if prompted.

📦 Installation
1. Clone the Repository
git clone <your-repository-url>
cd ios-location-spoofer

2. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

📁 Project Structure

Your project should look something like this:

ios-location-spoofer/
│
├── 📄 app.py
├── 📄 requirements.txt
└── 📄 README.md

📋 Requirements

The project uses the following Python packages:

requirements.txt
pymobiledevice3
fastapi
uvicorn
folium
pydantic

📱 Connect Your iPhone

Before starting the application:

Connect your iPhone to your computer using USB.

Unlock your iPhone.

If prompted, select Trust This Computer.

Make sure Developer Mode is enabled.

On Windows, ensure the required Apple device drivers/software are installed.

Your computer should be able to communicate with the connected iPhone before continuing.

🚀 Running spoofie
Start the Server

From the project directory, run:

python app.py


Once the server starts, open your browser and visit:

http://127.0.0.1:8000

🗺️ Using the Map

Once the web interface loads:

┌──────────────────────────────────────┐
│                                      │
│              🗺️ MAP                  │
│                                      │
│          📍 Select Location          │
│                                      │
│                                      │
└──────────────────────────────────────┘


Open the local web interface.

Navigate around the map.

Select your desired location.

The application uses the selected coordinates for the connected device.

Keep the iPhone connected via USB while using the application.

🔧 Troubleshooting
📱 iPhone isn't detected

Check the following:

iPhone is unlocked.

USB cable supports data transfer.

Trust This Computer was accepted.

Developer Mode is enabled.

Required Apple device software/drivers are installed.

Try disconnecting and reconnecting the iPhone.

🌐 Web interface won't load

Make sure the application is running:

python app.py


Then visit:

http://127.0.0.1:8000


If port 8000 is already being used by another application, configure the server to use another available port.

🐍 Python dependency errors

Try upgrading pip before installing the requirements:

python -m pip install --upgrade pip


Then:

pip install -r requirements.txt

🛠️ Tech Stack

🐍 Python

⚡ FastAPI

🗺️ Folium

📱 pymobiledevice3

🌐 Leaflet

🔌 Apple DVT developer protocols

🔄 Basic Workflow
        ┌───────────────┐
        │   🖥️ Computer  │
        └───────┬───────┘
                │
                │ USB
                ▼
        ┌───────────────┐
        │   📱 iPhone   │
        └───────────────┘

                ▲
                │
                │ Coordinates
                │
        ┌───────┴───────┐
        │  🗺️ Web Map   │
        │    :8000      │
        └───────────────┘

⚠️ Disclaimer

spoofie is provided for development, testing, and educational purposes.

Use the software only with devices you own or have explicit permission to modify. Location spoofing can affect location-dependent applications and services and may violate the terms of some services.

The authors are not responsible for misuse of this software or for any consequences resulting from its use.

⭐ Contributing

Contributions, bug reports, and improvements are welcome.

If you'd like to contribute:

git checkout -b feature/my-feature


Make your changes, test them, and submit a pull request.

📄 License

Add your preferred license here, for example:

MIT License


See LICENSE for details.
