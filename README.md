## usb-hub-controller
Manage Acroname USBHub3+ remotely

#### Preconditions
- USBHub3+ is connected to computer via usb cable
- Brainstem package installed
- No other related processes are running (HubTool, StemTool, etc)

#### Usage
```
python toggle_ports.py --help

arguments:
  -h, --help             Show this help message and exit
  -p , --port            Port to enable/disable. All ports selected if not specified.
  -e , --enable          Enable(True)/Disable(False)
  -s , --serial_number   Serial number for specific usb hub (optional) 
```
