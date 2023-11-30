from refresh import Refresh
import requests
import json

class Spotify:
    def __init__(self):
        self.spotify_token = ""
        self.current_song = []
        self.previous_song = []
    
    def call_refresh(self):
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()
    
    def fetch_current_playing_song(self):
        while True:
                    
            fetch_playing_song = requests.get("https://api.spotify.com/v1/me/player/currently-playing?market=nl", headers={"Authorization": f"Bearer {self.spotify_token}"})

            fetch_playing_song_json = fetch_playing_song.json()
            
            song_title = json.dumps(fetch_playing_song_json['item']['name'])

            list_of_artists = fetch_playing_song_json['item']['artists']
            
            count = -1
            artist_list = ''
            for i in list_of_artists:
                count += 1
                artists_json = json.dumps(fetch_playing_song_json['item']['artists'][count]['name'])
                artist = json.loads(artists_json)
                artist_list += f"{artist}, "
            
            self.current_song = json.loads(song_title)
            
            if self.previous_song != self.current_song:
                print(f"Now Playing: {self.current_song} - {artist_list[:-2]}")
            self.previous_song = self.current_song

s = Spotify()
s.call_refresh()

s.fetch_current_playing_song()