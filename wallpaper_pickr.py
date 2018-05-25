import flickrapi
import random
from time import time
import os
from requests.exceptions import ConnectionError
import requests as req
import shutil
from set_as_wallpaper import set_wallpaper

curr_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(curr_directory)

# get the Flick API token
try:
    with open(os.path.join(curr_directory, "token")) as f:
        token = [line.replace("\n","") for line in f]
except FileNotFoundError:
    print("Please a enter a valid token in the file 'token'")
    exit(1)

try:
    found_an_image = False
    f = flickrapi.FlickrAPI(token[0], token[1])

    while not found_an_image:
        # feel free to customise this bit
        if random.random() < 0.8:
            # pick from a pre-set wallpaper user group
            groups = ["40961104@N00","548678@N23","893835@N20","2535978@N21" ]
            rsp = f.photos.search(group_id=random.choice(groups), sort="interestingness-desc", media="photos", per_page=150)
        else:
            # pick from a set of tags. Each tag has a top-N associated with it. This program will pick from the top N.
            tags = [("nature",35), ("landscape",25), ("mountain",150), ("rocks",200), ("hiking", 150), ("sunlight", 15)]
            tag, top_requested_entries = random.choice(tags)
            used_tags = "wallpaper, " + tag

            rsp = f.photos.search(tags=used_tags, tag_mode="all", sort="interestingness-desc", media="photos", per_page=top_requested_entries)

        photo_ids = [child.get("id") for child in rsp.getchildren()[0].getchildren()]
        the_chosen_one = random.choice(photo_ids)
        sz = f.photos.getSizes(photo_id=the_chosen_one).getchildren()[0].getchildren()

        # the largest size should be the last in the list
        sz = sz[-1]
        # only accept images that are large enough
        found_an_image = int(sz.get("width")) > int(sz.get("height")) and int(sz.get("width")) >= 1000

    url = sz.get("source")

    # download the chosen image
    r = req.get(url, stream=True)
    filename = os.path.join(curr_directory, "wallpaper")
    with open(filename, "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 

    set_wallpaper(str(filename))

    # update the last_change time
    with open("lastchange", "w") as f:
        f.write(str(time()))

except ConnectionError:
    print("No internet connection")
    exit(1)
