from setuptools import setup, find_packages

setup(
  name="audiomaker",
  version="0.1.0",
  packages=find_packages(),
  install_requires=[
    "edge-tts",
    "pydub",
    "tqdm"
  ],
  entry_points={
    "console_scripts": [
      "audiomaker=audiomaker.cli:main"
    ]
  },
  author="Ankush Rathour",
  description="Generate seamless long-form audio from massive text using chunking and merging.",
  python_requires=">=3.7",
)
