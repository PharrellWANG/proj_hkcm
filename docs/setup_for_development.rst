Setup for development
=====================

**Prerequisites**:

    * Python3.6

    * virtualenv

1. To start development, clone the source code from remote repository:

.. code-block:: bash

    $ git clone https://github.com/PharrellWANG/proj_hkcm.git

2. Navigate to project root dir by ``cd proj_hkcm``.

3. Setup virtual environment by ``virtualenv venv -p `which python3```.

4. Install dependencies by ``pip install -r requirements.txt``.

5. Install PostgreSQL and create a database for crimemap. Refer to ``./proj_hkcm/settings.py`` for database name and username.

6. Dump `.sql` file from production, copy it to dev site and restore data for your dev database.

7. Navigate to project root dir, run dev server by ``python manage.py runserver``

View the dev site by clicking https://localhost:8000/hkcm

