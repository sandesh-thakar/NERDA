import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NERDA", 
    version="0.8.7",
    author="Lars Kjeldgaard, Lukas Christian Nielsen",
    author_email="lars.kjeldgaard@eb.dk",
    description="A Framework for Finetuning Transformers for Named-Entity Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandesh-thakar/NERDA",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'torch<=1.7.1',
        'transformers<=3.5.1',
        'sklearn',
        'nltk',
        'pandas',
        'progressbar',
        'pyconll'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'pytest-cov'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True
    )