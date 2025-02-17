import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import LineString
import matplotlib as mpl

# Set font to Times New Roman
mpl.rcParams['font.family'] = 'Times New Roman'

# Load CSV file
file_path = 'data/04-YuMing_final_with_clusters.csv'
data = pd.read_csv(file_path)
print("Data loaded successfully, containing {0} rows and {1} columns".format(len(data), data.shape[1]))

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))
gdf.crs = "EPSG:4326"  # Maintain the original latitude-longitude coordinate system

# Check for and remove rows with missing values
gdf = gdf.dropna(subset=['Longitude', 'Latitude']).drop_duplicates(subset=['Longitude', 'Latitude'])

# Define color mapping, starting from index 1
color_mapping = {1: 'royalblue', 2: 'orchid', 3: 'green', 4: 'brown', 5: 'orange', 6: 'grey'}
gdf['colors'] = gdf['SeaConditionCluster'].map(color_mapping)

# Figure 1: Ship trajectory with sea condition clustering results
fig, ax = plt.subplots(figsize=(8.5, 4.5))

# Convert coordinates to Web Mercator for background map visualization
gdf_web_mercator = gdf.to_crs(epsg=3857)

# Draw connecting lines, coloring each segment according to the starting point's sea condition
for i in range(len(gdf_web_mercator) - 1):
    segment = LineString([gdf_web_mercator.geometry.iloc[i], gdf_web_mercator.geometry.iloc[i + 1]])
    segment_gdf = gpd.GeoDataFrame(geometry=[segment], crs="EPSG:3857")
    segment_gdf.plot(ax=ax, color=gdf_web_mercator['colors'].iloc[i], linewidth=1.5, alpha=0.7)

# Add a CartoDB.Positron basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, zoom=10)

# Create a custom legend, starting from index 1
for condition, color in color_mapping.items():
    ax.scatter([], [], color=color, label=f'Sea Condition {condition}', s=50)
ax.legend(title="Sea Condition", loc="lower left", fontsize=8, title_fontsize='small')

# Set axis labels and title
ax.set_xlabel('Longitude', fontsize=8, fontname="Times New Roman")
ax.set_ylabel('Latitude', fontsize=8, fontname="Times New Roman")
ax.tick_params(axis='both', which='major', labelsize=8)  # Adjust fontsize as needed

# Figure 2: Ship trajectory without sea condition clustering results
fig, ax2 = plt.subplots(figsize=(8.5, 4.5))

# Draw trajectory without clustering, using a uniform black color
for i in range(len(gdf_web_mercator) - 1):
    segment = LineString([gdf_web_mercator.geometry.iloc[i], gdf_web_mercator.geometry.iloc[i + 1]])
    segment_gdf = gpd.GeoDataFrame(geometry=[segment], crs="EPSG:3857")
    segment_gdf.plot(ax=ax2, color='black', linewidth=1.5, alpha=0.7)

# Add a CartoDB.Positron basemap
ctx.add_basemap(ax2, source=ctx.providers.CartoDB.Positron, zoom=10)

# Set axis labels and title
ax2.set_xlabel('Longitude', fontsize=8, fontname="Times New Roman")
ax2.set_ylabel('Latitude', fontsize=8, fontname="Times New Roman")
ax2.tick_params(axis='both', which='major', labelsize=8)

# Display the plots
plt.show()
