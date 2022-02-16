import json
import os

from config import *



def create_stars_json():
    hose = os.listdir(k_image_dir)
    start_dict = {}

    f = open("website/static/imgsrc.txt", "r")
    img_filename = f.readlines()
    f.close()

    #for img_filename in hose:
    for i in range(len(img_filename)):
        name = hose[i]
        start_dict[name] = {"elo": k_default_elo, "image_source": f"{k_image_path_base}{name+'/'}{img_filename[i].strip()}"}

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
