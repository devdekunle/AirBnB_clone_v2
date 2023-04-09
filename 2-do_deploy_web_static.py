#!/usr/bin/pyhton3
"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers,
using the function do_deploy:
"""
import os
from fabric.api import *

# specify the hosts and run the command across the systems
env.username = 'ubuntu'
env.hosts = ['100.24.236.208', '54.146.75.104']

def do_deploy(archive_path):
    """
    deploys the content of the archived file
    """
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split(".")

    #upload the archive to the /tmp/ directory of web server
    put(archive_path, "/tmp/")
    print("Hello")

    #create directory to extract archive into
    run(f"mkdir -p /data/web_static/releases/{file_name[0]}")

    #uncompress the archive
    run(f"tar -xzf /tmp/{archive_path} -C /data/web_static/releases/{file_name[0]}/")


    #delete the archive from the web server
    run(f"rm -rf /tmp/{archive_path}")

    #copy all static files to created directory
    run(f"mv /data/web_static/releases/{file_name[0]}/web_static/* /data/web_static/releases/{file_name[0]}/")

    run(f"rm -rf /data/web_static/releases/{file_name[0]}/web_static")

    #delete the symbolic link
    run("rm -rf /data/web_static/current")

    #create sybmolic link to static files directory
    run(f"ln -s /data/web_static/releases/{file_name[0]} /data/web_static/current")
    print("New version deployed")
    return True
