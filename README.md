# ArcGIS Python Project

This starter project contains examples for working with the ArcGIS Python API.

## ⚠️ IMPORTANT: Known Issues

**👉 [READ FAILURES.md FIRST](FAILURES.md)** - Interactive maps in Jupyter Lab DO NOT WORK with this setup.

**👉 [Read SETUP.md for what works](SETUP.md)** - Everything else works perfectly from command line.

### What Works
- ✓ All 5 example Python scripts
- ✓ Geocoding
- ✓ Spatial analysis
- ✓ Feature layer queries
- ✓ Data processing

### What Doesn't Work
- ✗ Interactive map display in Jupyter notebooks
- ✗ Widget-based visualizations

**Use the Python scripts directly. Jupyter map visualization failed despite multiple fix attempts.**

## Quick Start

### Running Examples
```bash
cd ~/arcgis_project
python3 examples/01_basic_connection.py
```

### Starting Jupyter Lab
```bash
cd ~/arcgis_project
~/Library/Python/3.9/bin/jupyter lab
```

## Verify Installation

```bash
python3 -c "import arcgis; print(arcgis.__version__)"
```

## Project Structure

```
arcgis_project/
├── README.md (this file)
├── examples/
│   ├── 01_basic_connection.py - Connect to ArcGIS Online
│   ├── 02_geocoding.py - Geocode addresses
│   ├── 03_spatial_analysis.py - Perform spatial operations
│   ├── 04_map_visualization.py - Create and display maps
│   └── 05_feature_layers.py - Work with feature layers
├── config_template.py - Configuration template
└── requirements.txt - Package dependencies
```

## Getting Started

1. Copy `config_template.py` to `config.py` and add your credentials if needed
2. Run any example script: `python3 examples/01_basic_connection.py`
3. For Jupyter notebooks: `jupyter lab` (then open any .ipynb file)

## Examples Overview

- **01_basic_connection.py**: Connect to ArcGIS Online (anonymous and authenticated)
- **02_geocoding.py**: Convert addresses to coordinates and reverse geocode
- **03_spatial_analysis.py**: Perform spatial operations and analysis
- **04_map_visualization.py**: Create interactive maps
- **05_feature_layers.py**: Query and manipulate feature layers

## Authentication

Many ArcGIS operations work without authentication. For advanced features, you'll need:
- ArcGIS Online account (free at https://developers.arcgis.com/)
- Organization URL and credentials

## Resources

- [ArcGIS Python API Documentation](https://developers.arcgis.com/python/)
- [Sample Notebooks](https://developers.arcgis.com/python/sample-notebooks/)
- [API Reference](https://developers.arcgis.com/python/api-reference/)
