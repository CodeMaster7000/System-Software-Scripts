import psutil

def get_cpu_speed():
    cpu_info = psutil.cpu_freq()
    if cpu_info:
        return cpu_info.current
    else:
        return None
# Retrieve CPU speed
cpu_speed = get_cpu_speed()
if cpu_speed is not None:
    print(f"CPU speed: {cpu_speed} MHz")
else:
    print("Failed to retrieve CPU speed.")
