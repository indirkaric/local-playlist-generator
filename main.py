import shutil, os
import random
from datetime import date

MP3 = "mp3"
DOUBLE_SLASH = "\\"
candidate_tracks = []
final_playlist = []      

def validate_path(path):
    if not os.path.exists(path):
        raise Exception("Path does not exists")

def select_random_tracks(path):
    bands = os.listdir(path)

    for band in bands:

        band_full_path = path + DOUBLE_SLASH + band
        albums = os.listdir(band_full_path)

        for album in albums:

            if (len(candidate_tracks) != 0):
                final_playlist.append(random.choice(candidate_tracks))
                candidate_tracks.clear()

            album_full_path = band_full_path + DOUBLE_SLASH + album
            tracks = os.listdir(album_full_path)

            for track in tracks:
                
                if MP3 in track:
                    track_full_path = album_full_path + DOUBLE_SLASH + track
                    candidate_tracks.append(track_full_path)

def generate_playlist_dir(path):
    playlist_name = "My-Playlist-" + str(date.today())
    playlist_dir = path + DOUBLE_SLASH + playlist_name
    os.mkdir(playlist_dir)

    for track in final_playlist:
        shutil.copy(track, playlist_dir)

    print("Number of tracks in playlist:" + str(len(final_playlist)))

dir_path = input("Enter music collection path:")
playlist_path = input("Enter location for your playlist:")
validate_path(dir_path)
validate_path(playlist_path)
select_random_tracks(dir_path)
generate_playlist_dir(playlist_path)
