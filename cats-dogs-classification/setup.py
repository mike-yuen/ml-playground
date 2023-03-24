from setuptools import setup, find_packages

setup(
    name="cats_dogs_classification",
    version="0.1",
    author="Mikey",
    author_email="nhatminh.150596@gmail.com",
    description="A machine learning project that classifies images of cats and dogs using neural networks",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "numpy==1.19.5",
        "pandas==1.2.3",
        "matplotlib==3.3.4",
        "scikit-learn==0.24.1",
        "keras==2.4.3",
        "tensorflow==2.4.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
