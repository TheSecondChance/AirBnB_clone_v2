#!/usr/bin/python3
"""
script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    compress
    """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        mezegb = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(mezegb))
        return mezegb
    except BaseException:
        return None
