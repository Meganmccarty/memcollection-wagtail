Developing
==========

To create a new Django app, you can run

.. code-block:: console

    make create-app name=YOUR-APP-NAME-HERE

Be sure to add your newly created app to the ``INSTALLED_APPS`` list within
``/memcollection/settings/base.py``.

Linting
-------

I have set up `Flake8 <https://flake8.pycqa.org/en/latest/>`_ as the linter for this project. You
can run the following command to lint the Python code:

.. code-block:: console

    make lint

This command will output any errors into the terminal, but it will NOT automatically fix issues
found. You can either fix them manually, or you can run the formatting command (listed below in the
next section). I have noticed that long lines of strings (like code comments) often have to be fixed
manually.

Formatting
----------

For formatting, I chose to use `Black <https://black.readthedocs.io/en/stable/>`_. You can format
the Python code by running

.. code-block:: console

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

.. code-block:: console

    make test

I set the verbosity to be a little higher (2, vs the default of 1), as I like seeing more details
outputted in the terminal. This setting can be changed by altering the ``test`` command in the
Makefile.

I've also installed `Coverage <https://coverage.readthedocs.io/en/7.6.4/>`_ in this project. You can
see the overall test coverage by running

.. code-block:: console

    make coverage
