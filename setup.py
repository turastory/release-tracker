from setuptools import setup, find_packages

setup(
    name="release-tracker",
    version="1.0.0",
    description="Simple utility for tracking changes between releases.",
    author="turastory",
    author_email="soldier4443@gmail.com",
    license="MIT",
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
