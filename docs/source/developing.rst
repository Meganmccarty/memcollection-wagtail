Developing
==========

To create a new Django app, you can run

.. code::

    make create-app name=YOUR-APP-NAME-HERE

Be sure to add your newly created app to the ``INSTALLED_APPS`` list within
``/memcollection/settings/base.py``.

Linting
-------

I have set up `Flake8 <https://flake8.pycqa.org/en/latest/>`_ as the linter for this project. You
can run the following command to lint the Python code:

.. code::

    make lint

This command will output any errors into the terminal, but it will NOT automatically fix issues
found. You can either fix them manually, or you can run the formatting command (listed below in the
next section). I have noticed that long lines of strings (like code comments) often have to be fixed
manually.

Formatting
----------

For formatting, I chose to use `Black <https://black.readthedocs.io/en/stable/>`_. You can format
the Python code by running

.. code::

    make format

This command WILL automatically format files, and it'll output in the terminal how many files are
formatted or left unchanged.

Testing
-------

My aim is to have comprehensive test coverage for the various Django apps within the project. I'm
using `unittest <https://docs.python.org/3/library/unittest.html>`_ for, well, the unit tests, as
it's built into the Python Standard Library (I've heard pytest is better, but I'm too lazy to try to
figure out how to configure it in this project). Maybe someday, I'll write a few integration tests
for the different models, but I feel that unit tests provide sufficient test coverage for this
project.

You can execute the tests by running

.. code::

    make test

I set the verbosity to be a little higher (2, vs the default of 1), as I like seeing more details
outputted in the terminal. This setting can be changed by altering the ``test`` command in the
Makefile.

I've also installed `Coverage <https://coverage.readthedocs.io/en/7.6.4/>`_ in this project. You can
see the overall test coverage by running

.. code::

    make coverage

Documenting
-----------

I've set up Sphinx to generate docs from both the ``docs/`` directory, as well as auto-generate docs
from the docstrings present in my apps' various ``models.py`` files (I could have included
docstrings from other types of files, like viewsets and serializers, but the docstrings in those
files are all very similiar to each other, so I didn't see the point). At some point, I plan to host
the statically-generated HTML doc files, but in the mean time, these files can be viewed locally by
running

.. code::

    make build-docs

This will create a ``build/`` folder under ``docs/``. Opening ``build/html/index.html`` in your
browser of choice will allow you to navigate the docs as though they are hosted on a server or S3
bucket.
