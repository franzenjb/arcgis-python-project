"""
Example 3: Spatial Analysis

This example demonstrates spatial operations using the ArcGIS API:
- Creating geometries (points, lines, polygons)
- Calculating distances
- Buffer operations
- Spatial relationships
"""

from arcgis.geometry import Point, Polyline, Polygon
from arcgis.geometry import lengths, areas, distance
from arcgis.gis import GIS

def create_geometries():
    """Create various geometry objects"""
    print("Creating geometries...")

    # Create points
    point1 = Point({"x": -118.15, "y": 33.80, "spatialReference": {"wkid": 4326}})
    point2 = Point({"x": -122.45, "y": 37.78, "spatialReference": {"wkid": 4326}})

    print(f"  Point 1: Longitude {point1.x}, Latitude {point1.y}")
    print(f"  Point 2: Longitude {point2.x}, Latitude {point2.y}")

    # Create a polyline (line)
    polyline = Polyline({
        "paths": [[
            [-118.15, 33.80],
            [-120.00, 35.00],
            [-122.45, 37.78]
        ]],
        "spatialReference": {"wkid": 4326}
    })
    print(f"  Polyline created with {len(polyline.paths[0])} points")

    # Create a polygon
    polygon = Polygon({
        "rings": [[
            [-118.0, 34.0],
            [-118.0, 34.5],
            [-117.5, 34.5],
            [-117.5, 34.0],
            [-118.0, 34.0]  # Close the ring
        ]],
        "spatialReference": {"wkid": 4326}
    })
    print(f"  Polygon created")

    return point1, point2, polyline, polygon

def calculate_distance(point1, point2):
    """Calculate distance between two points"""
    print("\nCalculating distance...")

    # Calculate geodesic distance
    dist = distance(point1, point2, distance_unit="KILOMETERS")

    print(f"  Distance: {dist:.2f} km")
    print(f"  Distance: {dist * 0.621371:.2f} miles")

    return dist

def buffer_analysis(point):
    """Create a buffer around a point"""
    print("\nBuffer analysis...")

    # Create a buffer (50 km radius)
    buffer_geom = point.buffer(50)  # 50 km buffer

    print(f"  Created buffer around point")
    print(f"  Buffer type: {buffer_geom.type}")

    return buffer_geom

def calculate_area(polygon):
    """Calculate area of a polygon"""
    print("\nCalculating area...")

    # Calculate area
    area = areas([polygon], area_unit="SQUARE_KILOMETERS")[0]

    print(f"  Area: {area:.2f} square kilometers")
    print(f"  Area: {area * 0.386102:.2f} square miles")

    return area

def spatial_relationships(point, polygon):
    """Check spatial relationships"""
    print("\nChecking spatial relationships...")

    # Check if point is within polygon
    within = point.within(polygon)
    print(f"  Point within polygon: {within}")

    # Check if geometries intersect
    intersects = point.intersects(polygon)
    print(f"  Point intersects polygon: {intersects}")

if __name__ == "__main__":
    # Create GIS connection
    gis = GIS()

    print("=== Spatial Analysis Examples ===\n")

    # Create geometries
    print("1. Creating Geometries")
    print("-" * 40)
    point1, point2, polyline, polygon = create_geometries()

    # Calculate distance
    print("\n2. Distance Calculation")
    print("-" * 40)
    calculate_distance(point1, point2)

    # Buffer analysis
    print("\n3. Buffer Analysis")
    print("-" * 40)
    buffer_geom = buffer_analysis(point1)

    # Calculate area
    print("\n4. Area Calculation")
    print("-" * 40)
    calculate_area(polygon)

    # Spatial relationships
    print("\n5. Spatial Relationships")
    print("-" * 40)
    spatial_relationships(point1, polygon)

    print("\nExample completed!")
