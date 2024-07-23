#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

import os
from os.path import exists
from datetime import datetime
from fabric.api import env, local, put, sudo, runs_once

# Hosts IP and user of the web server web-01 and web-02
env.hosts = ["54.157.136.194", "100.25.134.41"]


def do_install():
    """Installs a MySQL Server on remote machines.

    Returns:
        False - if the installation failed.
        Otherwise - True.
    """
    try:
        sudo('wget -O mysql57 {}{}'.format(gh_user, gh_repo))
        sudo('chmod +x mysql57')
        sudo('./mysql57')

        print("MySQL 5.7 successfully installed!")
        return True
    except Exception as e:
        print("Something failed! Try another method.")
        return False

def do_config(script):
    """Installs a MySQL Server on remote machines.

    Returns:
        False - if the installation failed.
        Otherwise - True.
    """
    try:
        put(script, '/tmp/')
        sudo('cd ~')
        sudo('mysql < /tmp/{}'.format(script))

        print("Configuration successfully added!")
        return True
    except Exception as e:
        print("Something failed! Try another method.")
        return False
