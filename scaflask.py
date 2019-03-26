"""
Scaffold together a basic Flask project, meant to 
be run in the project's base directory. Uses Pipenv, 
but does not need to be installed to run.

# Project structure
-src
 |__/templates
 |   |_layout.html
 |__/static
 |   |__/css
 |   |   |_main.css
 |   |__/js
 |   |   |_main.js
 |   |__/img
 |__/tests
 |__app.py
"""
from os import mkdir
from subprocess import call

# Create a virtualenv w/ pipenv, and install packages inside it
def pipenv():

    # Install pipenv, if it is not already installed
    call('pip install pipenv')
    call('pipenv install flask')
    call('pipenv install flask-sqlalchemy')

# Create project root directory
def create_root():
    
    mkdir('src/') 
    open('src/app.py', 'a')
    open('src/models.py', 'a')
    open('src/forms.py', 'a')
    open('src/routes.py', 'a')
    open('src/__init__.py', 'a')

# Create templates directory
def create_templates():

    mkdir('src/templates') 
    # Create a layout template in dir for other templates to inherit from
    open('src/templates/layout.html', 'a') 

# Create static files directory    
def create_static():

    mkdir('src/static')
    # Create CSS dir and main.css file, if it doesn't already exist
    mkdir('src/static/css')
    open('src/static/css/main.css', 'a') 
    # Create JS dir and main.js file, if it doesn't already exist
    mkdir('src/static/js') 
    open('src/static/js/main.js', 'a')
    # Create an images dir
    mkdir('src/static/img') 

# Create directory for unit tests
def create_tests():

    mkdir('src/tests')

def main():

    pipenv()
    create_root()
    create_templates()
    create_static()
    create_tests()

main()
