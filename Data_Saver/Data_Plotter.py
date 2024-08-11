import pandas as pd

# Load the CSV file
data = pd.read_csv('data.csv')

# Display the first few rows of the data
print(data.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Convert timestamp to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Plot Magnitude over Time
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Magnitude'], marker='o')
plt.title('Magnitude Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Magnitude (uT)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Heading over Time
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Heading'], marker='o', color='r')
plt.title('Heading Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Heading (Degrees)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot data on a scatter plot with magnitude as color
plt.figure(figsize=(10, 6))
plt.scatter(data['Longitude'], data['Latitude'], c=data['Magnitude'], cmap='viridis', s=100)
plt.colorbar(label='Magnitude (uT)')
plt.title('Magnitude by Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['Longitude'], data['Latitude'], c=data['Magnitude'], cmap='viridis', s=100)
plt.colorbar(label='Magnitude (uT)')
for i in range(len(data)):
    plt.arrow(data['Longitude'][i], data['Latitude'][i],
              0.01 * pd.np.cos(pd.np.radians(data['Heading'][i])),
              0.01 * pd.np.sin(pd.np.radians(data['Heading'][i])),
              head_width=0.01, head_length=0.02, fc='k', ec='k')
plt.title('Magnitude and Heading by Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
