#!/usr/bin/python3
"""Defines a module"""

from fabric.api import *
import datetime
import os

def do_pack():
    """generate a .tgz archive from contents of my web_static folder"""
    
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    timestamp = ("{}{}{}{}{}{}" .format(year, month, day, hour, minute, second))
    
    if not os.path.exists("versions"):
        local("mkdir versions")
    filep = local("tar -cvzf versions/web_static_{}.tgz web_static".format(timestamp))
    if filep.return_code == 0:
        return ("versions/web_static_{}.tgz" .format(timestamp))
    else:
        return None

    do_pack()
