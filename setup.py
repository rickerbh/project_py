try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Hamish Rickerby',
    'url': 'https://github.com/rickerbh/project_py',
    'author_email': 'hamish@simplemachines.com.au',
    'version': '0.1',
    'install_requires': ['nose', 'nosy'],
    'packages': ['MY_PROJECT'],
    'scripts': [],
    'name': 'MY_PROJECT',
    'test_suite': 'nose.collector'
}

setup(**config)
