import json
import os
from website import models, db
from config import *



def create_stars_json():
    hose = os.listdir(k_image_dir)
    start_dict = {}

    #for img_filename in hose:
    for i in range(len(hose)):
        name = hose[i]
        f = open("website/static/imgdir/" + name + "/social.txt","r")
        social = f.readlines()
        f.close()
        ph = "none"
        insta = "none"
        twitter = "none"
        for link in social:
            if link.find("pornhub.com") != -1:
                ph = link
            if link.find("instagram.com") != -1:
                insta = link
            if link.find("twitter.com") != -1:
                twitter = link

        newGirl = models.Girldata(name=name, elo=k_default_elo, image_source=f"{k_image_path_base}{name+'/1.jpg'}",
                                  ph=ph.strip(), insta=insta.strip(), twitter=twitter.strip())

        db.session.add(newGirl)
        db.session.commit()

    with open(k_json_filename, 'w') as stars_json_file:
        json_dumps_str = json.dumps(start_dict, indent=4)
        print(json_dumps_str, file=stars_json_file)


def update_stars_elo_json(changes):
    stars_dict = None
    with open(k_json_filename) as stars_json_file:
        stars_dict = json.load(stars_json_file)

    for name, elo in changes.items():
        stars_dict[name]["elo"] = elo

    with open(k_json_filename, 'w') as stars_json_file:
        json_dumps_str = json.dumps(stars_dict, indent=4)
        print(json_dumps_str, file=stars_json_file)


def load_elos(names):
    with open(k_json_filename) as stars_json_file:
        stars_dict = json.load(stars_json_file)
        result = {}
        for name in names:
            result[name] = stars_dict[name]["elo"]

        return result


def load_stars():
    with open(k_json_filename) as stars_json_file:
        return json.load(stars_json_file)


if __name__ == "__main__":
    create_stars_json()
