#!/usr/bin/env python3

import folium
import json
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

from shapely import Polygon

### PART 1 ###
capitals = pd.read_csv('capitals_lat_lon.csv')

map = folium.Map(location=[15, -10], zoom_start=3)
for row in capitals.itertuples():
    map.add_child(folium.Marker(
        location=[row.Latitude, row.Longitude],
        popup=row.Capital))
map.save('capitals.html')
print("Part 1 map saved to 'capitals.html'")

### PART 2 ###
p1 = [-34.2, 22]
p2 = [35.7, -5.8]
p3 = [11, 51]

africa = folium.Map()
triangle = folium.Polygon(locations=[p1, p2, p3]).add_to(africa)
africa.fit_bounds(triangle.get_bounds())
africa.save('africa.html')
print("Part 2 map saved to 'africa.html'")

poly = Polygon([p1, p2, p3])
print(f"Area of triangle around Africa: {poly.area:.1f}")
print(f"Perimeter of triangle around Africa: {poly.length:.1f}")

### PART 3 ###
# List of LON-LATs for Kansas and Nebraska (manually estimated)
kansas_coords = [(-102.09, 36.97), (-94.58, 36.97), (-94.58, 39.99), (-102.09, 39.99)]
nebraska_coords = [(-104.04, 40.98), (-102.09, 40.98), (-102.09, 39.99), (-95.37, 39.99), (-96.76, 42.94), (-104.04, 42.94)]

# Building a GeoJSON dictionary
kansas_json = {'type': 'Feature',
               'properties': {'name': 'Kansas'},
               'geometry': {'type':'Polygon', 'coordinates': [kansas_coords]}}
nebraska_json = {'type': 'Feature',
                 'properties': {'name': 'Nebraska'},
                 'geometry': {'type':'Polygon', 'coordinates': [nebraska_coords]}}
geojson = {'type': 'FeatureCollection', 'features': [kansas_json, nebraska_json]}

# Write the GeoJSON to a file
with open("part3.json", "w") as outfile:
    json.dump(geojson, outfile, indent=4)

# Read the file back into a new dictionary
with open("part3.json", "r") as infile:
    geo_dict = json.load(infile)

gdf = gpd.GeoDataFrame.from_features(geo_dict)
fig, ax = plt.subplots()
gdf.plot(color='white', edgecolor='black', ax=ax)
gdf.apply(lambda x: ax.annotate(text=x['name'], xy=x.geometry.centroid.coords[0], ha='center'), axis=1);
ax.set_title('Simplified Kansas and Nebraska')
plt.show()

### PART 4 ###
states = gpd.read_file('states_geo.json')
states['happiness'] = np.random.randint(25, 100, size=len(states))

map = folium.Map(location=[48, -102], zoom_start=4)
folium.Choropleth(
    geo_data=states,
    data=states,
    key_on='feature.properties.name',
    columns=['name','happiness'],
    fill_color="BuGn",
    fill_opacity = 0.7,
    legend_name="Happiness By State",
).add_to(map)

folium.LayerControl().add_to(map)
map.save('states_choropleth.html')
print("Part 4 map saved to 'states_choropleth.html'")

### PART 5 ###
np.random.seed(4433)
data = np.random.exponential(scale=0.75, size=500)
fig = px.histogram(data)
fig.show()
