#!/usr/bin/env python

from distutils.core import setup

setup(name='pythreatgrid',
	version='0.2',
	description='Python ThreatGrid API wrapper',
	author='Stephen Hosom, Rusty Bower',
	author_email='0xhosom@gmail.com, rusty@rustybower.com',
	url='https://github.com/rustybower/pythreatgrid',
	packages=['pythreatgrid'],
	install_requires=['requests'],
)
