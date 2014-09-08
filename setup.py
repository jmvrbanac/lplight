from setuptools import setup, find_packages

setup(
    name='lplight',
    version='0.0.3',
    description=('Simple Launchpad client for retrieving project information '
                 'and bugs'),
    long_description=('A simple read-only (currently) launchpad client '
                      'library to access bugs and projects via the available '
                      'REST api. This project has no affiliation with '
                      'Launchpad or Canonical Ltd.'),
    url='https://github.com/jmvrbanac/lplight',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='launchpad lightweight client',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['requests', 'six'],
    test_requires=['specter>=0.1.15'],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
