import asyncio
import os
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import folium

from pymobiledevice3.lockdown import create_using_usbmux

app = FastAPI()

class Coordinates(BaseModel):
    lat: float
    lon: float

async def apply_gps_simulation(lat: float, lon: float):
    try:
        proc = await asyncio.create_subprocess_exec(
            "python", "-m", "pymobiledevice3", "developer", "dvt", "simulate-location", "set", "--", str(lat), str(lon),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            print(f"[SUCCESS] Location updated to: Lat {lat}, Lon {lon}")
        else:
            print(f"[ERROR] Failed to update location: {stderr.decode().strip()}")
    except Exception as e:
        print(f"[ERROR] Exception during location update: {e}")

@app.get("/", response_class=HTMLResponse)
async def index():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
    
    # Add native Folium LatLngPopup which handles clicking coordinates cleanly
    m.add_child(folium.LatLngPopup())
    
    # Custom script to intercept the popup link and send it to our backend endpoint
    click_script = """
    <script>
        document.addEventListener("click", function(e) {
            if (e.target && e.target.innerHTML.includes("Lat:")) {
                // Leaflet default popup format contains coordinates text
                let text = e.target.innerHTML;
                // Parse out latitude and longitude strings
                let matches = text.match(/-?\\d+\\.\\d+/g);
                if (matches && matches.length >= 2) {
                    let lat = parseFloat(matches[0]);
                    let lon = parseFloat(matches[1]);
                    fetch('/set-location', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({lat: lat, lon: lon})
                    }).then(res => res.json()).then(data => alert('Teleported iPhone to: ' + lat + ', ' + lon));
                }
            }
        });
    </script>
    """
    map_html = m._repr_html_()
    return HTMLResponse(content=f"<html><body><h2>iOS Local GPS Spoofer</h2><p>Click anywhere on the map, then click the popup link that appears!</p>{map_html}{click_script}</body></html>")

@app.post("/set-location")
async def update_location(coords: Coordinates, background_tasks: BackgroundTasks):
    background_tasks.add_task(apply_gps_simulation, coords.lat, coords.lon)
    return {"status": "processing", "lat": coords.lat, "lon": coords.lon}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
