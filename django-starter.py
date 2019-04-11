"""
Create a Django project, in 
a virtualenv with psycopg2 installed. 
"""
from subprocess import call


# Create the virtualenv, and install packages
def pipenv():

    # Make sure pip is up-to-date
    call('python -m pip install --upgrade pip')
    # Install pipenv, if it is not already installed
    call('pip install pipenv')
    call('pipenv install django')
    call('pipenv install psycopg2')
    call('git init') # Initialize an empty git repo


""" Prompt the user for a project name, then
Run the django-admin startproject cmd  """
def create_project():
    
    proj_name = input("Enter a project name: ")
    call('django-admin.exe startproject ' + proj_name)
    
    # Throw an exception is proj_name is null
    if not proj_name:
        raise Exception('Project name cannot be null!')
        

# Add an app for user authentication and managment
def create_app():

    app_name = input("Enter a name for your first Django app: ")
    call('django-admin.exe startapp ' + app_name)

    # Throw an exception is app_name is null
    if not app_name:
        raise Exception('App name cannot be null!')


def main():

    pipenv()
    create_project()
    create_app()


main()