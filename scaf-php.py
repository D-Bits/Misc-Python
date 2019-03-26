"""
# Directory and file structure to scaffold
-src
 |__/admin
 |   |_index.php 
 |__/css
 |   |_main.css
 |__/images
 |__/includes
 |__/js
 |  |_main.js
 |
 |__index.php
"""
import os

# Create project's base directory
def root():

    os.mkdir('src/') 
    open('src/index.php', 'a')

# Create the admin dir, with an index file
def admin():

    os.mkdir('src/admin')
    open('src/admin/index.php', 'a')

# Create a directory for stylesheets, with a main.css
def css():

    os.mkdir('src/css')
    open('src/css/main.css', 'a')

# Create a directory for stylesheets, with a main.css
def images():

    os.mkdir('src/images')

# Create a directory for includes, with a header, and footer include
def includes():

    os.mkdir('src/includes')
    open('src/includes/header.php', 'a')
    open('src/includes/footer.php', 'a')

# Create a directory for js files
def js():

    os.mkdir('src/js')
    open('src/js/main.js', 'a')

def main():

    root()
    admin()
    css()
    images()
    includes()
    js()

main()