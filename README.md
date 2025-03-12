# SavePip

A tool to install and save clean package dependencies for both pip and conda environments.

## Installation

```bash
pip install savepip
```

## Usage

```bash
# Install packages with pip
savepip install pandas numpy

# Install packages with conda
savepip -m conda numpy pandas

# Save current environment
savepip save

# Upgrade packages
savepip -u requests pandas

# Save to custom file
savepip -o custom_requirements.txt requests pandas
```

## Categories Feature

SavePip allows you to categorize and save only the desired high-level packages, avoiding the inclusion of unnecessary package names. This is particularly useful when you want to share only the essential libraries with repository users.

### Example Usage

```bash
# Create a new category
savepip mk-category datascience

# Switch to the new category
savepip use-category datascience

# Add dependencies to the current category
savepip install numpy pandas

# Save dependencies of the current category to requirements.txt
savepip save -c datascience

# List all categories
savepip ls-categories
```

## Features

- Supports both pip and conda package managers
- Cleans up dependency specifications
- Preserves existing dependencies
- Sorts dependencies alphabetically
- Removes build hashes and unnecessary information
- Categorize and save only the required high-level packages

## Contributors

Thanks to all the people who have contributed to this project:

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
    <tr>
        <td align="center"><a href="https://github.com/Aeidle"><img src="https://avatars.githubusercontent.com/u/72752236?v=4" width="50;" style="border-radius: 25px;" alt=""/><br /><sub><b>Aeidle</b></sub></a><br /></td>
        <td align="center"><a href="https://github.com/achrafmataich"><img src="https://avatars.githubusercontent.com/u/100163733?&v=4" width="50;" style="border-radius: 25px;" alt=""/><br /><sub><b>achrafmataich</b></sub></a><br /></td>
    </tr>
</table>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->