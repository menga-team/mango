import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mango",
    version="0.0.2",
    author="Nakano Miku",
    author_email="nakanomiku@menga.org",
    description="python api for https://www.digitalesregister.it/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/menga-team/mango",
    project_urls={
        "Bug Tracker": "https://github.com/menga-team/mango/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points='''
            [console_scripts]
            svg2eagle=mango.mango:cli
        ''',
)
