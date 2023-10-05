#!/usr/bin/python3
"""Defines the modules"""

import os
from fabric.api import *


env.hosts = [
            '54.210.88.27 web-01',
            '52.91.117.155 web-02'
            ]

def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False

    uncompressed = "/data/web_static/releases/"
    archive_filename = os.path.basename(archive_path)

    put(archive_path, "/tmp/")
    with cd("/tmp"):
        run("tar -xzf {} -C {}" .format(archive_path, uncompressed))
        run("rm {}".format(archive_path))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current" .format(archive_filename))
    results = run("ls {}" .format(uncompressed)).succeeded #check if deployment was succesful

    if results:
        return True
    else:
        return False
