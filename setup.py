import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="DeliberativePolling_v2",
    version="1.4.2",
    author="The Deliberative Democracy Lab at Stanford University",
    author_email="deliberation@stanford.edu",
    packages=["DeliberativePolling_v2"],
    description="A package for analyzing survey data from Deliberative Polling experiments.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/stanford-ddl/DeliberativePolling",
    license="MIT",
    python_requires=">=3.11",
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl",
        "pyreadstat",
        "statsmodels",
        "scipy",
        "docx",
        "tqdm",
        "python-docx",
    ],
)
