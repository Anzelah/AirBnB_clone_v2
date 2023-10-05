#!/usr/bin/python3
"""Defines the modules"""

import os
from fabric.api import *


env.hosts = [
            '54.210.88.27',
            '52.91.117.155'
            ]

def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False
    
    filename = archive_path.split('/')[-1]
    archive_filename = os.path.splitext(archive_path)[0]
    uncompressed = "/data/web_static/releases/{}/" .format(archive_filename)
    fname_noext = os.path.splitext(filename)[0]

    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}/" .format(fname_noext))
#    with cd("/tmp"):
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/" .format(filename, fname_noext))
    run("rm /tmp/{}".format(filename))
    run("mv data/web_static/releases/{}/web_static/* data/web_static/releases/{}/" .format(fname_noext, fname_noext))
    run("rm -rf {}web_static" .format(filename))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current" .format(archive_filename))
    results = run("ls {}" .format(uncompressed)).succeeded #check if deployment was succesful

    if results:
        return results
    else:
        return False
