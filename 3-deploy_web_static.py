#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

def deploy():
""" This function fully deploys the web_static to the web servers"""

