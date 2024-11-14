# setup.py
from distutils.core import setup
import py2exe

setup(
    console=['main.py'],
    py_modules=['application', 'database_manager']
)
