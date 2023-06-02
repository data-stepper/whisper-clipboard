#! /usr/bin/env python3

import warnings

warnings.filterwarnings("ignore")

import tempfile
from time import time

try:
    import pyperclip
except ImportError:
    raise ImportError(
        "pyperclip package not found. Please reinstall pyperclip to use this script."
    )

try:
    import sounddevice as sd
except ImportError:
    raise ImportError(
        "sounddevice package not found. Please reinstall sounddevice to use this script."
    )

try:
    import whisper
except ImportError:
    raise ImportError(
        "whisper package not found. Please reinstall whisper to use this script."
    )

import numpy as np
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


class Recorder:
    """Recorder class for audio recording."""

    def __init__(
        self,
        fs: int = 16_000,
        duration: int = 120,
        model_name: str = "base",
    ):
        """Initialize the Recorder object.

        Args:
            fs (int): The sample rate in kHz. Default is 16 kHz.
            duration (int): The maximum duration of the recording in seconds. Default is 120 seconds.
            model_name (str): The name of the model to load. Default is "base".
        """
        self.fs = fs
        self.duration = duration
        self.is_recording = False
        self.recording = None
        self.start_time = None

        try:
            self.model = whisper.load_model(model_name, in_memory=True)
        except Exception as e:
            error_message = (
                f"Failed to load whisper model '{model_name}'. Make sure the model is available and correctly configured. "
                f"Available models are 'tiny', 'base', 'small', 'large'"
            )
            print(error_message)
            raise type(e)(error_message).with_traceback(e.__traceback__)

    def start_recording(self):
        print("Recording ", end="")
        self.is_recording = True
        self.start_time = time()
        self.recording = sd.rec(
            int(self.fs * self.duration), samplerate=self.fs, channels=1
        )

    def stop_recording(self):
        self.is_recording = False
        sd.stop()
        elapsed_time = time() - self.start_time
        self.recording = self.recording[: int(elapsed_time * self.fs)]

        print(f"finished after {elapsed_time:.2f} seconds. ", end="")

        self.transcribe_audio()

    def transcribe_audio(self):
        try:
            r = self.model.transcribe(self.recording[:, 0], temperature=0.0)
            transcribed_text = str(r["text"]).rstrip().lstrip()

            print("Transcribed audio: ")
            print(80 * "=")
            print(transcribed_text)
            print(80 * "=")
            pyperclip.copy(transcribed_text)
        except Exception as e:
            print("Error during transcription:", str(e))

    def record_and_transcribe(self):
        # Create key bindings
        bindings = KeyBindings()

        @bindings.add("space")
        def _(_):
            if self.is_recording:
                self.stop_recording()
            else:
                self.start_recording()

        @bindings.add("q")
        def _(_):
            print("Exiting application.")
            raise KeyboardInterrupt

        # Create a session with the key bindings
        session = PromptSession(key_bindings=bindings)

        while True:
            try:
                _ = session.prompt("> ")

            except KeyboardInterrupt:
                break


def main():
    print("Welcome to whisper-transcribe! \n")
    print("Instructions:")
    print("Press 'Space' to start / stop recording.")
    print("Press 'Q', Ctrl+D or Ctrl+C to quit the application.")
    print("Transcriptions are automatically copied to clipboard.")
    print()

    recorder = Recorder()
    recorder.record_and_transcribe()


if __name__ == "__main__":
    main()
