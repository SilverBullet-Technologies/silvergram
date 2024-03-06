from setuptools import setup, find_packages

setup(
    name="silvergram",
    version="0.0.4",
    packages=find_packages(),
    description="A convenient shell for the Aiogram library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SilverBullet Technologies",
    author_email="tech.silver.bullet@gmail.com",
    url="https://github.com/SilverBullet-Technologies/silvergram",
    install_requires=[
        "aiogram>=3.4.1"
    ]
)
