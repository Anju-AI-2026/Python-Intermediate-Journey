
# Sensor Data Stream Simulator
# Generates sensor readings and detects abnormal values


def sensor_stream(readings):

    for reading in readings:
        yield reading


sensor_readings = [24.5, 26.1, 28.0, 42.8, 25.3, 8.2, 27.4, 45.6, 23.9]

minimum_safe = 15.0
maximum_safe = 40.0

processed = 0
normal = 0
alerts = 0

print("=" * 55)
print("            SENSOR DATA STREAM")
print("=" * 55)

for reading_number, temperature in enumerate(
    sensor_stream(sensor_readings),
    start=1
):
    processed += 1

    if temperature < minimum_safe:
        status = "LOW TEMPERATURE ALERT"
        alerts += 1

    elif temperature > maximum_safe:
        status = "HIGH TEMPERATURE ALERT"
        alerts += 1

    else:
        status = "NORMAL"
        normal += 1

    print(
        f"Reading {reading_number:02}: "
        f"{temperature:>5.1f} °C | {status}"
    )

print("-" * 55)
print("Total readings:", processed)
print("Normal readings:", normal)
print("Alerts detected:", alerts)
print("=" * 55)
