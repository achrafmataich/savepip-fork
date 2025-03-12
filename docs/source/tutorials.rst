Tutorials
=========

This section provides step-by-step tutorials on how to use the `savepip` library through CLI commands.

Setting Up
----------

1. Install the `savepip` library.
   
   .. code-block:: bash

      pip install savepip

Creating and Using Categories
-----------------------------

1. Create a new category.
   
   .. code-block:: bash

      savepip mk-category webdev

2. Switch to the new category.
   
   .. code-block:: bash
   
      savepip use-category webdev

Adding Dependencies and saving them to a `requirements.txt` file
----------------------------------------------------------------

1. Install and add package dependencies to the current category.

   .. code-block:: bash

      savepip install requests pydantics fastapi

2. Saves the list of dependencies for the current category into a `requirements.txt` file.
   
   .. code-block:: bash

      savepip save -c webdev

Listing Categories
------------------

1. List all categories along with a flag indicating whether each category is the current category.
   
   .. code-block:: bash

      savepip ls-categories
