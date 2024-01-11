#!/usr/bin/python3
from datetime import datetime
import os
from fabric.api import *

env.hosts = ['localhost']

def do_pack():
    try:
        mezeg = "versions/web_static_" + datetime.now().\
                   strftime("%Y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -zcvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        web_static")
        print("web_static packed: {} -> {}".
              format(mezeg, os.path.getsize(mezeg)))
    except:
            return None
