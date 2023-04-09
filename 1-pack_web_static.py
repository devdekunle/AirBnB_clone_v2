#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo,
using the function do_pack."""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """This function generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone v2, using the function do_pack.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now.strftime("%Y%m%d%H%M%S")
    archived_file = "versions/web_static_{time}.tgz"
    try:
        print(f"Packing web_static to {archived_file}")
        local(f"tar -zvcf {archived_file} web_static/")
        archived_size = os.stat(archived_file).st_size
        print(f"web_static packed: {archived_file} -> {archived_size}Bytes")

    except Exception:
        archived_file = None

    return archived_file
