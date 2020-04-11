import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sosi_crawler_interfaces_datarepository", 
    version="0.0.2",
    author="SoSI",
    author_email="contato@sosi.com.br",
    description="Interface that represents the commom behaviors of a data repository class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonidasnascimento/sosi_crawler_interfaces_datarepository",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)