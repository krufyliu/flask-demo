from setuptools import setup

setup(
  name='MyApp',
  version='1.1',
  long_description=__doc__,
  packages=['myapp', 'myapp.main', 'myapp.admin'],
  include_package_data=True,
  zip_safe = False,
  install_requires=[
    'Flask>=0.10',
    'Flask-Mail>=0.9',
    'Flask-SQLAlchemy>=2.1'
  ]
)