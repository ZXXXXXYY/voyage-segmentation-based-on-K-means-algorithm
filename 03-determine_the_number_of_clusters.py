import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load CSV file
csv_file_path = 'data/03-YuMing_final.csv'
df = pd.read_csv(csv_file_path)

# Select feature columns and normalize the data
features = df[['WindSpeed', 'WindDirection', 'WaterSpeed']]
scaler = MinMaxScaler()
features_normalized = scaler.fit_transform(features)

# Determine the optimal number of clusters (K) using the Elbow method
sse = []
k_range = range(1, 16)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_normalized)
    sse.append(kmeans.inertia_)

# Print SSE values for each K
print("SSE values for different K values:")
for k, value in zip(k_range, sse):
    print(f"K={k}, SSE={value:.2f}")

# Plot the Elbow method graph
plt.figure(figsize=(4.5, 3))
plt.plot(k_range, sse, marker='o', color=(46/255, 117/255, 181/255), linestyle='-', markersize=5, linewidth=1.5)
plt.xlabel('Number of clusters (K)', fontname="Times New Roman", fontsize=8)
plt.ylabel('SSE (Sum of Squared Errors)', fontname="Times New Roman", fontsize=8)

# Set font type and size for axis ticks
plt.xticks(fontsize=8, fontname="Times New Roman")
plt.yticks(fontsize=8, fontname="Times New Roman")

# Add grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Display the plot
plt.show()
