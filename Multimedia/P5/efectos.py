from pydub import AudioSegment
from pydub.playback import play

# Load the audio file
audio = AudioSegment.from_file("output.mp3", format="mp3")
audio2 = AudioSegment.from_file("audio/Mozart_from_Piano_Sonata_K310_first_movement.wav", format="wav")

# Filtro
filtro = audio.low_pass_filter(40)
#play(filtro)

# Recorte
fragmento = audio[:1000] # primero 5 segundos
#play(fragmento)

union = audio + audio2
bucle = audio * 3
mezcla = audio.overlay(audio2, position=1000) # empieza en el segundo 1

#play(union)
#play(bucle)
#play(mezcla)

mas_alta = audio + 6       # +6 dB
mas_baja = audio - 4       # -4 dB
con_fade = audio2.fade_in(3000).fade_out(8000)

#play(mas_alta)
#play(mas_baja)
#play(con_fade)

duration = len(audio)  # in milliseconds
sample_rate = audio.frame_rate  # in Hz
channels = audio.channels  # 1 for mono, 2 for stereo

print(f"{duration}, {sample_rate}, {channels}")