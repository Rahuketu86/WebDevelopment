#!/usr/bin/env python

import os, sys

#print os.path.abspath(os.path.dirname(__file__),'..')
#sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from tumblog import app
from flask.ext.script import Manager, Server

manager = Manager(app)

manager.add_command("runserver",Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0'                       
    ))

if __name__ == '__main__':
    manager.run()