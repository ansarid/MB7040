import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='mb7040',
    version='0.0.1',
    description='MB7040 Ultrasonic Sensor Library',
    packages=setuptools.find_packages(),
    install_requires=['smbus2',],
    keywords=['ultrasonic','MB7040','mb7040','maxbotix'],
    url='https://github.com/ansarid/MB7040',
    long_description=long_description,
    long_description_content_type='text/markdown'
)

