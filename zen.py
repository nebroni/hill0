import sys
import this

from django.core.management import execute_from_command_line
from django.urls import path
from django.shortcuts import render


ROOT_URLCONF=__name__
DEBUG=True
SECRET_KEY='secret'
TEMPLATES = [
    {
        "BACKEND": 'django.template.backends.django.DjangoTemplates',
        "DIRS": ['templates/']
    }
]

title, _, *quotes = "".join([this.d.get(i, i) for i in this.s]).splitlines()


def home(request):
    return render(request, "home.html", {"quotes": quotes})


def index(request, index):
    return render(request, "index.html", {"title": title, "quote": quotes[index]})


urlpatterns = [
    path("quotes/", home),
    path("quotes/<int:index>", index),
]


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
