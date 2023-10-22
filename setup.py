import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description f.read()

___version___ = "0.0.0"

REPO_NAME = "Kidney_Disease_Classification"
AUTHOR_USER_NAME = "riyadharshh"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "priyadharshinikaruna15@gmail.com"
setuptools.setup(
    name=SRC_REPO,
    version=__version___,
    author-AUTHOR_USER_NAME,
    author_email-AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url-f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    project urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issuses"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")