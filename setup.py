"""Setup.py Module Installer with auto-download for decoder & encoder"""
import os
import urllib.request
from setuptools import setup, find_packages

# Paths & URLs
FILES_TO_DOWNLOAD = {
    "decoder.py": "https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility/releases/download/v2.0.0-stable/decoder.py",
    "encoder.py": "https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility/releases/download/v2.0.0-stable/encoder.py"
}
DEST_FOLDER = os.path.expanduser("~/.zte-decoder")
os.makedirs(DEST_FOLDER, exist_ok=True)

# Download files if they don't exist
for filename, url in FILES_TO_DOWNLOAD.items():
    dest_file = os.path.join(DEST_FOLDER, filename)
    if not os.path.exists(dest_file):
        print(f"Downloading {filename} ...")
        urllib.request.urlretrieve(url, dest_file)
    else:
        print(f"{filename} already exists, skipping download.")

# Read metadata
with open('README.md', encoding='utf-8') as f:
    readme = f.read()
with open('LICENSE', encoding='utf-8') as f:
    LICENSE_TEXT = f.read()
with open('requirements.txt', encoding='utf-8') as f:
    REQUIRED = [line.strip() for line in f if line.strip()]

# Setup
setup(
    name='zcu',
    description='Indihome ZTE Decoder Encoder',
    long_description=readme,
    author='Dunia MR',
    author_email='wgalxczk3@mozmail.com',
    url='https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility',
    license=LICENSE_TEXT,
    install_requires=REQUIRED,
    packages=find_packages(exclude=('ftp', 'telnet', 'ext', 'portscan')),
    include_package_data=True
)
