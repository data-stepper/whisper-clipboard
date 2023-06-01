#! /usr/bin/env python3
import tempfile
import warnings
from time import time

import pyperclip
import sounddevice as sd
import soundfile as sf
import whisper

warnings.filterwarnings("ignore")

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


class Recorder:
    def __init__(self, filename: str):
        self.filename = filename
        self.fs = 44100  # sample rate
        self.duration = 120  # in seconds
        self.is_recording = False
        self.recording = None
        self.start_time = None

        try:
            self.model = whisper.load_model("base", in_memory=True)

        except Exception as e:
            print("Failed to load whisper model.")
            raise e

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
        sf.write(self.filename, self.recording, self.fs)

        print(f"finished after {elapsed_time:.2f} seconds. ", end="")

        self.transcribe_audio()

    def transcribe_audio(self):
        try:
            print("Transcribing audio now...")
            r = self.model.transcribe(self.filename, temperature=0.0)
            transcribed_text = str(r["text"]).rstrip().lstrip()

            print("Transcribed: \n")
            print(80 * "=")
            print(transcribed_text)
            print(80 * "=")
            pyperclip.copy(transcribed_text)
        except Exception as e:
            print("Error during transcription:", str(e))

    def record_audio(self):
        # Create key bindings
        bindings = KeyBindings()

        @bindings.add("space")
        def _(_):
            if self.is_recording:
                self.stop_recording()
            else:
                self.start_recording()

        @bindings.add("q")
        def _(event):
            print("Exiting application.")
            raise KeyboardInterrupt

        # Create a session with the key bindings
        session = PromptSession(key_bindings=bindings)

        while True:
            try:
                _ = session.prompt("> ")

            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    print("Welcome to whisper-transcribe! \n")
    print("Instructions:")
    print("Press 'Space' to start / stop recording.")
    print("Press 'Q', Ctrl+D or Ctrl+C to quit the application.")
    print("Transcriptions are automatically copied to clipboard.")
    print()

    with tempfile.NamedTemporaryFile(suffix=".wav") as temp:
        recorder = Recorder(filename=temp.name)
        recorder.record_audio()
