"""
Example 4: Map Visualization

This example demonstrates how to:
- Create interactive maps
- Add locations to maps
- Customize map appearance
- Save maps (requires authentication)
"""

from arcgis.gis import GIS
from arcgis.geocoding import geocode

def create_basic_map(gis):
    """Create a basic map"""
    print("Creating basic map...")

    # Create a map centered on a location
    map1 = gis.map("San Francisco, CA", zoomlevel=12)

    print("  ✓ Map created")
    print("  Note: In Jupyter notebooks, this would display interactively")

    return map1

def add_locations_to_map(gis):
    """Create a map with multiple locations"""
    print("\nCreating map with multiple locations...")

    # Create map centered on USA
    map2 = gis.map("United States", zoomlevel=4)

    # Add locations
    locations = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Phoenix, AZ"
    ]

    print("  Adding locations:")
    for location in locations:
        result = geocode(location, max_locations=1)
        if result:
            print(f"    + {location}")
            # In a Jupyter notebook, you would use:
            # map2.draw(result[0]['location'])

    print("  ✓ Map created with locations")

    return map2

def customize_map(gis):
    """Create a customized map"""
    print("\nCreating customized map...")

    # Create map
    map3 = gis.map("Los Angeles, CA")

    # Customize basemap
    # Available basemaps: streets, satellite, hybrid, topo, gray, dark-gray,
    #                     oceans, national-geographic, terrain, osm
    map3.basemap = 'satellite'
    map3.zoom = 10

    print("  ✓ Map created with satellite basemap")

    return map3

def search_and_map(gis):
    """Search for a location and display on map"""
    print("\nSearching and mapping location...")

    # Geocode a famous location
    location_name = "Golden Gate Bridge, San Francisco"
    result = geocode(location_name, max_locations=1)

    if result:
        location = result[0]['location']
        print(f"  Found: {result[0]['address']}")
        print(f"  Coordinates: ({location['y']:.6f}, {location['x']:.6f})")

        # Create map centered on this location
        map4 = gis.map()
        map4.center = [location['y'], location['x']]
        map4.zoom = 15

        print("  ✓ Map created and centered on location")

        return map4
    else:
        print("  ✗ Location not found")
        return None

if __name__ == "__main__":
    # Create GIS connection
    gis = GIS()

    print("=== Map Visualization Examples ===\n")

    print("1. Basic Map")
    print("-" * 40)
    map1 = create_basic_map(gis)

    print("\n2. Map with Multiple Locations")
    print("-" * 40)
    map2 = add_locations_to_map(gis)

    print("\n3. Customized Map")
    print("-" * 40)
    map3 = customize_map(gis)

    print("\n4. Search and Map")
    print("-" * 40)
    map4 = search_and_map(gis)

    print("\n" + "=" * 60)
    print("Note: These maps are Python objects.")
    print("To view them interactively, run this code in a Jupyter notebook:")
    print("  1. Start Jupyter: jupyter lab")
    print("  2. Create a new notebook")
    print("  3. Run any map creation code")
    print("  4. Display with: map1  (the map object will render)")
    print("=" * 60)

    print("\nExample completed!")
