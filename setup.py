from setuptools import setup, find_packages
import os

version = '0.4'

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='fnord.safename',
      version=version,
      description="A codec for safe filenames.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        ],
      keywords='codec safename',
      author='Bert Vanderbauwhede',
      author_email='batlock666@gmail.com',
      url='https://github.com/batlock666/fnord.safename',
      license='lgpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['fnord'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'fnord.easycodec',
      ],
      entry_points={
          "console_scripts": ["safename = fnord.safename.script:safename"],
      },
      )
