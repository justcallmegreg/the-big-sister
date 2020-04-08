from setuptools import setup, find_packages
from os import path
try: # for pip >= 10
  from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
  from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))

version_file = open(path.join(here, 'VERSION'))

PROJECT_URL = 'http://github.com/ngergo/the-big-sister'
VERSION = version_file.read().strip()

DESCRIPTION = """
TODO
"""

install_reqs = parse_requirements(
    path.join(here, 'requirements.txt'),
    session=False
)
install_requirements = [str(ir.req) for ir in install_reqs]

dev_reqs = parse_requirements(
    path.join(here, 'requirements.txt'),
    session=False
)
development_requirements = [str(ir.req) for ir in dev_reqs]

setup(
    name='ratatoskr',
    version=VERSION,
    description=DESCRIPTION,
    url=PROJECT_URL,
    download_url=PROJECT_URL + '/tarball/v' + VERSION,
    author='Gergo Nagy',
    author_email='contact@gergonagy.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],
    keywords='TODO',
    packages=find_packages(),
    install_requires=install_requirements,
    extras_require={
        'dev': development_requirements
    },
)
