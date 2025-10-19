"""
Example 1: Basic Connection to ArcGIS Online

This example demonstrates how to connect to ArcGIS Online both
anonymously and with authentication.
"""

from arcgis.gis import GIS

def anonymous_connection():
    """Connect to ArcGIS Online without authentication"""
    print("Connecting to ArcGIS Online (anonymous)...")

    # Create an anonymous connection
    gis = GIS()

    print(f"✓ Connected successfully!")
    print(f"  Version: {gis.version}")
    print(f"  URL: {gis.url}")
    print(f"  User: {gis.users.me if gis.users.me else 'Anonymous'}")

    return gis

def authenticated_connection(username=None, password=None):
    """Connect to ArcGIS Online with authentication"""
    if not username or not password:
        print("Skipping authenticated connection (no credentials provided)")
        return None

    print(f"Connecting to ArcGIS Online as {username}...")

    try:
        gis = GIS("https://www.arcgis.com", username, password)
        print(f"✓ Authenticated successfully!")
        print(f"  User: {gis.users.me.username}")
        print(f"  Full Name: {gis.users.me.fullName}")
        print(f"  Role: {gis.users.me.role}")
        return gis
    except Exception as e:
        print(f"✗ Authentication failed: {e}")
        return None

def search_public_content(gis):
    """Search for public content on ArcGIS Online"""
    print("\nSearching for public COVID-19 maps...")

    # Search for public content
    items = gis.content.search(
        query="COVID-19",
        item_type="Web Map",
        max_items=5
    )

    print(f"Found {len(items)} items:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item.title}")
        print(f"     Owner: {item.owner}")
        print(f"     Views: {item.numViews}")
        print(f"     URL: {item.homepage}")
        print()

if __name__ == "__main__":
    # Connect anonymously
    gis = anonymous_connection()

    # Search public content
    search_public_content(gis)

    # To use authenticated connection, uncomment and add your credentials:
    # gis_auth = authenticated_connection("your_username", "your_password")

    print("\nExample completed!")
