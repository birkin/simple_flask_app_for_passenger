# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, sys


CONFIG_DIR = os.path.dirname( os.path.abspath(__file__) )
PROJECT_DIR = os.path.dirname( CONFIG_DIR )  # flask_test
PROJECT_STUFF_DIR = os.path.dirname( PROJECT_DIR )  # dir enclosing flask_test
sys.path.append( PROJECT_DIR )
sys.path.append( PROJECT_STUFF_DIR )  # allows statements like `from flask_test.the_app import...`

activate_this = os.path.join( PROJECT_STUFF_DIR, 'env_flasktest/bin/activate_this.py' )
execfile( activate_this, dict(__file__=activate_this) )

from flask_test.the_app import app as application
