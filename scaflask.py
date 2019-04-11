"""
Scaffold together a basic Flask project, meant to 
be run in the project's base directory. Uses Pipenv, 
but does not need to be pre-installed to run.

# Packages to be installed

* Flask
* Flask-SQLAlchemy
* Flask-WTForms
* Flask-Security 

# Project structure
-package_name
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
from os import mkdir, chdir
from subprocess import call

# Create a virtualenv w/ pipenv, and install packages inside it
def pipenv():

    # Make sure pip is up-to-date
    call('python -m pip install --upgrade pip')
    # Install pipenv, if it is not already installed
    call('pip install pipenv')
    call('pipenv install flask')
    call('pipenv install flask-sqlalchemy')
    call('pipenv install flask-wtf')
    call('pipenv install flask-security')
    call('git init') # Initialize empty git repo

# Create project root directory
def create_root():
    
    # Prompt the user for a package name
    pkg_name = input('Enter a name for your Flask package: ')
    # Throw an exception is package name is null
    if not pkg_name:
        raise Exception('Package name cannot be null!')

    mkdir(pkg_name) 
    open('app.py', 'a')
    chdir(pkg_name) # Change into the package directory
    open('models.py', 'a')
    open('forms.py', 'a')
    open('routes.py', 'a')
    open('__init__.py', 'a')

# Create templates directory
def create_templates():

    mkdir('templates') 
    # Create a layout template in dir for other templates to inherit from
    open('templates/layout.html', 'a') 

# Create static files directory    
def create_static():

    mkdir('static')
    # Create CSS dir and main.css file, if it doesn't already exist
    mkdir('static/css')
    open('static/css/main.css', 'a') 
    # Create JS dir and main.js file, if it doesn't already exist
    mkdir('static/js') 
    open('static/js/main.js', 'a')
    # Create an images dir
    mkdir('static/img') 

# Create directory for unit tests
def create_tests():

    mkdir('tests')

def main():

    pipenv()
    create_root()
    create_templates()
    create_static()
    create_tests()

main()
