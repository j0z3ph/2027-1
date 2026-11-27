from pydub import AudioSegment

audio = AudioSegment.from_file("audio/pcm3244s.wav", format="wav")
audio.export("output.mp3", format="mp3")