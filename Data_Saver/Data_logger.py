import serial
import csv
import datetime

# Set up the serial connection (Replace 'COM3' with your Bluetooth COM port)
ser = serial.Serial('COM12', 9600)

# Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Timestamp', 'X', 'Y', 'Z', 'Magnitude', 'Heading'])  # Header row

    try:
        while True:
            data = ser.readline().decode('utf-8').strip()  # Read a line from the Bluetooth module
            print(f"Raw data: {data}")  # Print the received data

            # Try splitting the data and writing to CSV
            try:
                x, y, z, magnitude, heading = map(float, data.split(','))
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
                csvwriter.writerow([timestamp, x, y, z, magnitude, heading])
                csvfile.flush()  # Ensure data is written to the file immediately
            except ValueError:
                print(f"Error processing data: {data}")
                continue  # Skip to the next line on error

    except KeyboardInterrupt:
        print("Data logging stopped.")
