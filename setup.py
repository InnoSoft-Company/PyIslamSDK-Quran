from setuptools import setup, find_packages

__version__ = "0.1.0"

setup(
    name="islam-sdk-quran",
    version=__version__,
    author="InnoSoft Company",
    author_email="midoghanam@hotmail.com",
    description="IslamSDK Quran module with Quranic texts, utilities, and local database.",
    entry_points={"console_scripts": ["pyislamsdk_quran=pyislamsdk_quran.cli:main", ],},
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/InnoSoft-Company/IslamSDK-Quran",
    license="MIT",
    project_urls={
        "Source Code": "https://github.com/InnoSoft-Company/PyIslamSDK-Quran",
        "Bug Tracker": "https://github.com/InnoSoft-Company/PyIslamSDK-Quran/issues",
        "Documentation": "https://github.com/InnoSoft-Company/PyIslamSDK-Quran#readme",
    },
    packages=find_packages(),
    package_data={"pyislamsdk_quran": ["dbs/*.db", "data/*.json"]},
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries",
        "Typing :: Typed",
    ],
    keywords=[
        "islam", "quran", "adhan", "dua", "sdk", "religion", "prayer", "dhikr"
    ],
)