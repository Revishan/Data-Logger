import serial
import csv
from datetime import datetime
PORT = "COM3"   # change this to your Arduino port
BAUD = 9600
ser = serial.Serial(PORT, BAUD, timeout=1)
#Path in C:\Users\YourUsername\Documents\wind_data_20240601_120000.csv
filename = f"wind_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    print(f"Logging to {filename}")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if line:
                values = line.split(",")
                if len(values) == 5:
                    writer.writerow(values)
                    file.flush()
                    print(values)
    except KeyboardInterrupt:
        print("Stopped logging.")
        ser.close()

