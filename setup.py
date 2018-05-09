#!/usr/bin/env python
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pythreatgrid',
      version='1.0.5',
      description='Python ThreatGrid API wrapper',
      long_description=read('README.md') + '\n\n' + read('HISTORY')
      author='Stephen Hosom, Rusty Bower',
      author_email='0xhosom@gmail.com, rusty@rustybower.com',
      download_url='https://github.com/RustyBower/pythreatgrid/archive/v1.0.5.tar.gz',
      url='https://github.com/RustyBower/pythreatgrid',
      packages=['pythreatgrid'],
      install_requires=['requests'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ]
      )
