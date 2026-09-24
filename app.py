import asyncio
import os
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import folium

from pymobiledevice3.lockdown import create_living_lockdown_client
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxy
from pymobiledevice3.services.dvt.instruments.location_simulation import LocationSimulation

app = FastAPI()

class Coordinates(BaseModel):
    lat: float
    lon: float

async def apply_gps_simulation(lat: float, lon: float):
    """Asynchronously pushes coordinates to the tethered iOS device."""
    try:
        async with create_living_lockdown_client() as lockdown:
            async with DvtSecureSocketProxy(lockdown) as dvt:
                loc_sim = LocationSimulation(dvt)
                loc_sim.set(lat, lon)
                print(f"[SUCCESS] Location updated to: Lat {lat}, Lon {lon}")
    except Exception as e:
        print(f"[ERROR] Failed to update location. Ensure phone is unlocked, trusted, and Developer Mode is active. Details: {e}")

@app.get("/", response_class=HTMLResponse)
async def index():
    """Generates an interactive map interface where clicking a point sets the location."""
    # Default center map view (e.g., New York / customizable)
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
    
    # Add a custom JavaScript click handler to send coordinates back to the server
    click_script = """
    <script>
        // Listen for map clicks to trigger location updates automatically
        document.addEventListener("DOMContentLoaded", function() {
            // Leaflet map object injection hack for custom UI binding
            let mapObject = window.map; 
            if(mapObject) {
                mapObject.on('click', function(e) {
                    let lat = e.latlng.lat;
                    let lon = e.latlng.lng;
                    
                    fetch('/set-location', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({lat: lat, lon: lon})
                    })
                    .then(response => response.json())
                    .then(data => {
                        alert('Location spoofed to: ' + lat.toFixed(4) + ', ' + lon.toFixed(4));
                    });
                });
            }
        });
    </script>
    """
    
    # Render map to HTML string
    map_html = m._repr_html_()
    
    page_content = f"""
    <html>
        <head>
            <title>iOS Location Spoofer</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f4f4f9; }}
                h2 {{ color: #333; }}
                .container {{ max-width: 900px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>iOS Local GPS Spoofer</h2>
                <p>Plug in your iPhone, trust this computer, enable Developer Mode, and <b>click anywhere on the map below</b> to teleport your device.</p>
                {map_html}
            </div>
            {click_script}
        </body>
    </html>
    """
    return HTMLResponse(content=page_content)

@app.post("/set-location")
async def update_location(coords: Coordinates, background_tasks: BackgroundTasks):
    background_tasks.add_task(apply_gps_simulation, coords.lat, coords.lon)
    return {"status": "processing", "lat": coords.lat, "lon": coords.lon}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
