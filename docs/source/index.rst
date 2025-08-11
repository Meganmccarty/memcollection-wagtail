.. MEMCollection-Wagtail documentation master file, created by
   sphinx-quickstart on Fri May 23 22:49:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MEMCollection-Wagtail
=====================

MEM Collection is a (perpetual work-in-progress) project where I manage my personal entomology
collection and my personal photo collection of live specimens. This repo represents the backend API
of the project and uses `headless Wagtail <https://wagtail.org/headless/>`_ for managing the project's
content. There are older versions of MEM Collection in different repos using different versions of
plain `Django <https://www.djangoproject.com/>`_; while I love Django, I have found working with and
in Wagtail's admin interface to be an even more pleasant experience. It's easier for me to start
fresh than try to update an older repo that wasn't well maintained.

As I've said, this is a perpetual, work-in-progress project. Hopefully, this is the last time I
recreate this project from scratch...

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   developing
   cicd
   deploying
   backups
   changelog
   reference/index
