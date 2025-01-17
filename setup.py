import os

from setuptools import setup

# import groupme_bot


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='groupme-bot',
    version="2.3.1",
    description='A simple bot builder for GroupMe',
    url='https://github.com/stryker51a/groupme-bot-library',
    author="Branden Colen",
    author_email='brandencolen@gmail.com',
    license='MIT',
    packages=['groupme_bot'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=[
        'anyio~=3.6.2',
        'apscheduler~=3.10.1',
        'certifi~=2022.12.7',
        'charset-normalizer~=3.1.0',
        'click~=8.1.3',
        'colorama~=0.4.6',
        'h11~=0.14.0',
        'idna~=3.4',
        'pytz~=2023.3',
        'pytz-deprecation-shim~=0.1.0.post0',
        'requests~=2.29.0',
        'six~=1.16.0',
        'sniffio~=1.3.0',
        'starlette~=0.26.1',
        'tzdata~=2023.3',
        'tzlocal~=4.3',
        'urllib3~=1.26.15',
        'uvicorn~=0.22.0'
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
