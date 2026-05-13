from setuptools import setup, find_packages

setup(
    name="openclaw-tv-caster",
    version="1.3.0",
    description="SmartTV casting toolkit with DIAL/SSDP/mDNS discovery and display server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "tv-cast=src.protocols.ssdp:main",
            "cast-server=cast-display.server:main",
        ],
    },
    scripts=["cast-display/server.py"],
)
