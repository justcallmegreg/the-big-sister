# the-big-sister

[![Build Status](https://travis-ci.org/ngergo/the-big-sister.svg?branch=master)](https://travis-ci.org/ngergo/the-big-sister)
[![Coverage Status](https://coveralls.io/repos/github/ngergo/the-big-sister/badge.svg?branch=master)](https://coveralls.io/github/ngergo/the-big-sister?branch=master)
[![Code Health](https://landscape.io/github/ngergo/the-big-sister/master/landscape.svg?style=flat)](https://landscape.io/github/ngergo/the-big-sister/master)
[![Stories in Ready](https://badge.waffle.io/ngergo/the-big-sister.svg?label=ready&title=Ready)](http://waffle.io/ngergo/the-big-sister)
[![Requirements Status](https://requires.io/github/ngergo/the-big-sister/requirements.svg?branch=master)](https://requires.io/github/ngergo/the-big-sister/requirements/?branch=master)

__the-big-sister__ is an extandeble Slackbot library written in Python to make the world a pleasent place for every each of us.
The Big Sister is easy to deploy and watches over us all in order to ensure compliancy won't be broken and all your employees 
start their days knowing their individual features and preferances are going to be respected througout the day
enabling them to deliver maximum producitivty in the organization!

## Installation

The package has not been deployed to `pip` yet.
You can install it by:

* cloning the repository/or downloading release tarball and run `pip install .`
* __OR__ run `pip install the-big-sister`

## Tests

__Writing tests is good!__ They protect you from doing things you don't want... It's not different at `the-big-sister`. Tests are written using `pytest` and run via `tox`.
`tox` also checks for style using `flake8` and does code coverage report using `coverage`.

* Run `tox` command in the root directory of the project to run all the tests. 
* You can specify which interpreters should be used by `tox -e [pyX.X]`
* Read more about [__tox__](https://testrun.org/tox/latest/)

PR's for testing new cases is always welcome!

### Contribute

* Fork the repository on GitHub.
* Write a test which shows that the bug was fixed or that the feature works as expected.

  - Use `tox` command to run all the tests in all locally available python version.
* Install `pre-commit` via `pip install pre-commit` then `pre-commit install`.
* Send a pull request and bug the maintainer until it gets merged and published. :).

For more instructions see `TESTING.rst`.

## MIT License

Copyright (c) 2016 Gergő Nagy

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
