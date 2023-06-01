from setuptools import setup

setup(
    name="whisper-clipboard",
    version="0.1.0",
    description="A basic TUI for transcribing audio to your clipboard using OpenAI's whisper models.",
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
