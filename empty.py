from pydub import AudioSegment

# создаём 20 секунд тишины
silence = AudioSegment.silent(duration=20000)  # в миллисекундах

# экспорт в mp3
silence.export("silent_20s.mp3", format="mp3")
