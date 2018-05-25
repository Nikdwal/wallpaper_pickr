### wallpaper-pickr: A script that sets a random picture from Flickr as your desktop wallpaper
This Python package relies on the following libraries

- requests
- flickrapi

you have to edit the following lines to make it work:

0. The file ``token`` should contain your Flickr API token. The token is divided in two halves. The first line should be the first half and the second line should be the second half
0. Set the implementation of ``set_wallpaper`` in ``set_as_wallpaper.py`` to the function corresponding to your window manager (e.g. mac, gnome, windows, ...)

then you can run ``wallpaper_pickr.py``

