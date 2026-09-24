# 🗺️ Spoofie: iOS Location Spoofer with Visual Map Interface

A lightweight, Python-based desktop application that lets you spoof your iPhone's GPS location using an interactive web map interface.

Built with `pymobiledevice3`, `FastAPI`, and `Folium`.

---

## ✨ Features

* **🗺️ Interactive Web Map:** Click anywhere on a Leaflet map to select a custom latitude and longitude.
* **🔌 USB Tethered Sync:** Communicates with a connected iPhone over USB.
* **⚡ Real-Time Updates:** Quickly apply new coordinates without restarting the application.
* **🌐 Local Web Interface:** Simple browser-based interface running locally on your computer.

---

## 📋 Prerequisites

Before getting started, make sure you have:
* A Windows PC or Mac.
* Python 3.8+ installed.
* An iPhone with Developer Mode enabled.
* A USB cable capable of data transfer.

### Enable Developer Mode
On your iPhone, go to:
> `Settings > Privacy & Security > Developer Mode`

Enable Developer Mode and restart your iPhone if prompted.

---

## 📁 Project Structure

Create a folder named `ios-location-spoofer`:

```text
ios-location-spoofer/
├── app.py
├── requirements.txt
└── README.md
