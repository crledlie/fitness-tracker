from setuptools import setup
# Sets up requirement that it has to install flask first
setup(
    name='fitness_tracker',
    packages=['fitness_tracker'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
