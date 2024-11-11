# MEM Collection (Wagtail)

MEM Collection is a (perpetual work-in-progress) project where I can manage my personal entomology collection and my personal photo collection of live specimens. This repo represents the backend API of the project and uses [headless Wagtail](https://wagtail.org/headless/) for managing the project's content. There are older versions of MEM Collection in different repos using different versions of plain [Django](https://www.djangoproject.com/); while I love Django, I have found working with and in Wagtail's admin interface to be an even more pleasant experience. It's easier for me to start fresh than try to update an older repo that wasn't well maintained.

As I've said, this is a perpetual, work-in-progress project. :)

## Getting Started
This project will likely be something no one else will want to play with, but the steps to getting a local working copy up and running are below.

First, clone this repo from GitHub.

### Environment Variables
You'll need to create an `.env` file in the project's root directory. Both Django and Docker expect a few environment variables to be present to properly run.

After creating the `.env` file, add the following variables to it:
```
    DATABASE_NAME=postgres
    DATABASE_PASSWORD=postgres
    DATABASE_USER=postgres
    SECRET_KEY=Your Django Secret Key Here
```
You can use a [secret key generator](https://djecrety.ir/) for the `SECRET_KEY` value.

### Docker
This project uses [Docker Compose](https://docs.docker.com/compose/) to manage containers (one for the Wagtail web app, and another for the Postgres database). 

If you're using a Macbook with an M1/M2/M3 chip, you'll need to use a different set of commands. Because these commands are a bit unwieldy, I created a Makefile to make typing the commands out easier. Feel free to look in the Makefile to see what these commands are actually doing under-the-hood. You can also run `make help` for a list of all the available Makefile commands (and what they do!).

### Building and Spinning Up Containers

To build an image (non-M chip), run
```
    make build
```
or, if on an M chip, run
```
    make mac-build
```

Once the image finishes building, run
```
    make up
```
or
```
    make mac-up
```
to spin up the containers.

After the containers are up, you should find that two services have been created: one for the Wagtail app, and another for the Postgres database. You could be able to access the app at http://localhost:8000/.

You may need to run migrations before anything else. To do so, run the following in a separate terminal:
```
    make makemigrations
    make migrate
```

You'll then need to create a user account to access the Wagtail admin. In the terminal, run:
```
    make createsuperuser
```
You should then be prompted in the terminal for credentials. You can press enter to select the defaults (user = 'wagtail', email = '') and input a password. Afterwards, use your newly-created user account to log into the Wagtail admin at http://localhost:8000/admin.

### Stopping and Tearing Down Containers
To stop the containers, press `Ctrl+C` in the terminal where your containers are running.

If you want to tear down the containers, simply run the following:
```
    make down
```
This command works for both non-M chip and M chip laptops. It will NOT wipe out the contents of your database, as they are stored on a volume (`/postgres-data`) within the project directory.

If you find you want to wipe out everything, simply run:
```
    make prune
```
This will prune your system, containers, images, and volumes. Be careful with this command!

If, while developing, you find you need to rebuild an image without caching, there's a command for that:
```
    make build-no-cache
```
or
```
    make mac-build-no-cache
```

## Developing
To create a new Django app, you can run
```
    make create-app name=YOUR-APP-NAME-HERE
```
Be sure to add your newly created app to the `INSTALLED_APPS` list within `/memcollection/settings/base.py`.

### Linting
I have set up [Flake8](https://flake8.pycqa.org/en/latest/) as the linter for this project. You can run `make lint` to lint the Python code.

### Formatting
For formatting, I chose to use [Black](https://black.readthedocs.io/en/stable/). You can format the Python code by running `make format`.

## Deploying
This project is deployed to [Fly.io](https://fly.io/). GitHub Actions is configured to deploy the project whenever changes are pushed to the main branch.

However, there are still some little quirks I have yet to work out. For example, the only way to configure the prod environment variables is to do either one of the following:

1. Manually update them on the Fly.io Dashboard
2. Update them locally in a `.env.production` file and then run `make fly-secrets`

I haven't figured out how to pass secrets from GitHub to GitHub Actions without having to manually authenticate to Fly.io.

### Manually Deploying
I also configured the project in such a way that I can deploy from my laptop. (Actually, I did that first to see if it worked before trying to do so via GitHub Actions, and then I was too lazy to remove this feature once I got GitHub Actions working.)

These steps below are more for me than for anyone else, as they assume you've completed the following tasks:
* Set up hosting for media assets (using [Backblaze B2 Cloud Storage](https://www.backblaze.com/cloud-storage))
* Set up hosting for the actual web app (using Fly.io)
* Set up a `.env.production` file for storing secrets used in the prod environment

Wagtail has a [nice guide for deploying to Fly.io](https://docs.wagtail.org/en/stable/deployment/flyio.html), which is what I used initially. However, I deviated from the instructions towards the end; after running `fly launch`, I chose to NOT overwrite my `.dockerignore` or my `Dockerfile`, as doing so led to deployment errors. I then found and used [Tom Usher's blog series on deploying Wagtail to Fly.io](https://usher.dev/posts/2022-08-30-wagtail-on-flyio/part-1/) to get me over the hump of deployment errors.

After the initial setup is done, you can run
```
    make fly-auth
```
to authenticate (if you aren't already authenticated). Once that's done, you can deploy by running
```
    make fly-deploy
```
