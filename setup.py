from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Anymarket API'
LONG_DESCRIPTION = 'Anymarket´s API to solve a lot of implementations in your project!'

# Setting up
setup(
    name="Anymarket",
    version=VERSION,
    author="Pablo Belmiro",
    author_email="dev.pablobelmiro@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['httpx'],
    keywords=['python', 'API', 'Anymarket', 'Ecommerce'],
)