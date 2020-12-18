# Getting Started with Django #
Starting a project with the Django framework involves some basic first steps for almost any project. I use Visual Studio Code so this walkthrough will primarily focus around that.

## Starting a Project ##
To start a project, create a folder with the name of the project. Use ```Ctrl + ` ``` to open the terminal in VS Code.
Inside the terminal, enter: ```django-admin startproject projectName``` to start the project. If that does not work, try adding __py__, __python3__ or __python3 -m___ and see if that solves the problem

Once the project has started, change directories to the name of the project so: ```cd projectName```
Once inside that directory, run the command: ```py manage.py startapp core``` which will create the basic files we need.
Find the file ```settings.py``` and add ``` `core.apps.CoreConfig` ``` to the list under ```INSTALLED_APPS```

After this, we can start migrating to the database and creating the website/app. Run ```py manage.py migrate``` to make those migrations. Afterwards, run ```py manage.py createsuperuser``` to establish an admin.
You can check to make sure you did this correctly by running ```py manage.py runserver``` and you should see the Django hello world screen.

## Views, Templates, etc. ##
We are going to use a template to provide all the HTML, CSS, JS, etc. we need for a decent site. Inside the ```core``` folder create a new folder called ```templates``` where we will store the files we get from the template.

Find the ```views.py``` file. We will need to add a view for the ```index.html``` file. It should look like this:
```
from django.shortcuts import render
from django.views import View

class Index(View):
  template = 'index.html'
  
  def get(self, request):
    return render(request, self.template)
```
Now find ```urls.py``` so we can add the route:
```
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.Index.as_view(), name='index')
]
```
Now, if you go back to the server it will have the HTML but it will look __awful__ because we have not included any CSS. So, we will do that now.

Go back to the ```core``` folder and create a new folder named ```static```. From whatever template you have, but the files ```css```,```js```,```vendor```, or ```assets``` inside of that static folder.
Navigate to your ```index.html``` file and add the ```/static/``` to the CSS links so it can find the CSS. Return the server and if you did this correctly, it will look much better.

