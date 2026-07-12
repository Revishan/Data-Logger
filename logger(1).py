import csv
from datetime import datetime
import random
import sys
import time


filename = f"wind_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ADC", "MeasuredVoltage_V", "RealVoltage_V", "Current_mA", "Power_mW"])
    print(f"Logging to {filename}")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            adc = random.randint(0, 200)
            measured = round(adc * 0.00488, 3)
            real = round(measured * 2, 3)
            current = round(real * 10, 3)
            power = round(real * current, 3)
            row = [adc, measured, real, current, power]
            writer.writerow(row)
            file.flush()
            print(row)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Stopped logging.")
        #ser.close()
        import subprocess
        subprocess.run([sys.executable, "wind_plot(1).py", filename])
        
        
