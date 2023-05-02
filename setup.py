import os

from setuptools import setup

import groupme_bot

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='groupme-bot',
    version=groupme_bot.__version__,
    description='A simple bot builder for GroupMe',
    url='https://github.com/stryker51a/groupme-bot-library',
    author=groupme_bot.__author__,
    author_email='brandencolen@gmail.com',
    license='MIT',
    packages=['groupme_bot'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=[
        'anyio==3.6.2'
        'APScheduler~=3.10.1',
        'httpx~=0.16.1',
        'starlette~=0.26.1',
        'uvicorn~=0.22.0',
        'requests~=2.29.0'
    ],
    python_requires='>=3.6',  # for use of f strings
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
