# setup script for py2exe to create the rfc2217_server.exe

from distutils.core import setup
import glob
import os
import sys
import py2exe

sys.path.insert(0, '..')

sys.argv.extend("py2exe --bundle 1".split())

setup(
    name='rfc2217_server',
    zipfile=None,
    options = {"py2exe": {
        'dll_excludes': [],
        'includes': [
                'serial.urlhandler.protocol_hwgrep', 'serial.urlhandler.protocol_rfc2217',
                'serial.urlhandler.protocol_socket', 'serial.urlhandler.protocol_loop',],
        'dist_dir': 'bin',
        'excludes': ['serialjava', 'serialposix', 'serialcli'],
        'compressed': 1,
        },
    },
    console = [
        "rfc2217_server.py",
    ],
)
