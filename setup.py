from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_hospitalrun/__init__.py
from erp_hospitalrun import __version__ as version

setup(
	name="erp_hospitalrun",
	version=version,
	description="Hospital Management",
	author="Biswajit Sahoo",
	author_email="biswajit@buzztagmedia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
