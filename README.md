# Whisper Transcribe

Welcome to the Whisper Transcribe repository. This is a simple Python application that allows you to record audio and transcribes it using the Whisper ASR model by OpenAI. It uses a terminal user interface, making it easy to use.

## Prerequisites
* Python 3.10 or higher (probably works with lower versions, but not tested)
* FFMPEG

## Installation

### For NixOS Users
1. Clone the repository:

```
git clone https://github.com/data-stepper/whisper-transcribe
```

2. cd into the cloned repository:

```
cd whisper-transcribe
```

3. Run Nix-shell:

```
nix-shell
```

This will set up the environment and install all necessary packages.

4. Run the Whisper Transcribe program:

```
python transcribe.py
```

### For Non-NixOS Users
1. Clone the repository:

```
git clone https://github.com/data-stepper/whisper-transcribe
```

2. cd into the cloned repository:

```
cd whisper-transcribe
```

3. (Optional) Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

On Windows, activate the virtual environment with `venv\Scripts\activate`

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Run the Whisper Transcribe program:

```
python transcribe.py
```

## Usage

After starting the program, you will see a prompt ('>').

* Press 'Space' to start recording. While recording, the terminal will display "Recording..."
* Press 'Space' again to stop recording. The audio will be saved, and the transcription will be displayed in the terminal and copied to the clipboard.
* Press 'Q' to quit the application.

## Troubleshooting

Ensure that you have the required version of Python and FFMPEG installed. If you encounter any issues, feel free to create an issue on this repository.

Happy transcribing!
