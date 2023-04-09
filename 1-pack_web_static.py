#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
import os
from fabric.api import local, runs_once
from datetime import datetime


@runs_once
def do_pack():
    """Archive the web_static folder using the format described """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    archived_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    try:
        print(f"Packing web_static to {archived_file}")
        local(f"tar -zvcf {archived_file} web_static/")
        archived_size = os.stat(archived_file).st_size
        print(f"web_static packed: {archived_file} -> {archived_size}Bytes")

    except Exception:
        archived_file = None

    return archived_file
