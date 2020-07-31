from setuptools import setup, find_packages

# Required to include this when making a package public

setup(
    name='Eskom_7functions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Personal version predict 2 package deliverable',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/jaccars/An_sprint_own',
    author='Jacques Carstens',
    author_email='carstensjacques3@gmail.com'
)