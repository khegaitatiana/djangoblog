#!/usr/bin/env python
# script that helps to manage the website.
# run server: py manage.py runserver
# create application: py manage.py startapp blog    (blog - is name of app, after running command - new folder is created with structure)
# create migration file to apply changes in db: py manage.py makemigrations blog (blog - is name of app)
# apply db changes: py manage.py migrate blog (blog - is name of app)
# create superuser: py manage.py createsuperuse
# console django: py manage.py shell

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simpleBlog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
