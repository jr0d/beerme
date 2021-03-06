from setuptools import setup, find_packages

from beerme import get_version


def read_file(path):
    with open(path) as fp:
        return fp.read().strip()


setup(name='beerme',
      version=get_version(),
      description="Untapped beer list scraper for Big Hops San Antonio",
      long_description=read_file('README.md'),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='BigHops,beer',
      author='Jared Rodriguez',
      author_email='jared@blacknode.net',
      url='https://github.com/jr0d/beerme',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "beautifulsoup4",
          "requests"
      ],
      entry_points={
        'console_scripts': [
            'beerme=beerme.beerme:main'
        ]
      },
      requires_python='>=3.5',
)
