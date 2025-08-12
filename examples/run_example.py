from audiomaker import text_to_audio

if __name__ == "__main__":
  with open("example.txt", "r", encoding="utf-8") as f:
    text = f.read()

  text_to_audio(
    text=text,
    output_path="output.mp3",
    chunk_size=3000,
    voice="en-US-AriaNeural",
    temp_dir="audio_parts"
  )
