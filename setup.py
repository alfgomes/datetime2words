from setuptools import setup, find_packages

setup(
    name='datetime2words',
    version='0.1.0',
    description='Converts datetime to words in multiple languages.',
    author='André Gomes',
    url='https://github.com/seuusuario/datetime2words',
    packages=find_packages(),
    install_requires=['num2words'],
    python_requires='>=3.8'
)