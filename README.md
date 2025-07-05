# WIfiScanner
# Wi-Fi Network Scanner 
A Python tool to discover nearby wireless networks and measure signal strength on Windows systems

# Key Features

1. Detects all available Wi-Fi networks in range

2. Measures signal strength percentage

3. Displays results in clean table format

4. Sorts networks by strongest signal

5. Uses native Windows commands (no special hardware required)

6. Lightweight and fast

# Requirements
OS: Windows 7 or newer

Python: 3.6+

# Dependencies:

        bash
        
        pip install pandas
        
# Installation

Clone repository (if applicable)

        bash
        
        https://github.com/SaravananRKANANDHI/WIfiScanner.git
        
        cd WIfiScanner


# Usage
Must run as Administrator:

        bash
        
        python wifi_scanner.py

# How It Works

1. Parses command output for SSIDs and signal strength

2. Converts signal quality to percentage

3. Formats results using pandas DataFrame

4. Sorts networks by strongest signal
