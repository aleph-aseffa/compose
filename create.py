import config
import spotipy

# gathers the playlist information from the user.
def gather_playlist_data():
    playlist_name = input("What would you like your playlist to be named? ")
    artist_id = input("Enter the ID of the artist you want to model the playlist on: ")
    result = (playlist_name, artist_id)
    return result


# creates list of similar artists and selects the first 4.
def get_similar_artists(artist_id, sp):
    similar_artists = sp.artist_related_artists(artist_id)
    uris = []
    artist_list = similar_artists['artists']

    # get the first 4 similar artists
    i = 0
    while i < 4:
        uris.append(artist_list[i]['uri'])
        i += 1

    return uris


def add_to_playlist(artist_id, playlist_uri, sp):
    # get the artist's top 10 songs:
    top_10 = sp.artist_top_tracks(artist_id)
    for song in top_10['tracks']:
        sp.user_playlist_add_tracks(config.username,playlist_uri,[song['uri']])


def specific_artist(token):

    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    user_input = gather_playlist_data()
    playlist_name, artist_id = user_input
    created_playlist = sp.user_playlist_create(config.username, playlist_name, public=False)

    similar_artists = get_similar_artists(artist_id, sp)
    for artist in similar_artists:
        add_to_playlist(artist, created_playlist['uri'], sp)
    print("Your playlist has been created!")
