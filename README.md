# Tile Reconcilation
A graphical user interface allowing on-site support and FSC operators the ability to perform a complete tile reconcilation within one applicaiton.
Funcitonality includes loading databases options, scan item options, and envelope validation funcitonality. Application has been tested to work with MacOS and Windows.


## Installation
Install the module with pip:
```
pip3 install customtkinter
```
```
pip3 install tk
```
```
pip3 install pandas
```
# Homescreen Interface

## Database Options
Load Small Database:   
    - Pulls 5,000 entries from barcode_scan_events as well as mc_scan_events.   
Load Large Database:   
    - Pulls 50,000 entries from barcode_scan_events as well as mc_scan_events.

## Scan an Item
Scan Tile:   
    - Scan tile device to find systematically correct envelope and master carton location.   
Scan Envelope:   
    - Scan envelope to find systematically correct master carton location.   
Scan Master Carton:   
    - Scan master carton to begin envelope validation process.
<img src="app_imgs/homescreen.png" width="1100"/>
