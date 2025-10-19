"""
Example 3: Spatial Analysis

This example demonstrates spatial operations using the ArcGIS API:
- Creating geometries (points, lines, polygons)
- Calculating distances
- Buffer operations
- Spatial relationships
"""

from arcgis.geometry import Point, Polyline, Polygon
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

    # Calculate distance using geometry method
    # Note: This gives approximate distance in degrees, multiply for km
    from math import radians, sin, cos, sqrt, atan2

    # Haversine formula for great circle distance
    lat1, lon1 = radians(point1.y), radians(point1.x)
    lat2, lon2 = radians(point2.y), radians(point2.x)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    # Earth radius in km
    dist = 6371 * c

    print(f"  Distance: {dist:.2f} km")
    print(f"  Distance: {dist * 0.621371:.2f} miles")

    return dist

def buffer_analysis(point):
    """Create a buffer around a point"""
    print("\nBuffer analysis...")

    # Note: Buffer operations typically require a projected coordinate system
    # For geographic coordinates (lat/lon), use the geometry service
    print(f"  Point location: ({point.y:.4f}, {point.x:.4f})")
    print(f"  Buffer operations work best with projected coordinates")
    print(f"  For production use, use arcgis.geometry.buffer() with proper spatial reference")

    return None

def calculate_area(polygon):
    """Calculate area of a polygon"""
    print("\nCalculating area...")

    # Calculate area using polygon's get_area method (returns in square meters for geographic coords)
    # For this example, we'll calculate approximate area
    # Note: For accurate geodesic area, use arcgis.geometry.areas with a spatial reference
    coords = polygon.rings[0]

    # Simple approximation - not geodesically accurate but demonstrates the concept
    from math import radians, cos
    lat = sum(p[1] for p in coords) / len(coords)

    # Rough calculation (for demo purposes)
    width_deg = max(p[0] for p in coords) - min(p[0] for p in coords)
    height_deg = max(p[1] for p in coords) - min(p[1] for p in coords)

    # Convert to km (very rough approximation)
    width_km = width_deg * 111.32 * cos(radians(lat))
    height_km = height_deg * 110.57

    area = width_km * height_km

    print(f"  Area: ~{area:.2f} square kilometers (approximate)")
    print(f"  Area: ~{area * 0.386102:.2f} square miles (approximate)")

    return area

def spatial_relationships(point, polygon):
    """Check spatial relationships"""
    print("\nChecking spatial relationships...")

    # Display geometry information
    print(f"  Point coordinates: ({point.y:.4f}, {point.x:.4f})")
    print(f"  Polygon bounds:")
    coords = polygon.rings[0]
    min_x = min(p[0] for p in coords)
    max_x = max(p[0] for p in coords)
    min_y = min(p[1] for p in coords)
    max_y = max(p[1] for p in coords)
    print(f"    X: {min_x} to {max_x}")
    print(f"    Y: {min_y} to {max_y}")

    # Simple bounding box check
    within_bounds = (min_x <= point.x <= max_x) and (min_y <= point.y <= max_y)
    print(f"  Point within polygon bounds: {within_bounds}")

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
