import os
from mutagen.mp3 import MP3
from mutagen.wave import WAVE


def calculate_music_duration_and_count(folder_path):
    total_duration = 0  # in seconds
    total_songs = 0  # to count the number of songs

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if file.endswith(".mp3"):
                    audio = MP3(file_path)
                    total_duration += audio.info.length
                    total_songs += 1
                elif file.endswith(".wav"):
                    audio = WAVE(file_path)
                    total_duration += audio.info.length
                    total_songs += 1
            except Exception as e:
                print(f"Could not process file {file}: {e}")

    total_hours = total_duration / 3600
    print(f"Total music duration: {total_hours:.2f} hours")
    print(f"Total number of songs downloaded: {total_songs}")


# Provide the path to your folder
folder_path = r"C:\Users\pc1\Downloads\Musics"
calculate_music_duration_and_count(folder_path)
