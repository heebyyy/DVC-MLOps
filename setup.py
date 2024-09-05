from setuptools import setup


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Bolaji",
    description="A small package for dvc ml pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heebyyy/DVC-MLOps",
    author_email="olayemibolaji1@gmail.com",
    packages=["src"],
    python_requires=">=3.12",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)