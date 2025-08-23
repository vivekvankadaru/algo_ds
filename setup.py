from setuptools import setup, find_packages

setup(
    name="algo_ds",
    version="0.1.0",
    description="Algorithms and Data Structures in Python",
    author="Vivek Vankadaru",
    packages=find_packages(),
    
    install_requires=[
        # Add your dependencies here, e.g. "numpy>=1.21.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)