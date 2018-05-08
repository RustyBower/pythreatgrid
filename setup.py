#!/usr/bin/env python
import codecs
from distutils.core import setup

with codecs.open('README.md', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY', 'r', 'utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(name='pythreatgrid',
      version='1.0',
      description='Python ThreatGrid API wrapper',
      long_description=readme + '\n\n' + history,
      author='Stephen Hosom, Rusty Bower',
      author_email='0xhosom@gmail.com, rusty@rustybower.com',
      download_url='https://github.com/RustyBower/pythreatgrid/archive/1.0.tar.gz',
      url='https://github.com/RustyBower/pythreatgrid',
      packages=['pythreatgrid'],
      install_requires=['requests'],
      )
