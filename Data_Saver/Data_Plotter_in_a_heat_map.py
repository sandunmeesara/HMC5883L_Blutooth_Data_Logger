import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('data.csv')

# Extract x, y, and magnitude
x = data['X']
y = data['Y']
magnitude = data['Magnitude']

# Define grid size
grid_size = 50

# Create grid
x_bins = np.linspace(min(x), max(x), grid_size)
y_bins = np.linspace(min(y), max(y), grid_size)

# Digitize x and y into grid bins
x_digitized = np.digitize(x, x_bins)
y_digitized = np.digitize(y, y_bins)

# Create a 2D histogram
heatmap, xedges, yedges = np.histogram2d(x_digitized, y_digitized, bins=[len(x_bins), len(y_bins)], weights=magnitude)

# Normalize heatmap for better visualization
heatmap = heatmap / np.maximum(np.sum(heatmap, axis=1, keepdims=True), 1e-10)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap.T, cmap='viridis', cbar=True, xticklabels=x_bins, yticklabels=y_bins)
plt.title('Magnetic Field Strength Heatmap')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
