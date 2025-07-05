import subprocess
import pandas as pd
import re

def scan_wifi():
    # Run Windows command to list Wi-Fi networks
    command = "netsh wlan show networks mode=bssid"
    result = subprocess.run(command, capture_output=True, text=True, encoding='latin-1')
    
    if result.returncode != 0:
        print("Error: Run in Command Prompt as Administrator")
        return
    
    # Parse output
    networks = []
    current_ssid = None
    
    for line in result.stdout.split('\n'):
        line = line.strip()
        
        # Detect SSID
        if line.startswith("SSID"):
            current_ssid = line.split(':')[1].strip()
        
        # Detect signal strength
        elif "Signal" in line and current_ssid:
            signal = line.split(':')[1].replace('%', '').strip()
            if signal.isdigit():
                networks.append({
                    "SSID": current_ssid, 
                    "Signal (%)": int(signal)
                })
    
    # Display results
    if networks:
        df = pd.DataFrame(networks)
        print("\nAvailable Wi-Fi Networks:")
        print(df.drop_duplicates(subset="SSID").sort_values("Signal (%)", ascending=False))
    else:
        print("No networks found")

if _name_ == "_main_":
    scan_wifi()