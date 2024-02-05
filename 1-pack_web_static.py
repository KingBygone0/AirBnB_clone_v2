#!/usr/bin/python3
# fabfile to generate a .tgz archive from the content of web static

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    if local("tar -cvzf {} web_static".format(file)).failed:
        return None

    return file
