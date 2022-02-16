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
        leftGirlph = stars_dict[nameLeftGirl]["ph"]
        leftGirlinsta = stars_dict[nameLeftGirl]["insta"]
        leftGirltwitter = stars_dict[nameLeftGirl]["twitter"]
        rightGirlElo = int(name_elo_dict[nameRightGirl])
        rightGirlph = stars_dict[nameRightGirl]["ph"]
        rightGirlinsta = stars_dict[nameRightGirl]["insta"]
        rightGirltwitter = stars_dict[nameRightGirl]["twitter"]
        newGirlElo = int(name_elo_dict[nameNewGirl])
        newGirlph = stars_dict[nameNewGirl]["ph"]
        newGirlinsta = stars_dict[nameNewGirl]["insta"]
        newGirltwitter = stars_dict[nameNewGirl]["twitter"]

        if decision == "left":
            return render_template("Instamash2.html", image1=leftGirl, image2=newGirl, elo1=leftGirlElo,
                                   elo2=newGirlElo, name1=nameLeftGirl, name2=nameNewGirl,
                                   twitter1=leftGirltwitter, insta1=leftGirlinsta, ph1=leftGirlph,
                                   twitter2=newGirltwitter, insta2=newGirlinsta, ph2=newGirlph)
        if decision == "right":
            return render_template("Instamash2.html", image1=newGirl, image2=rightGirl, elo1=newGirlElo,
                                   elo2=rightGirlElo, name1=nameNewGirl, name2=nameRightGirl,
                                   twitter1=newGirltwitter, insta1=newGirlinsta, ph1=newGirlph,
                                   twitter2=rightGirltwitter, insta2=rightGirlinsta, ph2=rightGirlph)

    return render_template("Instamash2.html", image1=stars_dict["1ladylove"]["image_source"], image2=stars_dict["1twothreecum"]["image_source"])
