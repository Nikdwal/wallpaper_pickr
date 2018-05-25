### wallpaper-pickr: A script that sets a random picture from Flickr as your desktop wallpaper
This Python package relies on the following libraries

- requests
- flickrapi

you have to edit the following lines to make it work:

1. The file ``token`` should contain your Flickr API token. The token is divided in two halves, an API key and a corresponding secret. The first line should be the key and the second line should be the secret
  - A Flickr API token can be requested [here](https://www.flickr.com/services/api/)
2. Enter the name of your window manager (e.g. mac, gnome, windows, ....) in the file winmgr.conf

then you can run ``wallpaper_pickr.py`` with Python


