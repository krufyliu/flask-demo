from fabric.api import *

env.hosts = ['192.168.33.10']
env.user = 'vagrant'
env.password = 'vagrant'

def package():
  local('python setup.py sdist --format=gztar', capture=False)

def deploy():
  dist = local('python setup.py --fullname', capture=True).strip()
  put('dist/%s.tar.gz' % dist, '/tmp/myapp.tar.gz')
  run('mkdir /tmp/myapp')
  with cd('/tmp/myapp'):
    run('tar xzf /tmp/myapp.tar.gz')
    with cd('/tmp/myapp/%s' % dist):
      run('/home/vagrant/test/bin/python setup.py install')
  run('rm -rf /tmp/myapp /tmp/myapp.tar.gz')
  # run('touch /var/www/myapp.wsgi')