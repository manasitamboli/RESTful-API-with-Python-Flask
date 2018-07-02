#!/bin/bash

cd /usr/src/app/src
pip install virtualenv
virtualenv flask
source flask/bin/activate
flask/bin/pip install Flask
flask/bin/pip install flask_cors
