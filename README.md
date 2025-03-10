# PipIt

A tool to install and save clean package dependencies for both pip and conda environments.

## Installation

```bash
pip install pipit
```

## Usage
```bash
# Install packages with pip
pipit install pandas numpy

# Install packages with conda
pipit -m conda numpy pandas

# Save current environment
pipit save

# Upgrade packages
pipit -u requests pandas

# Save to custom file
pipit -o custom_requirements.txt requests pandas
 ```

## Features
- Supports both pip and conda package managers
- Cleans up dependency specifications
- Preserves existing dependencies
- Sorts dependencies alphabetically
- Removes build hashes and unnecessary information
