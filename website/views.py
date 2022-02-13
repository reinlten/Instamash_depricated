from flask import Blueprint, render_template, request
import os

import data_loader
import rate

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    stars_dict = data_loader.load_stars()
    if request.method == "POST":
        leftGirl = request.form.get("left_src")
        rightGirl = request.form.get("right_src")
        decision = request.form.get("chose")

        newGirl = rate.rateGirlAndReturn(leftGirl, rightGirl, decision)

        nameLeftGirl = rate.get_name(leftGirl)
        nameRightGirl = rate.get_name(rightGirl)
        nameNewGirl = rate.get_name(newGirl)

        name_elo_dict = data_loader.load_elos([nameLeftGirl, nameRightGirl, nameNewGirl])

        leftGirlElo = int(name_elo_dict[nameLeftGirl])
        rightGirlElo = int(name_elo_dict[nameRightGirl])
        newGirlElo = int(name_elo_dict[nameNewGirl])

        if decision == "left":
            return render_template("Instamash.html", image1=leftGirl, image2=newGirl, elo1=leftGirlElo, elo2=newGirlElo, name1=nameLeftGirl, name2=nameNewGirl)
        if decision == "right":
            return render_template("Instamash.html", image1=newGirl, image2=rightGirl, elo1=newGirlElo, elo2=rightGirlElo, name1=nameNewGirl, name2=nameRightGirl)

    return render_template("Instamash.html", image1=stars_dict["Abella Danger"]["image_source"], image2=stars_dict["Aidra Fox"]["image_source"])
