import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SoSI_Crawler_Interfaces_IDataRepository", 
    version="0.0.1",
    author="SoSI",
    author_email="contato@sosi.com.br",
    description="Interface that represents the commom behaviors of a data repository class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonidasnascimento/SoSI.Crawler.Interfaces.IDataRepository",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)