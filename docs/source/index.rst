.. savepip documentation master file, created by
   sphinx-quickstart on Wed Mar 12 16:01:29 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

savepip documentation
=====================

This is the main documentation file for the CLI library. This library addresses the common issue with `pip freeze` where all installed packages, including those not necessary for the project, are listed in the `requirements.txt` file. This can be problematic when you want to share only the essential libraries with repository users.

With this library, you can categorize and save only the desired high-level packages. For example, if you are working on a project using `pandas` and `torch` but use `jupyter` locally for testing functionalities, `pip freeze` would output all packages and subpackages. Using this library, you can save only the high-level packages like `torch` and `pandas`, avoiding the inclusion of unnecessary package names.

Key Features:
   - Categorize and save only the required high-level packages 
   - Simple and intuitive command syntax 
   - Support for custom commands and scripts 
   - Extensive documentation and examples 
   - Integration with other tools and libraries 
   - Error handling and logging capabilities 


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   functionalities
   tutorials
