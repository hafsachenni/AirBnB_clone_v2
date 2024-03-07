#!/usr/bin/python3
"""this a fabric that distributes a compressed
archive to both of my web servers"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.167.198.176', '35.175.102.14']


def do_deploy(archive_path):
    """deploying the compressed archive to my servers"""
    if exists(archive_path) is False:
        return False

    nameof_file = archive_path.split('/')[-1]
    filename = nameof_file.split('.')[0]

    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}/"
        .format(filename))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(nameof_file, filename))
    run("rm /tmp/{}".format(nameof_file))
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/"
        .format(filename, filename))
    run("rm -rf /data/web_static/releases/{}/web_static"
        .format(filename))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename))

    print("New version deployed!")
    return True
