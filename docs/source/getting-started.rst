Getting Started
===============

This project will likely be something no one else will want to play with, but the steps to getting a
local working copy up and running are below. (It's also good practice for me to thoroughly document
my code, as I am very liable to forget stuff.)

First, clone this repo from GitHub:

.. code-block:: console

    git clone git@github.com:Meganmccarty/memcollection-wagtail.git

Environment Variables
---------------------

You'll need to create an ``.env`` file in the project's root directory. Both Django and Docker expect
a few environment variables to be present to properly run.

After creating the ``.env`` file, add the following variables to it:

.. code-block::

    DATABASE_NAME=postgres
    DATABASE_PASSWORD=postgres
    DATABASE_USER=postgres
    DJANGO_SETTINGS_MODULE=memcollection.settings.dev
    SECRET_KEY=Your Django Secret Key Here

You can use a `secret key generator <https://djecrety.ir/>`_ for the ``SECRET_KEY`` value.

Docker
------

This project uses `Docker Compose <https://docs.docker.com/compose/>`_ to manage containers (one for
the Wagtail web app, and another for the Postgres database). 

If you're using a Macbook with an M1/M2/M3 chip, you'll need to use a different set of commands.
Because these commands are a bit unwieldy, I created a Makefile to make typing the commands out
easier. Feel free to look in the Makefile to see what these commands are actually doing
under-the-hood. You can also run ``make help`` for a list of all the available Makefile commands (and
what they do!).

Building and Spinning Up Containers
-----------------------------------

To build an image (non-M chip), run

.. code-block:: console

    make build

or, if on an M chip, run

.. code-block:: console

    make mac-build

Once the image finishes building, run

.. code-block:: console

    make up

or

.. code-block:: console

    make mac-up

to spin up the containers.

After the containers are up, you should find that two services have been created: one for the
Wagtail app, and another for the Postgres database. You could be able to access the app at
http://localhost:8000/.

You may need to run migrations before anything else. To do so, run the following in a separate
terminal:

.. code-block:: console

    make migrations
    make migrate

You'll then need to create a user account to access the Wagtail admin. In the terminal, run:

.. code-block:: console

    make createsuperuser

You should then be prompted in the terminal for credentials. You can press enter to select the
defaults (user = 'wagtail', email = '') and input a password. Afterwards, use your newly-created
user account to log into the Wagtail admin at http://localhost:8000/admin.

Stopping and Tearing Down Containers
------------------------------------

To stop the containers, press ``Ctrl+C`` in the terminal where your containers are running.

If you want to tear down the containers, simply run the following:

.. code-block:: console

    make down

This command works for both non-M chip and M chip laptops. It will NOT wipe out the contents of your
database, as they are stored on a volume (``/postgres-data``) within the project directory.

If you find you want to wipe out everything, simply run:

.. code-block:: console

    make prune

This will prune your system, containers, images, and volumes. Be careful with this command!

If, while developing, you find you need to rebuild an image without caching, there's a command for that:

.. code-block:: console

    make build-no-cache

or

.. code-block:: console

    make mac-build-no-cache
