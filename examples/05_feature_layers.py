"""
Example 5: Working with Feature Layers

This example demonstrates how to:
- Search for feature layers
- Query feature layers
- Extract data from layers
- Display layer information
"""

from arcgis.gis import GIS
from arcgis.features import FeatureLayer

def search_feature_layers(gis):
    """Search for public feature layers"""
    print("Searching for feature layers...")

    # Search for earthquake data
    search_results = gis.content.search(
        query="earthquake",
        item_type="Feature Layer",
        max_items=5
    )

    print(f"  Found {len(search_results)} feature layers:")
    for i, item in enumerate(search_results, 1):
        print(f"    {i}. {item.title}")
        print(f"       Owner: {item.owner}")
        print(f"       Item ID: {item.id}")

    return search_results

def query_feature_layer(gis):
    """Query a public feature layer"""
    print("\nQuerying feature layer...")

    # Use a well-known public feature layer (USA States)
    # This is a stable Esri sample layer
    layer_url = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer/0"

    try:
        # Create feature layer object
        layer = FeatureLayer(layer_url)

        print(f"  Layer: {layer.properties.name}")
        print(f"  Type: {layer.properties.geometryType}")
        print(f"  Fields: {len(layer.properties.fields)}")

        # Query first 5 features
        query_result = layer.query(where="1=1", out_fields="*", return_geometry=False, result_record_count=5)

        print(f"\n  Queried {len(query_result.features)} features:")
        for i, feature in enumerate(query_result.features, 1):
            attrs = feature.attributes
            # Get state name (field name may vary)
            state_name = attrs.get('STATE_NAME', attrs.get('NAME', 'Unknown'))
            print(f"    {i}. {state_name}")

        return layer, query_result

    except Exception as e:
        print(f"  Error querying layer: {e}")
        return None, None

def get_layer_statistics(layer):
    """Get statistics from a feature layer"""
    print("\nGetting layer statistics...")

    try:
        # Query total count
        count_result = layer.query(where="1=1", return_count_only=True)

        print(f"  Total features: {count_result}")

        # Get extent
        extent = layer.properties.extent
        print(f"  Extent:")
        print(f"    XMin: {extent.get('xmin', 'N/A')}")
        print(f"    YMin: {extent.get('ymin', 'N/A')}")
        print(f"    XMax: {extent.get('xmax', 'N/A')}")
        print(f"    YMax: {extent.get('ymax', 'N/A')}")

    except Exception as e:
        print(f"  Error getting statistics: {e}")

def query_with_filters(layer):
    """Query feature layer with filters"""
    print("\nQuerying with filters...")

    try:
        # Query specific states (California and Texas)
        query_result = layer.query(
            where="STATE_NAME IN ('California', 'Texas')",
            out_fields="STATE_NAME,POP2010",
            return_geometry=False
        )

        print(f"  Found {len(query_result.features)} matching features:")
        for feature in query_result.features:
            attrs = feature.attributes
            name = attrs.get('STATE_NAME', 'Unknown')
            pop = attrs.get('POP2010', 0)
            print(f"    {name}: Population {pop:,}")

    except Exception as e:
        print(f"  Error with filtered query: {e}")

if __name__ == "__main__":
    # Create GIS connection
    gis = GIS()

    print("=== Feature Layer Examples ===\n")

    # Search for layers
    print("1. Search for Feature Layers")
    print("-" * 40)
    search_results = search_feature_layers(gis)

    # Query a layer
    print("\n2. Query Feature Layer")
    print("-" * 40)
    layer, query_result = query_feature_layer(gis)

    if layer:
        # Get statistics
        print("\n3. Layer Statistics")
        print("-" * 40)
        get_layer_statistics(layer)

        # Query with filters
        print("\n4. Query with Filters")
        print("-" * 40)
        query_with_filters(layer)

    print("\n" + "=" * 60)
    print("Feature layers are powerful for accessing and analyzing")
    print("geographic data. You can:")
    print("  - Query by attributes")
    print("  - Filter by spatial extent")
    print("  - Calculate statistics")
    print("  - Export to various formats")
    print("=" * 60)

    print("\nExample completed!")
