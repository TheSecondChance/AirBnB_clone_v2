#!/usr/bin/python3
"""Fabric script"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['52.91.154.49', '54.197.206.197']


def do_pack():
    """generates a tgz archive"""
    try:
        zize = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        yzeSmem = "versions/web_static_{}.tgz".format(zize)
        local("tar -cvzf {} web_static".format(yzeSmem))
        return yzeSmem
    except:
        return None


def do_deploy(archive_path):
    """distributes archive web servers"""
    if exists(archive_path) is False:
        return False
    try:
        yeSem = archive_path.split("/")[-1]
        anoth = yeSem.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, anoth))
        run('tar -xzf /tmp/{} -C {}{}/'.format(yeSem, path, anoth))
        run('rm /tmp/{}'.format(yeSem))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, anoth))
        run('rm -rf {}{}/web_static'.format(path, anoth))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, anoth))
        return True
    except:
        return False


def deploy():
    """distributes archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
