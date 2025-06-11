# Geometry-Dash-Click-Sound
 Geometry Dash Click Sound created by me:)

# Geometry-Dash-Click-Sound
 Geometry Dash Click Sound created by me:)
 
This script is made for Arch Linux distributions!
Custom click sounds script version 1.0
The script is open source :)
(This is my first project for public release — if you find any bugs, please contact me!)

To install this script, you need to install a few libraries:

First, install Python itself:
```
sudo pacman -S python
```
After installation, create a virtual environment to install a few libraries
(IMPORTANT: Run the script inside the virtual environment for it to work properly — the system will complain if you run it without it!)

Create the environment:
```
python3 -m venv ~/clickmod-env
```
Activate it:
```
source ~/clickmod-env/bin/activate
```
Next, inside this virtual environment, install the required libraries:
```
pip install pygame pynput psutil
```
Then, open a new terminal and install the utilities:
```
sudo pacman -S xdotool wmctrl
```
After installing the libraries, download the script geoclick.py, save it wherever you like, and open it.

Find at the very top:
```
# === The Path to Sound ===
SOUND_PATH = "/home/your-name/the-place-where-you-saved-the-sound/mouse-click.mp3"
```
Important: The click sound must be no longer than 1 second!

Then, in the terminal where your virtual environment is activated, navigate to the folder where you saved the script and run:
```
python3 /path/to/geoclick.py
```
Done!
---
If you liked it, please share this repository with your friends :)
