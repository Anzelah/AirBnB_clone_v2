#!/usr/bin/python3
"""Defines the modules"""

import os
from fabric.api import *
import datetime


env.hosts = [
            '54.210.88.27',
            '52.91.117.155'
            ]


def do_pack():
    """generate a .tgz archive from contents of my web_static folder"""

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    timestamp = ("{}{}{}{}{}{}" .format(year,
                 month, day, hour, minute, second))

    if not os.path.exists("versions"):
        local("mkdir versions")

    filep = local("tar -cvzf versions/web_static_{}.tgz web_static"
                  .format(timestamp))

    if filep.return_code == 0:
        return ("versions/web_static_{}.tgz" .format(timestamp))
    else:
        return None


def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False

    archive = archive_path.split('/')[-1]
    archive_noext = os.path.splitext(archive)[0]
    extract_folderpath = "/data/web_static/releases/"
    extracted = extract_folderpath + archive_noext

    put(archive_path, "/tmp/")
    run("mkdir -p {}/" .format(extracted))  # extract files to if not present
    run("tar -xzf /tmp/{} -C {}/" .format(archive, extracted))
    run("rm /tmp/{}" .format(archive))
    run("rm -rf /data/web_static/current")
    run("ln -s {}/ /data/web_static/current" .format(extracted))

    return True


def deploy():
    """creates and distributes an archive to your web servers"""

    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    results = do_deploy(archive_path)

    return results
