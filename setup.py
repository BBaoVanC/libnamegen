import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libnamegen",
    version="3.0.2",
    author="BBaoVanC",
    author_email="bbaovanc@protonmail.com",
    description="Library containing name generation methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BBaoVanC/libnamegen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)