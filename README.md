# PipSave

A tool to install and save clean package dependencies for both pip and conda environments.

## Installation

```bash
pip install pipsave
```

## Usage
```bash
# Install packages with pip
pipsave install pandas numpy

# Install packages with conda
pipsave -m conda numpy pandas

# Save current environment
pipsave save

# Upgrade packages
pipsave -u requests pandas

# Save to custom file
pipsave -o custom_requirements.txt requests pandas
 ```

## Features
- Supports both pip and conda package managers
- Cleans up dependency specifications
- Preserves existing dependencies
- Sorts dependencies alphabetically
- Removes build hashes and unnecessary information
