#!/usr/bin/env python
#######################
from __future__ import print_function, unicode_literals

import os
import sys

#######################

settings_file = "biosci_siteconf.settings"


def get_virtual_env_path(base_path, default="venv", env_path_filename=".virtualenv"):
    """
    Determine the absolute path for the virtual environment.
    
    Do this by first checking for the existence of a .virtualenv file,
    and reading it for the virtual environment path.
    
    If this file or path do not exist, then fallback to the default 
    virtual environment.
    """
    path = None
    if base_path is not None and not os.path.isabs(env_path_filename):
        env_path_filename = os.path.join(base_path, env_path_filename)
    if os.path.exists(env_path_filename):
        contents = open(env_path_filename).read().strip()
        path = os.path.normpath(os.path.expanduser(contents))
        if not os.path.exists(path):
            path = None
    if path is None:
        path = default
        if base_path is not None and not os.path.isabs(path):
            path = os.path.join(base_path, path)
    return path


def activate_virtualenv(base_path):
    """
    Activate the virtual environment by determining its path
    and then executing the activate_this.py script.
    """
    venv_path = get_virtual_env_path(base_path)
    if venv_path is None:
        return

    activate_file = os.path.normpath(os.path.join(venv_path, "bin", "activate_this.py"))
    if os.path.exists(activate_file):
        execfile(activate_file, dict(__file__=activate_file))


if __name__ == "__main__":
    """
    Django manage.py, extended for flexible and automatic
    virtual environment loading.    
    """
    base_path = os.path.dirname(os.path.abspath(__file__))

    activate_virtualenv(base_path)

    # Add base path to Python Path.
    sys.path.append(base_path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_file)
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
