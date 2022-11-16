from setuptools import find_packages, setup


with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="heart",
    packages=find_packages(),
    version="0.1.0",
    description="MLOps Homework #1",
    author="Viliars (Michael Pritugin)",
    entry_points={
        "console_scripts": [
            "train = heart.models.train:main",
            "predict = heart.models.predict:main",
            "download_dataset = heart.data.download_dataset:main",
        ]
    },
    install_requires=required,
)
