# ArcGIS Project Setup Guide

This document explains EVERYTHING we did to set up this ArcGIS Python project from scratch.

## Table of Contents
1. [Installation](#installation)
2. [Dependency Issues and Fixes](#dependency-issues-and-fixes)
3. [PATH Configuration](#path-configuration)
4. [Running Jupyter Lab](#running-jupyter-lab)
5. [Troubleshooting](#troubleshooting)

---

## Installation

### Step 1: Install ArcGIS Package

```bash
pip3 install --user arcgis
```

**What happened:**
- Installed arcgis version 2.3.1
- Automatically installed dependencies: numpy, pandas, matplotlib, jupyterlab, etc.
- Installation location: `~/Library/Python/3.9/lib/python/site-packages/`

**Initial Problems:**
- Version conflicts between packages (see next section)
- Command-line tools not on PATH

---

## Dependency Issues and Fixes

### The Problem
ArcGIS package requires **very specific** older versions of some packages, which conflict with newer Jupyter packages.

**Key Conflict:**
- `arcgis 2.3.1` requires `jupyter-client<=6.1.12` (old)
- `jupyterlab 4.4.9` requires `ipykernel>=6.5.0` (new)
- `jupyter_server 2.17.0` requires `jupyter-client>=7.4.4` (new)

This caused the Jupyter kernel to fail with error:
```
type object 'MultiKernelManager' has no attribute '_async_start_kernel'
```

### The Solution
We downgraded Jupyter packages to versions compatible with ArcGIS:

```bash
# Downgrade to compatible versions
pip3 install --user 'jupyter_server<2.0'
pip3 install --user 'jupyterlab<4.0'
pip3 install --user 'notebook<7.0'
pip3 install --user 'ipykernel<6.0'
```

**Final Working Versions:**
- `arcgis==2.3.1`
- `jupyter-client==6.1.12`
- `ipykernel==5.5.6`
- `jupyter_server==1.24.0`
- `jupyterlab==3.6.8`
- `notebook==6.5.7`

---

## PATH Configuration

### The Problem
Python user packages install to `~/Library/Python/3.9/bin/` which is not on the system PATH by default. This means commands like `jupyter` won't work.

### The Fix
Created `~/.zshrc` file with:

```bash
# Python user bin PATH
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

**To apply:**
```bash
source ~/.zshrc
# OR restart your terminal
```

**Verify it works:**
```bash
which jupyter
# Should output: /Users/jefffranzen/Library/Python/3.9/bin/jupyter
```

---

## Running Jupyter Lab

### Starting Jupyter Lab

**Option 1: If PATH is configured**
```bash
cd ~/arcgis_project
jupyter lab
```

**Option 2: Using full path (always works)**
```bash
cd ~/arcgis_project
~/Library/Python/3.9/bin/jupyter lab
```

### What Happens
1. Jupyter Lab starts on `http://localhost:8888`
2. A token URL is displayed (copy this to your browser)
3. Browser should open automatically

### Example Output
```
Jupyter Server 1.24.0 is running at:
http://localhost:8888/lab?token=876fcb65eb3798e3a917739b55b9a3ad76d758237fbc87cb
```

### Stopping Jupyter Lab
- Press `Ctrl+C` in the terminal twice
- Or from another terminal: find the process and kill it

---

## Running the Examples

All examples work as standalone Python scripts:

```bash
cd ~/arcgis_project

# Test connection to ArcGIS Online
python3 examples/01_basic_connection.py

# Geocode addresses
python3 examples/02_geocoding.py

# Spatial analysis
python3 examples/03_spatial_analysis.py

# Map visualization (better in Jupyter!)
python3 examples/04_map_visualization.py

# Feature layers
python3 examples/05_feature_layers.py
```

**Note:** Maps display interactively only in Jupyter notebooks, not in terminal scripts.

---

## Troubleshooting

### Problem: "Command not found: jupyter"
**Solution:** PATH not configured or not reloaded
```bash
# Use full path
~/Library/Python/3.9/bin/jupyter lab

# OR configure PATH
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Problem: Kernel won't start in Jupyter
**Solution:** Version conflicts - reinstall compatible versions
```bash
pip3 install --user 'jupyter_server<2.0' 'jupyterlab<4.0' 'notebook<7.0' 'ipykernel<6.0'
```

### Problem: "ModuleNotFoundError: No module named 'arcgis'"
**Solution:** ArcGIS not installed in current Python
```bash
pip3 install --user arcgis
```

### Problem: Batch geocoding fails with "Token required"
**Solution:** Batch operations need authentication. Single geocoding works anonymously.

### Warning: urllib3 OpenSSL warning
**This is safe to ignore.** It's a warning about SSL library versions but doesn't affect functionality.

### Warning: dask dataframe warnings
**This is safe to ignore.** ArcGIS works fine without dask-expr.

---

## Quick Reference

### Current Working Directory
```bash
/Users/jefffranzen/arcgis_project
```

### Package Versions That Work Together
```
arcgis==2.3.1
jupyter-client==6.1.12
ipykernel==5.5.6
jupyter_server==1.24.0
jupyterlab==3.6.8
notebook==6.5.7
```

### Important Paths
- Python packages: `~/Library/Python/3.9/lib/python/site-packages/`
- Command-line tools: `~/Library/Python/3.9/bin/`
- Project directory: `~/arcgis_project/`

### Useful Commands
```bash
# Check installed packages
pip3 list | grep arcgis
pip3 list | grep jupyter

# Test ArcGIS import
python3 -c "import arcgis; print(arcgis.__version__)"

# Start Jupyter Lab
cd ~/arcgis_project && ~/Library/Python/3.9/bin/jupyter lab

# Run an example
python3 ~/arcgis_project/examples/01_basic_connection.py
```

---

## Next Steps

1. **Create an ArcGIS Developer Account** (free)
   - Go to: https://developers.arcgis.com/
   - Sign up for free account
   - Get API key for advanced features

2. **Configure Authentication** (optional)
   - Copy `config_template.py` to `config.py`
   - Add your credentials
   - Don't commit `config.py` to version control!

3. **Learn More**
   - Official docs: https://developers.arcgis.com/python/
   - Sample notebooks: https://developers.arcgis.com/python/sample-notebooks/
   - API reference: https://developers.arcgis.com/python/api-reference/

---

## Summary of What We Built

This project includes:
- ✓ Working ArcGIS Python API installation
- ✓ 5 example scripts covering core functionality
- ✓ Jupyter Lab configured and working
- ✓ All dependency conflicts resolved
- ✓ PATH configured for easy access to tools
- ✓ Complete documentation (this file!)

**Everything is working and ready to use!**
