activate_this = '/home/deploy/virtualenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
os.environ['PYTHON_EGG_CACHE'] = '/home/deploy/.python-eggs'

import sys
sys.path.append('/var/www')

from myapp import create_app
import config

application=create_app(config)

