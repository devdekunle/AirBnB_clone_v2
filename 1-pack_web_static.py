#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    archive the web_static folder using the format described
    Prototype: def do_pack():
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist)
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path
    if the archive has been correctly generated. Otherwise,
    it should return None
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
        time.second
    )
    try:
        print(f"Packing web_static to {archived_file}")
        local(f"tar -zvcf {archived_file} web_static/")
        archived_size = os.stat(archived_file).st_size
        print(f"web_static packed: {archived_file} -> {archived_size} Bytes")

    except Exception:
        archived_file = None

    return archived_file
