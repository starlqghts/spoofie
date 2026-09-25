import asyncio
import os
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import folium

app = FastAPI()

class Coordinates(BaseModel):
    lat: float
    lon: float

async def apply_gps_simulation(lat: float, lon: float):
    try:
        # Modern iOS requires starting an RSD tunnel first, then passing the tunnel parameters to simulate-location
        print("[INFO] Establishing secure tunnel to iPhone...")
        tunnel_proc = await asyncio.create_subprocess_exec(
            "python", "-m", "pymobiledevice3", "lockdown", "start-tunnel",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Read the first line of tunnel output to get RSD address and port
        rsd_host, rsd_port = None, None
        while True:
            line = await tunnel_proc.stdout.readline()
            if not line:
                break
            decoded = line.decode().strip()
            print(f"[TUNNEL] {decoded}")
            if "RSD Address:" in decoded or "fd03:" in decoded or ":" in decoded:
                # Basic parse check or fallback to standard tunnel management
                pass
            # Alternatively, pymobiledevice3 handles auto-tunneling via specific flags or we can invoke the integrated command sequence:
        
        # Simpler approach using built-in auto parameters if supported, or running the explicit set command:
        proc = await asyncio.create_subprocess_exec(
            "python", "-m", "pymobiledevice3", "developer", "dvt", "simulate-location", "set", "--", str(lat), str(lon),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        
        # Terminate tunnel process if still active
        try:
            tunnel_proc.terminate()
        except:
            pass

        if proc.returncode == 0:
            print(f"[SUCCESS] Location updated to: Lat {lat}, Lon {lon}")
        else:
            err_msg = stderr.decode().strip()
            print(f"[ERROR] Failed to update location: {err_msg}")
    except Exception as e:
        print(f"[ERROR] Exception during location update: {e}")

@app.get("/", response_class=HTMLResponse)
async def index():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
    m.add_child(folium.LatLngPopup())
    
    click_script = """
    <script>
        document.addEventListener('click', function (event) {
            let popupText = document.querySelector('.leaflet-popup-content');
            if (popupText && event.target.closest('.leaflet-popup')) {
                let text = popupText.innerText;
                let matches = text.match(/-?\\d+\\.\\d+/g);
                if (matches && matches.length >= 2) {
                    let lat = parseFloat(matches[0]);
                    let lon = parseFloat(matches[1]);
                    if(window.lastLat !== lat || window.lastLon !== lon) {
                        window.lastLat = lat;
                        window.lastLon = lon;
                        fetch('/set-location', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({lat: lat, lon: lon})
                        }).then(res => res.json()).then(data => alert('Teleporting iPhone to: ' + lat + ', ' + lon));
                    }
                }
            }
        });
    </script>
    """
    map_html = m._repr_html_()
    return HTMLResponse(content=f"<html><body><h2>iOS Local GPS Spoofer</h2><p>Click anywhere on the map, then click the coordinate box that pops up!</p>{map_html}{click_script}</body></html>")

@app.post("/set-location")
async def update_location(coords: Coordinates, background_tasks: BackgroundTasks):
    background_tasks.add_task(apply_gps_simulation, coords.lat, coords.lon)
    return {"status": "processing", "lat": coords.lat, "lon": coords.lon}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
