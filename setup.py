from setuptools import setup, find_packages


setup(
    name='mean',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-flake8',
    ]
)
