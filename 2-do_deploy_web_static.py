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

    archive = archive_path.split('/')[-1]
    archive_noext = os.path.splitext(archive)[0]
    extract_folderpath = "/data/web_static/releases/"
    extracted = extract_folderpath + archive_noext

    put(archive_path, "/tmp/")
    run("mkdir -p {}" .format(extracted)) #mkdir to extract files to if not present
    run("tar -xzf /tmp/{} -C {}/" .format(archive, extracted))
    run("rm /tmp/{}" .format(archive))
    run("mv {}/web_static/* {}" .format(extracted, extracted))
    run("rm -rf {}/web_static" .format(extracted))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current" .format(extracted))

    results = run("ls {}" .format(extracted))
    if results.succeeded:
        return True
    else:
        return False
