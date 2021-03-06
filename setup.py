# -*- coding: utf-8 -*-

import os
from distutils.core import setup
from yandexmaps_widget import __version__

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ymaps-admin-widget',
    version=__version__,
    packages=['yandexmaps_widget'],
    package_data={'yandexmaps_widget': ["templates/yandexmaps_widget/*", "static/js/*"]},
    url='https://github.com/DrMartiner/django-ymaps-admin-widget',
    license='MIT',
    author='Alexey Kuzmin',
    author_email='DrMartiner@GMail.Com',
    description='Widget admin for Yandex Maps',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)