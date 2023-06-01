import sys
import termios
import time
import tty

import sounddevice as sd
import soundfile as sf
import pyperclip

import whisper

model = whisper.load_model("base", in_memory=True)
print("Model loaded.")


def print_user_info(text: str) -> None:
    print(text, end="\r", flush=True)


def record_audio(filename: str) -> None:
    duration = 60  # in seconds
    fs = 44100  # sample rate

    print_user_info(
        "Recording audio. Press 'Space' to start / stop recording or 'q' to quit..."
    )
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == " ":
                print_user_info("Recording...")
                start_time = time.time()
                recording = sd.rec(
                    int(duration * fs), samplerate=fs, channels=1
                )

                progress_indicator = "|/-\\"
                progress_index = 0

                while True:
                    ch = sys.stdin.read(1)
                    if ch == " ":
                        sd.stop()
                        end_time = time.time()
                        elapsed_time = end_time - start_time

                        # Cut off any trailing zeros
                        recording = recording[: int(elapsed_time * fs)]

                        sf.write(filename, recording, fs)

                        print_user_info(f"\nAudio saved as {filename}.")
                        print_user_info(
                            f"Recording duration: {elapsed_time:.2f} seconds."
                        )

                        # And then transcribe the audio using whisper
                        try:
                            print_user_info("Transcribing audio...")
                            r = model.transcribe(filename, temperature=0.0)
                            transcribed_text = r["text"]
                            print_user_info("Transcribed: \n\n")
                            print_user_info(80 * "-")
                            print_user_info(transcribed_text)
                            print_user_info(80 * "-")
                            pyperclip.copy(transcribed_text)
                        except Exception as e:
                            print_user_info(
                                "Error during transcription:", str(e)
                            )

                        break

                    # Display progress indicator
                    sys.stdout.write(
                        f"\rRecording... {progress_indicator[progress_index % 4]}"
                    )
                    sys.stdout.flush()
                    progress_index += 1

            if ch in {"q", "Q", "c"}:
                raise KeyboardInterrupt

            if ch != "\n":
                print_user_info(
                    "Invalid input. Press 'Space' to start / stop recording or 'q' to quit..."
                )

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    try:
        # Get a tempfile path
        import tempfile

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as f:
            record_audio(f.name)

    except KeyboardInterrupt:
        print_user_info("\nInterrupted by user.")
        sys.exit(0)
