import sys
import this
from random import choice

from django.conf import settings
from django.core.management import execute_from_command_line
from django.urls import path
from django.http import HttpResponse

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True
)

title, _, *quotes = "".join([this.d.get(i, i) for i in this.s]).splitlines()

template = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{quote}</h1>
</body>
</html>
"""

def hello(request):
    return HttpResponse(template.format(title=title, quote=choice(quotes)))


urlpatterns = [
    path("", hello),
]

execute_from_command_line(sys.argv)
