#!/usr/bin/env python3
"""
Simple script to create an interactive ArcGIS map
"""
from arcgis.gis import GIS
import webbrowser
import os

print("Creating map...")

# Connect to ArcGIS
gis = GIS()

# Create a map of San Francisco
map1 = gis.map("San Francisco, CA", zoomlevel=12)

# Export to HTML file
html_file = os.path.expanduser("~/arcgis_project/my_interactive_map.html")
map1.export_to_html(html_file, title="My San Francisco Map")

print(f"✓ Map saved to: {html_file}")

# Open in browser
webbrowser.open('file://' + html_file)

print("✓ Map should open in your browser!")
print("\nIf it doesn't open automatically:")
print(f"  Open this file: {html_file}")
