# Recipe App Api
Backend built with DRF

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework that builds better web APIs with less code.
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
* [Docker](www.docker.com/): Docker is a software platform that simplifies the process of building, running, managing and distributing applications.
* [Swagger](www.docker.com/): Swagger generates awesome interactive webpage to interact with RESTful APIs.


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/ilkhom19/recipe-app-api.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd recipe
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  env -p python3
            $ source env/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/docs
    ```
