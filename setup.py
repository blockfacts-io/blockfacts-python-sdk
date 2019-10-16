from setuptools import setup, find_packages

NAME = "blockfacts-sdk"
VERSION = "1.0.0"
REQUIRES = ['requests','websocket-client']

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(
    name=NAME,
    version=VERSION,
    description="Official BlockFacts Python SDK including Rest and WebSocket API support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = "BlockFacts Ltd.",
    author_email="marko@blockfacts.io",
    url="https://github.com/blockfacts-io/blockfacts-python-sdk",
    keywords=["BlockFacts", "BlockFacts API", "Crypto API", "Crypto Assets API", "Unified Cryptocurrency API", "BlockFacts SDK", "BlockFacts Python", "Blockchain API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4'
)