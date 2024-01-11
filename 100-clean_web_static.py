#!/usr/bin/python3
# Fabfile to delete out-of-date
import os
from fabric.api import *

env.hosts = ['52.91.154.49', '54.197.206.197']
env.user = "ubuntu"


def do_clean(number=0):
    """Delete archive out-of-date
    Args:
        number (int): The number of archives to keep
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
