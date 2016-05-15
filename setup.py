try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Finds out the average colour of an image',
    'author': 'Robbie R',
    'url': '...',
    'download_url': '...',
    'author_email': 'robbie@roygbiv.co.uk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'colouraverage'
}

setup(**config)
