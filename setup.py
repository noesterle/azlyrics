# -*- coding: utf-8 -*-
from setuptools import setup, Command
import sys
import os
from shutil import rmtree

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

here = os.path.abspath(os.path.dirname(__file__))

class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()

setup(
  name = 'azlyrics',
  packages = ['azlyrics'],
  version = '1.3.4',
  description = 'An API wrapper for azlyrics which allows you to programatically extract data',
  long_description=long_descr,
  author = 'Nathan Oesterle',
  author_email = 'noesterle1@gmail.com',
  url = 'https://github.com/noesterle/azlyrics',
  download_url = '',
  keywords = ['azlyrics', 'lyrics', 'albums', 'artists', 'songs', 'music', 'api'],
  install_requires=['requests', 'beautifulsoup4'],
  classifiers = [],
  cmdclass={
          'publish': PublishCommand,
      }
)