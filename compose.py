import config
import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError


#authenticates the user and calls functions to gather playlist information.
def authenticate(username, scope, client_id, client_secret, redirect_uri):
    try:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) #prompt user to give permission for the script to access data.
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token: #if permission has been granted by the user:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        user_input = gather_playlist_data()
        playlist_name, artist_id = user_input
        created_playlist = sp.user_playlist_create(username, playlist_name, public=False)

        similar_artists = get_similar_artists(artist_id, sp)
        for artist in similar_artists:
            add_to_playlist(artist, created_playlist['uri'], sp)
        print("Your playlist has been created!")
    else:
        print("Token didn't work!")


#gathers the playlist information from the user.
def gather_playlist_data():
    playlist_name = input("What would you like your playlist to be named? ")
    artist_id = input("Enter the ID of the artist you want to model the playlist on: ")
    result = (playlist_name, artist_id)
    return result

#creates list of similar artists and selects the first 4.
def get_similar_artists(artist_id, sp):
    similar_artists = sp.artist_related_artists(artist_id)
    uris = []
    artist_list = similar_artists['artists']

    #get the first 4 similar artists
    i = 0
    while i < 4:
        uris.append(artist_list[i]['uri'])
        i += 1

    return uris

def add_to_playlist(artist_id, playlist_uri, sp):
    #get the artist's top 10 songs:
    top_10 = sp.artist_top_tracks(artist_id)
    for song in top_10['tracks']:
        result = sp.user_playlist_add_tracks(username,playlist_uri,[song['uri']])


if __name__ == '__main__':
    client_id = config.client_id    #replace with your own client id
    client_secret = config.client_secret    #replace with your own client secret
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'playlist-modify-private'
    username = input("What is your Spotify username? ")
    authenticate(username, scope, client_id, client_secret, redirect_uri)