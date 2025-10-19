"""
Example 2: Geocoding with ArcGIS

This example demonstrates how to:
- Geocode addresses to coordinates
- Reverse geocode coordinates to addresses
- Batch geocode multiple addresses
"""

from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode, batch_geocode

def geocode_address(address):
    """Convert an address to coordinates"""
    print(f"Geocoding: {address}")

    # Geocode the address
    results = geocode(address, max_locations=1)

    if results:
        result = results[0]
        location = result['location']
        print(f"  ✓ Found: {result['address']}")
        print(f"    Coordinates: ({location['y']:.6f}, {location['x']:.6f})")
        print(f"    Score: {result['score']}")
        return location
    else:
        print(f"  ✗ No results found")
        return None

def reverse_geocode_location(latitude, longitude):
    """Convert coordinates to an address"""
    print(f"Reverse geocoding: ({latitude}, {longitude})")

    # Reverse geocode the coordinates
    result = reverse_geocode({"x": longitude, "y": latitude})

    if result:
        address = result['address']
        print(f"  ✓ Address: {address['Address']}")
        print(f"    City: {address.get('City', 'N/A')}")
        print(f"    Region: {address.get('Region', 'N/A')}")
        print(f"    Country: {address.get('CountryCode', 'N/A')}")
        return address
    else:
        print(f"  ✗ No address found")
        return None

def batch_geocode_addresses(addresses):
    """Geocode multiple addresses at once"""
    print(f"Batch geocoding {len(addresses)} addresses...")

    # Batch geocode
    results = batch_geocode(addresses)

    print(f"  Results:")
    for i, result in enumerate(results, 1):
        if result['location']:
            loc = result['location']
            print(f"  {i}. {result['address']}")
            print(f"     Location: ({loc['y']:.6f}, {loc['x']:.6f})")
        else:
            print(f"  {i}. Not found: {addresses[i-1]}")

    return results

if __name__ == "__main__":
    # Create anonymous GIS connection
    gis = GIS()

    print("=== Geocoding Examples ===\n")

    # Example 1: Geocode single address
    print("1. Single Address Geocoding")
    print("-" * 40)
    location = geocode_address("1600 Pennsylvania Avenue NW, Washington, DC")
    print()

    # Example 2: Geocode another address
    location2 = geocode_address("380 New York St, Redlands, CA 92373")
    print()

    # Example 3: Reverse geocode
    print("2. Reverse Geocoding")
    print("-" * 40)
    if location:
        reverse_geocode_location(location['y'], location['x'])
    print()

    # Example 4: Batch geocoding
    print("3. Batch Geocoding")
    print("-" * 40)
    addresses = [
        "Times Square, New York, NY",
        "Golden Gate Bridge, San Francisco, CA",
        "Space Needle, Seattle, WA"
    ]
    batch_geocode_addresses(addresses)
    print()

    print("Example completed!")
