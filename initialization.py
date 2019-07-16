"""
Basically a file that prints out the options for the user and does the general setup.

Ideas on features to add:
- Go through your saved songs and remove songs that you don't like.
"""

import config
import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError
import create


def authenticate():
    try:  # prompt user to give permission for the script to access data.
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:  # if permission has been granted by the user:
    #    sp = spotipy.Spotify(auth=token)
     #   sp.trace = False
        return token
    else:
        print("Authentication failed.")
        return False


def print_menu(token) -> None:
    print("Welcome to Compose, a Spotify playlist creation and management tool.")
    user_menu_selection = input("Would you like to create (enter c), organize (enter o), or clean? (enter r) ")
    if user_menu_selection == 'c':
        create_options(token)
        pass
    elif user_menu_selection == 'o':
        organize_options()
        pass
    else:
        clean_options()
        pass


def create_options(token) -> None:
    print()
    print("Your options include creating a playlist based on:")
    print("- a specific artist...(enter a)")
    print("- your most listened to artists...(enter m)")
    print()
    user_create_selection = input("Enter your choice: ")
    if user_create_selection == 'a':
        create.specific_artist(token)
        pass
    else:
        # favourite_artists_create()
        pass


def organize_options() -> None:
    print()
    print("Your options include organizing your playlist based on:")
    print("- genre...(enter g)")
    print("More options coming soon!")
    # as organizing by genre is the only option at the moment, no user input is taken
    # organize_by_genre()


def clean_options() -> None:
    print()
    print("Compose will now begin going through your saved songs and asking you if you want to keep or remove them.")
    print("At any point, type q to quit.")
    # clean_library()


if __name__ == '__main__':

    scope = 'playlist-modify-private'
    client_id = config.client_id
    client_secret = config.client_secret
    username = config.username
    redirect_uri = 'http://localhost:8888/callback'

    valid_token = authenticate()
    if valid_token:
        print_menu(valid_token)
    else:
        print("Authentication failed. Please run the program again.")
