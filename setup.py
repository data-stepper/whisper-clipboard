from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="whisper-clipboard",
    version="0.1.1",
    description="A basic TUI for transcribing audio to your clipboard using OpenAI's whisper models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bent Mueller",
    author_email="bentmuller.ai@gmail.com",
    url="http://github.com/data-stepper/whisper-clipboard",
    py_modules=["transcribe"],
    entry_points={
        "console_scripts": [
            "transcribe = transcribe:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
