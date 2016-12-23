# :pineapple: Aloha Python :snake:

## Introduction
This is a sample `Django` application serving one of the world's most disruptive messages in software. The next subsequent sections will discuss how to serve the application locally as well as deployment instructions.

This guide assumes the user already has [Python](https://www.python.org/downloads/) installed.

## Up and Running
Create a virtual environment:

`python3 -m venv <env-name>`

Activate the environment:

`source <env-name>/bin/activate`

Install Django:

`pip install django~=1.10.0`

Upgrade `pip`:

`pip install --upgrade pip`

Clone the project to a directory of your choice (e.g. ~/Projects), and always ensure you are in your virtual environment. `cd` into the cloned project directory, and install its requirements:

`pip install -r requirements.txt`

Start the server:

`python manage.py runserver`

Visit the application in-browser:

`127.0.0.1:8000`

## Deploying
Please create an account at [Heroku](http://heroku.com) and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Send an email to tara.planas@gmail.com to be added to the Collaborators list of deployers. After you are added, add the Heroku remote to the project directory:

`heroku git:remote -a aloha-python`

To deploy: `git push heroku master`

In the not too distant future, we will be adding a continuous integration system, and upon each successful test suite run, deployments will be automatically sent.

---

## Notes
`Django` was chosen due to it having incredible documentation sources. The `WhiteNoise` dependency supports Django serving static files in production, and obviously, the one static CSS file accompanying the displayed message is not to be breezed over.

Ideally, it would make sense to run several pipelines from `test` -> `staging` and `staging -> production` instances with automatic deploys upon successful CI runs in the future.
