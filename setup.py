from setuptools import setup

with open("README.md", "r") as fin:
    long_description = fin.read()

setup(
    name='jon-rocker',
    version='0.1.0',
    packages=['jon_rocker'],
    package_data={'jon_rocker': ['templates/*.em']},
    author='Jon Azpiazu',
    author_email='jon.azpiazu@gmail.com',
    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonazpiazu/jon-rocker",
    license='Apache 2.0',
    install_requires=[
        'rocker',
    ],
    entry_points={
        'rocker.extensions': [
            'ros_git_pkg = jon_rocker.ros_git_pkg:RosGitPkg',
            'opencl = jon_rocker.opencl:Opencl',
        ]
    }
)
