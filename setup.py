import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="mamba",
    version="0.2.0",
    author="Jens Reidel",
    author_email="jens.reidel@gmail.com",
    description="A language built on top of python, with JS flavours",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gelbpunkt/mamba-lang",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": "mamba = mamba.__main__:main"},
    license="MIT",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
