import subprocess
import time
import pygetwindow as gw

# function to terminate processes by their names
def kill_processes(process_names):
    for process_name in process_names:
        try:
            subprocess.run(f'taskkill /IM {process_name} /F', shell=True, check=True)
            print(f"Terminated {process_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to terminate {process_name}: {e}")

# function to connect to a specific WiFi network
def connect_to_wifi(ssid):
    try:
        subprocess.run(f'netsh wlan connect name="{ssid}"', shell=True, check=True)
        print(f"Connected to WiFi: {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to WiFi: {ssid}, Error: {e}")

# paths to the executables of the programs you want to launch
apps_to_open = [
    r"C:\C Drive - Downloads and Installations\Capture2Text\Capture2Text\Capture2Text.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\C Drive - Downloads and Installations\ClipAngel - Copy Clipboard\ClipAngel.exe",
    r"C:\Users\Siris\AppData\Local\electron\Rize.exe",
    r"C:\Users\Siris\AppData\Local\Programs\Notion\Notion.exe"
]

# function to launch each application
def launch_applications(apps):
    for app in apps:
        try:
            subprocess.Popen(app)
            print(f"Started {app}")
        except Exception as e:
            print(f"Error starting {app}: {e}")

# function to close windows by partial title match
def close_window_by_partial_title(partial_title):
    try:
        windows = gw.getWindowsWithTitle(partial_title)
        if windows:
            for window in windows:
                window.close()
                print(f"Closed window with partial title: {partial_title}")
        else:
            print(f"No window found with partial title: {partial_title}")
    except Exception as e:
        print(f"Error closing window with partial title {partial_title}: {e}")

# First, terminate Bitdefender VPN App, Service, and ShareX
processes_to_kill = ["BitdefenderVpnApp.exe", "BitdefenderVpnService.exe", "ShareX.exe"]
kill_processes(processes_to_kill)

# Then, connect to the specific WiFi network
connect_to_wifi("Totalplay-829F")

# Launch the apps
launch_applications(apps_to_open)

# Give the apps time to fully load
time.sleep(5)

# Close ClipAngel window after initial delay
close_window_by_partial_title("ClipAngel")


# Wait 10 seconds before attempting to close the Notion window
time.sleep(20)
close_window_by_partial_title("A Fresh Start - The Happy Dash Lobby")  # Close Notion window

# Wait 12 seconds before attempting to close the Rize window
time.sleep(28)
close_window_by_partial_title("Dashboard")  # Close Rize window