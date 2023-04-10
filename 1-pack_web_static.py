#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo,
using the function do_pack.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ This function generates a .tgz archive from the contents of the
        web_static folder of AirBnB Clone v2, using the function do_pack.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    archived_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(

    time.year,
    time.month,
    time.day,
    time.hour,
    time.minute,
    time.second)
    try:
        print("Packing web_static to {}".format(archived_file))
        local("tar -zvcf {} web_static/".format(archived_file))
        archived_size = os.stat(archived_file).st_size
        print("web_static packed: {} -> {}Bytes".format(archived_file, archived_size))

    except Exception:
        archived_file = None

    return archived_file
