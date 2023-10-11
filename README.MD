## Command that performs the installation of new startapp in django
sudo docker-compose exec app python manage.py startapp src

## makemigrations

Django manages the database operations with the ORM technique. Migration refers to generating a database table whose structure matches the data model declared in the app. 

The following command should be run whenever a new model is declared:
python manage.py makemigrations

## migrate

This command option of manage.py synchronizes the database state with the currently declared models and migrations. 
python manage.py migrate

## Shell

This command opens up an interactive Python shell inside the project. This is useful when you are required to perform some quick interactive operations. 
python manage.py shell

## urls.py

This script contains a list of object urlpatterns. Every time the client browser requests a URL, the Django server looks to match its pattern and routes the application to the mapped view. 

The default structure of urls.py contains a view mapped to the project’s Admin site.