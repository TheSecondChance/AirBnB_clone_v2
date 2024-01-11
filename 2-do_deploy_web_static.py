#!/usr/bin/python3
"""Fabric script"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.91.154.49', '54.197.206.197']


def do_deploy(archive_path):
    """distributes web servers"""
    if exists(archive_path) is False:
        return False
    try:
        mezge = archive_path.split("/")[-1]
        no_ext = mezge.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(mezge, path, no_ext))
        run('rm /tmp/{}'.format(mezge))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
