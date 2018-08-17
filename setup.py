#!/usr/bin/env python3
from os.path import join, basename, abspath, dirname
from setuptools import setup

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

setup(
    name='mycroft-tts-plugin-gtts',
    version='0.2',
    description='A tts plugin for mycroft',
    url='http://github.com/MycroftAI/mycroft-tts-plugin-gtts',
    author='Åke Forslund',
    author_email='ake.forslund@gmail.ocm',
    license='Apache-2.0',
    packages=['mycroft_tts_plugin_gtts'],
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin tts',
)
