#!/usr/bin/env python
import ast
import re
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('django_google_maps/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='django-google-maps',
    version=version,
    author='Aaron Madison',
    author_email='aaron.l.madison@gmail.com',
    description='Plugs google maps V3 api into Django admin.',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/madisona/django-google-maps',
    packages=['django_google_maps'],
    include_package_data=True,
    install_requires=open('requirements.txt').read().split('\n'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
    platforms='any',
)
