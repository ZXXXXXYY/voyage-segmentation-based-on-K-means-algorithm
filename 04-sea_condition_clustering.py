import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.lines import Line2D

# Set global font to Times New Roman
rcParams['font.family'] = 'Times New Roman'

# Load CSV file, normalize data, and perform clustering
csv_file_path = 'data/03-YuMing_final.csv'
df = pd.read_csv(csv_file_path)

# Select feature columns and normalize the data
features = df[['WindSpeed', 'WindDirection', 'WaterSpeed']]
scaler = MinMaxScaler()
features_normalized = scaler.fit_transform(features)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=6, random_state=42)
df['SeaConditionCluster'] = kmeans.fit_predict(features_normalized) + 1  # Shift cluster labels to start from 1

# Save clustering results
output_file_path = 'data/04-YuMing_final_with_clusters.csv'
df.to_csv(output_file_path, index=False)

# Retrieve cluster centers and inverse transform normalization
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

# Define color mapping for clusters
unique_clusters = sorted(df['SeaConditionCluster'].unique())
colors = ['royalblue', 'orchid', 'green', 'brown', 'orange', 'grey']
color_mapping = {cluster: colors[i] for i, cluster in enumerate(unique_clusters)}

# Plot 3D scatter plot of data points
fig1 = plt.figure(figsize=(3.2, 3.2))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.scatter(df['WindDirection'], df['WindSpeed'], df['WaterSpeed'],
            color=[color_mapping[cluster] for cluster in df['SeaConditionCluster']],
            s=9, alpha=0.8, edgecolor='k', linewidth=0.3)

# Set axis labels
ax1.set_xlabel('Wind Direction (°)', fontsize=8, labelpad=2)
ax1.set_ylabel('Wind Speed (m/s)', fontsize=8, labelpad=2)
ax1.set_zlabel('Water Speed (m/s)', fontsize=8, labelpad=2)

# Create legend for clusters
legend_handles = [
    Line2D([0], [0], marker='o', color='w', label=f'Sea Condition {cluster}',
           markerfacecolor=color_mapping[cluster], markersize=5, markeredgewidth=0.5, markeredgecolor='k')
    for cluster in unique_clusters
]
ax1.legend(handles=legend_handles, loc='upper right', fontsize=6)

# Plot 3D scatter plot of cluster centers
fig2 = plt.figure(figsize=(3.2, 3.2))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.scatter(cluster_centers[:, 1], cluster_centers[:, 0], cluster_centers[:, 2],
            color=[color_mapping[cluster] for cluster in unique_clusters], s=40, marker='X', edgecolor='k', linewidth=1)

# Set axis labels
ax2.set_xlabel('Wind Direction (°)', fontsize=8, labelpad=2)
ax2.set_ylabel('Wind Speed (m/s)', fontsize=8, labelpad=2)
ax2.set_zlabel('Water Speed (m/s)', fontsize=8, labelpad=2)

# Create legend for cluster centers
legend_handles_centers = [
    Line2D([0], [0], marker='X', color='w', label=f'Cluster Center {cluster}',
           markerfacecolor=color_mapping[cluster], markersize=5, markeredgewidth=0.5, markeredgecolor='k')
    for cluster in unique_clusters
]
ax2.legend(handles=legend_handles_centers, loc='upper right', fontsize=7)

# Set axis range based on data
x_range = [df['WindDirection'].min(), df['WindDirection'].max()]
y_range = [df['WindSpeed'].min(), df['WindSpeed'].max()]
z_range = [df['WaterSpeed'].min(), df['WaterSpeed'].max()]

ax1.set_xlim(x_range)
ax1.set_ylim(y_range)
ax1.set_zlim(z_range)
ax2.set_xlim(x_range)
ax2.set_ylim(y_range)
ax2.set_zlim(z_range)

# Set view angle
ax1.view_init(elev=25, azim=140)
ax2.view_init(elev=25, azim=140)

# Adjust tick label font size
ax1.tick_params(axis='both', which='major', labelsize=8)
ax1.tick_params(axis='both', which='minor', labelsize=8)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.tick_params(axis='both', which='minor', labelsize=8)

# Reduce padding between axis labels and tick labels
ax1.tick_params(axis='x', pad=0.5)
ax1.tick_params(axis='y', pad=0.5)
ax1.tick_params(axis='z', pad=0.5)
ax2.tick_params(axis='x', pad=0.5)
ax2.tick_params(axis='y', pad=0.5)
ax2.tick_params(axis='z', pad=0.5)

# Display the plots
plt.show()
