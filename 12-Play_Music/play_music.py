import winsound
MUSIC_FILE = 'music.wav'
play_music = lambda: winsound.PlaySound(MUSIC_FILE, winsound.SND_FILENAME)
play_music()