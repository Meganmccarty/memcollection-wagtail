Backups
=======

.. note:: This doc really is solely for me, so that I can remember how to properly make backups AND
   restore from those backups.

Backing up data is super important for this project. Because I am hosting the data in an unmanaged
Postgres app on Fly.io, I need to ensure I have data backups in case something happens. I don't,
however, care to include any uploaded media files in the backups, as they are hosted on Backblaze
B2 (plus, I keep copies of the media files on an external hard drive, which is backed up to
a different cloud backup provider).

It's also important to me that my local environment's database matches the production one. In a
sense, the local database acts as a way for me to update the data offline (like if I'm in the field
without an internet connection). So being able to transfer the data from my local laptop to prod is
a must.

Likewise, if I somehow nuke my local environment, I'd like to be able to pull down the data from
prod back onto my local machine.

Using ``dumpdata`` and ``loaddata``
-----------------------------------

I'm making the backup process super simple by using Django's ``dumpdata`` and ``loaddata`` commands.
However, there are certain tables that aren't important to the backup (things like ``auth``, for
example), so using these commands without specificity isn't very helpful. I really only care about
the data in the custom models I've created, so those are the ones that will end up in the backup
file.

Creating a Local Backup
***********************

To make a local backup, run the following command:

.. code::

    make local-backup

This will output a ``.json`` file within the root directory, formatted as
``backup_local_memcollection_<time-stamp>.json``. This file can then be used to restore data in
prod, or it can be moved someplace else (an external hard drive or a cloud drive).

Creating a Prod Backup
**********************

.. note:: My fly app currently scales to zero after a short period of inactivity. So first navigate
   to the prod URL to wake up the app before attempting any of the commands in this section.

The process is similar to making a local backup, but first, I need to ``ssh`` into my fly app.

.. code::

    fly ssh console
    make prod-backup
    exit

Like with the local backup method, the outputted backup file will be a ``.json`` file in the
project's root directory. It'll have a similar naming convention as the local backup file, except
the word ``prod`` will replace the word ``local``. I figured this was important to prevent any
potential foot-guns of accidentally loading the wrong file into the wrong database.

Now that I have a prod backup, I can run the following:

.. code::

    fly ssh sftp shell
    put /path/to/remote/file path/to/local/file

With the prod backup now on my machine, I can either use it to restore my local environment or move
it into a different backup location.

Restoring a Backup
******************

Restoring data into the local database is super easy. First, make sure the backup file is located
in the project's root directory, then simply run:

.. code::

    make local-restore

Boom! Data should be loaded in.

Now, restoring data into the prod database requires a few more steps.

.. note:: Again, my fly app currently scales to zero after a short period of inactivity. Wake it up
   first before attempting any commands below!

First, this assumes that the backup file I want to restore from is located on my local machine (I
don't plan on storing backup files on fly, because it's supposed to just host my app's files!). So,
copy over the local backup file into fly:

.. code::

    fly ssh sftp shell
    put path/to/local/file /path/to/remote/file

Now that the file is on fly, exit out of that terminal, and then run:

.. code::

    fly ssh console
    make prod-restore

Boom! Data from the backup file should now be in the prod environment.
