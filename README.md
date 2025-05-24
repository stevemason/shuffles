SHUFFLES
========

After being frustrated by Spotify's shuffle play feature that kept playing the same tracks each time, this tool was created to properly conduct a random shuffle of a given Spotify playlist. The approach taken is based on the Fisher-Yates shuffle algorithm.

Oauth 2.0 is used to obtain access to a user's playlists. Once authorised, the Spotify ID of the playlist to be shuffled may then be passed as a commandline argument.

The method used to shuffle the playlist retains track-related metadata such as the date added, and the user who added the item to the playlist. The longer the playlist, the longer the time needed to shuffle, as tracks are shuffled by calling the Spotify API one track at a time.

Usage:

Step 1: Create a new app at <https://developer.spotify.com>. For the "Redirect URI", just make something up - it's not important. Take note of the "Client ID", "Client Secret" and "Redirect URI" values.

Step 2: Create ```config.py``` (as per the example provided) and populate it with the relevant settings.

Step 3: Run the following command: ```python shuffles.py --auth```

Step 4: Paste the resulting output into a web browser, log in with the relevant Spotify credentials - the browser will try to redirect to a non-existent page. This is fine, you just need to copy the Authorisation Code from the "code=" section in the browser's URL bar.

Step 5: Run the following command: ```python shuffles.py --code *paste code from previous step here*```

Step 6: You should now be good to go. Just run the following command to shuffle a playlist of your choice: ```python shuffles.py --playlist *playlist ID*```

If you don't know the playlist ID, this may be obtained from Spotify by sharing the playlist and "copying the link". This link contains the playlist ID.

Please do be mindful that the ```config.py```, ```access_token``` and ```refresh_token``` files contain sensitive data which should be secured appropriately.

UPDATE: As I am no longer a Spotify user, I have archived this repo.
