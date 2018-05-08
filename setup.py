#!/usr/bin/env python

from distutils.core import setup

setup(name='pythreatgrid',
	version='0.2',
	description='Python ThreatGrid API wrapper',
	author='Stephen Hosom, Rusty Bower',
	author_email='0xhosom@gmail.com, rusty@rustybower.com',
	download_url='https://github.com/RustyBower/pythreatgrid/archive/0.2.tar.gz',
	url='https://github.com/RustyBower/pythreatgrid',
	packages=['pythreatgrid'],
	install_requires=['requests'],
)
