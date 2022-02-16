from flask import Blueprint, render_template, request
from sqlalchemy import func

import os

import data_loader
import rate
from website import models

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    # stars_dict = data_loader.load_stars()
    if request.method == "POST":
        leftGirl = request.form.get("left_src")
        rightGirl = request.form.get("right_src")
        decision = request.form.get("chose")

        newGirl = rate.rateGirlAndReturn(leftGirl, rightGirl, decision)

        girl1 = models.Girldata.query.filter_by(image_source=leftGirl).first()
        girl2 = models.Girldata.query.filter_by(image_source=rightGirl).first()
        girl_new = models.Girldata.query.filter_by(image_source=newGirl).first()

        girl1_name = girl1.name
        girl2_name = girl2.name
        girl_new_name = girl_new.name
        start_elos = [girl1.elo, girl2.elo]

        leftGirlElo = int(girl1.elo)
        leftGirlph = girl1.ph
        leftGirlinsta = girl1.insta
        leftGirltwitter = girl1.twitter
        rightGirlElo = int(girl2.elo)
        rightGirlph = girl2.ph
        rightGirlinsta = girl2.insta
        rightGirltwitter = girl2.twitter
        newGirlElo = int(girl_new.elo)
        newGirlph = girl_new.ph
        newGirlinsta = girl_new.insta
        newGirltwitter = girl_new.twitter

        if decision == "left":
            return render_template("Instamash2.html", image1=leftGirl, image2=newGirl, elo1=leftGirlElo,
                                   elo2=newGirlElo, name1=girl1_name, name2=girl_new_name,
                                   twitter1=leftGirltwitter, insta1=leftGirlinsta, ph1=leftGirlph,
                                   twitter2=newGirltwitter, insta2=newGirlinsta, ph2=newGirlph)
        if decision == "right":
            return render_template("Instamash2.html", image1=newGirl, image2=rightGirl, elo1=newGirlElo,
                                   elo2=rightGirlElo, name1=girl_new_name, name2=girl2_name,
                                   twitter1=newGirltwitter, insta1=newGirlinsta, ph1=newGirlph,
                                   twitter2=rightGirltwitter, insta2=rightGirlinsta, ph2=rightGirlph)

    randGirl1 = models.Girldata.query.order_by(func.random()).first()
    randGirl2 = rate.return_other_girl(randGirl1)
    return render_template("Instamash2.html", image1=randGirl1.image_source, image2=randGirl2.image_source,
                           elo1=randGirl1.elo, elo2=randGirl2.elo, twitter1=randGirl1.twitter,
                           twitter2=randGirl2.twitter, insta1=randGirl1.insta, insta2=randGirl2.insta,
                           ph1=randGirl1.ph, ph2=randGirl2.ph)
