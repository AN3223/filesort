from setuptools import setup, find_packages

setup(
    name='filesort',
    version='0.1.1',
    description='A simple command line tool for sorting files',
    url='https://github.com/AN3223/filesort',
    author='AN3223',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['build', 'doc', 'dist', 'contrib', 'docs']),
    entry_points={
        'console_scripts': [
            'filesort = filesort.filesort:main'
        ]
    }
)
