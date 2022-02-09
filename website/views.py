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

        nameLeftGirl = rate.getName(leftGirl)
        nameRightGirl = rate.getName(rightGirl)
        nameNewGirl = rate.getName(newGirl)

        leftGirlElo = int(rate.data[rate.girlToNumber(leftGirl)])
        rightGirlElo = int(rate.data[rate.girlToNumber(rightGirl)])
        newGirlElo = int(rate.data[rate.girlToNumber(newGirl)])

        if decision == "left":
            ew_leftGirl = rate.ew(rate.data[rate.girlToNumber(leftGirl)], rate.data[rate.girlToNumber(newGirl)])
            ew_rightGirl = 1-ew_leftGirl

            return render_template("Instamash.html", image1=leftGirl, image2=newGirl, elo1=leftGirlElo, elo2=newGirlElo, name1=nameLeftGirl, name2=nameNewGirl)
        if decision == "right":
            return render_template("Instamash.html", image1=newGirl, image2=rightGirl, elo1=newGirlElo, elo2=rightGirlElo, name1=nameNewGirl, name2=nameRightGirl)
        # data = request.form.get("value")

    return render_template("Instamash.html", image1=rate.getImage(1), image2=rate.getImage(2))
