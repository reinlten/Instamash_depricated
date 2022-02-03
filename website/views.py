from flask import Blueprint, render_template, request
import os
import rate

views = Blueprint("views", __name__)

pic1 = rate.getImage(1)
pic2 = rate.getImage(2)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # print(request.form.get("image"))

        leftGirl = request.form.get("left_src")
        rightGirl = request.form.get("right_src")
        decision = request.form.get("chose")

        newGirl = rate.rateGirlAndReturn(leftGirl, rightGirl, decision)

        leftGirlElo = int(rate.data[rate.GirlToNumber(leftGirl)])
        rightGirlElo = int(rate.data[rate.GirlToNumber(rightGirl)])
        newGirlElo = int(rate.data[rate.GirlToNumber(newGirl)])

        if decision == "left":
            ew_leftGirl = rate.ew(rate.data[rate.GirlToNumber(leftGirl)], rate.data[rate.GirlToNumber(newGirl)])
            ew_rightGirl = 1-ew_leftGirl

            return render_template("Instamash.html", image1=leftGirl, image2=newGirl, elo1=leftGirlElo, elo2=newGirlElo)
        if decision == "right":
            return render_template("Instamash.html", image1=newGirl, image2=rightGirl, elo1=newGirlElo, elo2=rightGirlElo)
        # data = request.form.get("value")

    return render_template("Instamash.html", image1=rate.getImage(1), image2=rate.getImage(2))
