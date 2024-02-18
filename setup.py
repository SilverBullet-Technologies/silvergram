from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="silvergram",
    version="0.0.1",
    packages=find_packages(),
    description="A convenient shell for the aiogram library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SilverBullet Technologies",
    author_email="tech.silver.bullet@gmail.com",
    url="https://github.com/yourusername/mathlib",
    install_requires=install_requires
)

