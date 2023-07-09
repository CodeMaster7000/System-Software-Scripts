import psutil

def get_cpu_temperature():
    temperature = psutil.sensors_temperatures().get('coretemp', []) # You may need to modify this if your system uses a different name. 
    if temperature:
        return temperature[0].current
    else:
        return None
# Retrieve CPU temperature
cpu_temperature = get_cpu_temperature()
if cpu_temperature is not None:
    print(f"CPU temperature: {cpu_temperature}°C")
else:
    print("Failed to retrieve CPU temperature.")
