from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "telegrambot",
    version = "0.0.1",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    url = "https://github.com/RomainGratier/telegrambot",
    description = ("send telegram notification using a bot"),
    license = "MIT",
    keywords = "python telegram",
    py_modules=["telegrambot"],
    package_dir={"": "telegrambot"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires = [
        "requests>=2.25.0",
    ],
)

