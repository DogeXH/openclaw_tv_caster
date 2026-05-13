from setuptools import setup, find_packages

setup(
    name="openclaw-tv-caster",
    version="1.2.0",
    description="SmartTV casting toolkit with DIAL/SSDP/mDNS discovery",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "tv-cast=src.protocols.ssdp:main",
        ],
    },
)
