{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python310.withPackages (ps:
    with ps; [
      openai-whisper
      sounddevice
      soundfile
      keyboard
      pyperclip
      black
    ]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv pkgs.ffmpeg ];
  shellHook = ''
    echo "Using python executable: $(which python)"
    zsh
  '';
}
