import pygetwindow as gw

# Print all open window titles
all_windows = gw.getAllTitles()
print("All open window titles:")
for window in all_windows:
    print(window)
