# import config
import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError

# scope = 'playlist-modify-private'
scope = 'user-library-read playlist-read-private'
client_id = '647a2c2c53b04fe0bbc3aa790590aaef'
client_secret = '43123f12c81448d5ad0cdcb539908d22'
username = 'snda5g4bvdhp33loifwozbapa'
redirect_uri = 'http://localhost:4002/callback'

try:  # prompt user to give permission for the script to access data.
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:  # if permission has been granted by the user:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

