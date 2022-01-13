import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libnamegen",
    version="3.1.1.post2",
    author="BBaoVanC",
    author_email="pypi@bbaovanc.com",
    description="Library containing name generation methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.bbaovanc.com/bbaovanc/libnamegen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'libprogress<4',
          'liblistloader<2',
    ],
    python_requires='>=3.7',
)
