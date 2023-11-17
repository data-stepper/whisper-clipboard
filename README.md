# Whisper Clipboard

Welcome to the Whisper Transcribe repository. This is a simple Python
command line application that allows you to record audio and transcribe it using one of the
[Whisper ASR models by OpenAI](https://openai.com/research/whisper). It uses a terminal user interface, making it easy to use.

## Prerequisites
* Python 3.10 or higher (probably works with lower versions, but not tested)
* ffmpeg

## Installation from PyPI

```
pip install whisper-clipboard
```
And then run `transcribe` and start transcribing.
Please make sure you have `ffmpeg` installed properly on your system (this may vary between different operating systems).

## Installation using the repo

### For NixOS Users:

```bash
# Step 1: Clone the repository.
git clone https://github.com/data-stepper/whisper-clipboard

# Step 2: cd into the cloned repository.
cd whisper-clipboard

# Step 3: Run Nix-shell to set up the environment and install all necessary packages.
nix-shell

# Step 4: Run the Whisper Transcribe program.
python transcribe.py
```

### For Non-NixOS Users:

```bash
# Step 1: Clone the repository.
git clone https://github.com/data-stepper/whisper-clipboard

# Step 2: cd into the cloned repository.
cd whisper-clipboard

# Step 3: (Optional) Create a virtual environment and activate it.
python -m venv venv
source venv/bin/activate
# On Windows, activate the virtual environment with 'venv\Scripts\activate'

# Step 4: Install the required packages.
pip install -r requirements.txt

# Step 5: Run the Whisper Transcribe program.
python transcribe.py
```

## Usage

Start the program using
```bash
python transcribe.py
```

After starting the program, you will see a prompt ('>').

* Press 'Space' to start recording. While recording, the terminal will display "Recording..."
* Press 'Space' again to stop recording. The audio will be saved, and the transcription will be displayed in the terminal and copied to the clipboard.
* Press 'Q' to quit the application.

## Troubleshooting

Ensure that you have the required version of Python and FFMPEG installed. If you encounter any issues, feel free to create an issue on this repository.

Happy transcribing!
