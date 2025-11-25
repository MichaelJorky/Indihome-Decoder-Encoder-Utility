"""Setup.py Module Installer with auto-download for decoder & encoder"""

import os
import urllib.request
from setuptools import setup, find_packages

# -----------------------------
# Config: URLs & Destination
# -----------------------------
FILES_TO_DOWNLOAD = {
    "decoder.py": "https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility/releases/download/v2.0.0-stable/decoder.py",
    "encoder.py": "https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility/releases/download/v2.0.0-beta/encoder.py"
}

# Default install folder
DEST_FOLDER = os.path.expanduser("~/.indihome-utility")
os.makedirs(DEST_FOLDER, exist_ok=True)

# -----------------------------
# Download files if not exist
# -----------------------------
for filename, url in FILES_TO_DOWNLOAD.items():
    dest_file = os.path.join(DEST_FOLDER, filename)
    if not os.path.exists(dest_file):
        print(f"Downloading {filename} from Releases...")
        try:
            urllib.request.urlretrieve(url, dest_file)
            print(f"{filename} downloaded successfully to {dest_file}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"{filename} already exists, skipping download.")

# -----------------------------
# Read metadata
# -----------------------------
with open('README.md', encoding='utf-8') as f:
    readme = f.read()
with open('LICENSE', encoding='utf-8') as f:
    LICENSE_TEXT = f.read()
with open('requirements.txt', encoding='utf-8') as f:
    REQUIRED = [line.strip() for line in f if line.strip()]

# -----------------------------
# Setup package
# -----------------------------
setup(
    name='zcu',
    description='Indihome ZTE Decoder Encoder Utility',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='TeknoXpert',
    author_email='wgalxczk3@mozmail.com',
    url='https://github.com/MichaelJorky/Indihome-Decoder-Encoder-Utility',
    license=LICENSE_TEXT,
    install_requires=REQUIRED,
    packages=find_packages(exclude=('ftp', 'telnet', 'ext', 'portscan')),
    include_package_data=True,
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities :: Networking"
    ]
)

