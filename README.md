# compose

## Description
Compose is a Spotify playlist creation tool. You can input an artist's ID and a 40-song playlist of songs by similar artists will be automatically generated.


## Usage
Clone the repository and extract the downloaded .zip folder. Navigate to the extracted folder and edit the config.py file. Update the file with your own client ID, client secret, and Spotify username.

Then, open the initialization.py file and run it.

![Prompt](https://i.imgur.com/oMMMbzp.png)

A webpage will automatically open in your default web browser. If you have not used this program before, it will ask you if you want to grant the program permissions to view and edit your library. Press accept if you accept the terms, and continue with the next steps of this document.

![Redirect](https://i.imgur.com/pDk4Vf8.png)

Copy this URL and paste it into the running program and press Enter. The program will then ask you what series of feature you want to run. Currently, only the create option (which you can start by entering 'c') has been implemented.

Enter 'c' and then enter 'a' (other features will be implemented soon but for now this is the only option).

![Create](https://i.imgur.com/YkR8ZJO.png)

Enter in what you want your playlist to be named (e.g. Test Run).
![Playlist name](https://i.imgur.com/6w5lS7o.png)

Then enter the ID of the artist you want to base the playlist on. You can find this by Googling the artist's name + Spotify and then copying the last section of the URL.

For example, for J. Cole, copy the highlighted section in the address bar:
![J. Cole](https://i.imgur.com/7c22TnC.png)

Paste this in the program and press enter. Wait a bit while the program searches for and adds songs to your playlist. You can open up Spotify to see the songs being added. 

The program will notify you when the playlist has been created.
![Complete](https://i.imgur.com/WxqWfH6.png)


Final results:
![Output](https://i.imgur.com/mk2ZH55.png)



## Author
Aleph Aseffa


## Roadmap
Features coming soon:
- Get rid of unwanted songs from your library.
- Organize your saved songs into playlists based on genre.
- Organize your saved songs into playlists based on song's information (e.g. danceability, tempo, acousticness, etc.)
- Recommend artists to listen to based on a list of songs you like.
