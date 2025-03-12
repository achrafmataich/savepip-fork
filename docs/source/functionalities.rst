Functionalities
===============

This section provides detailed information about the functionalities provided by the `savepip` library through CLI commands.

Commands
--------

- `savepip mk-category <name>`: Creates a new category with the given name.

  - **Example**:

    .. code-block:: bash
    
       savepip mk-category datascience

- `savepip use-category <name>`: Sets the current category to the given name.

  - **Example**:

    .. code-block:: bash
       
       savepip use-category datascience

- `savepip install [dependencies]`: Installs an adds dependencies to the current category.

  - **Example**:

    .. code-block:: bash
       
       savepip install matplotlib numpy pandas

- `savepip save [-c [categories...]]`: Retrieves the list of package dependencies for the specified categories and save them in `requirements.txt`.

  - **Example**:

    .. code-block:: bash

       savepip save -c webdev datascience

- `savepip cur-category`: Returns the name of the current category.

  - **Example**:

    .. code-block:: bash

       savepip cur-category
       datascience
    
- `savepip ls-categories`: Lists all categories along with a flag indicating whether each category is the current category.
  
  - **Example**:

    .. code-block:: bash

       savepip ls-categories
       * datascience
         default