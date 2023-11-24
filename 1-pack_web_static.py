#!/usr/bin/python3
"""web server distribution
    """

from datetime import datetime
from fabric.api import *
import tarfile
import os.path
import re


def do_pack():
    """distributes an archive to your web servers
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
