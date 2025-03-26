import sys
import os
import importlib

from django.shortcuts import render
from django.core.management import execute_from_command_line
from django.urls import path
from django.http import HttpResponseNotFound, HttpResponse


ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='secret'
TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__))],
        'APP_DIRS': False,
    }
]


def home(request):
    modules = [name for name in sys.builtin_module_names if not name.startswith("_")]
    return render(request, template_name="home.html", context={"list_of_modules":modules, "doc": True})


def handler(request, module_name):
    try:
        return render(
            request,
            template_name="home.html",
            context={
                "list_of_modules": [
                name for name in dir(importlib.import_module(module_name))
                if not name.startswith("_")
                ],
                "name": module_name,
            }
        )
    except ModuleNotFoundError:
        return HttpResponseNotFound("Please enter correct name of module")
    

def doc_of_function(_, module_name, function):
    try:
        function = getattr(importlib.import_module(module_name), function)
        return HttpResponse(function.__doc__, content_type="text/plain")
    except ( AttributeError, ModuleNotFoundError):
        return HttpResponseNotFound("Please check your url and enter correct attribute and module name")


urlpatterns = [
    path('doc/', home),
	path('doc/<module_name>', handler),
	path('doc/<module_name>/<function>', doc_of_function)
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
