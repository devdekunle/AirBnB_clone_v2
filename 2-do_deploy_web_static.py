#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers,
using the function do_deploy:
"""
import os
from fabric.api import *

# specify the hosts and run the command across the systems
env.username = 'ubuntu'
env.hosts = ['ubuntu@100.24.236.208', 'ubuntu@54.146.75.104']
env.key_file = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    arch_file = os.path.basename(archive_path)
    file_name = arch_file.replace(".tgz", "")
    folder = "/data/web_static/releases/{}/".format(file_name)
    status = False

    try:
        # upload the archive to the /tmp/ directory of web server
        put(archive_path, "/tmp/{}".format(file_name))

        # create directory to extract archive into
        run("mkdir -p {}".format(folder))

        # uncompress the archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder))

        # delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))

        # copy all static files to created directory
        run("mv {}web_static/* {}".format(folder, folder))

        run("rm -rf {}web_static".format(folder))

        # delete the symbolic link
        run("rm -rf /data/web_static/current")

        # create sybmolic link to static files directory
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed")
        status = True
    except Exception:
        status = False
    return status
