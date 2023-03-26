
import os
from pydub import AudioSegment

def mp3_to_wav(input_file, output_file):
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format="wav")
