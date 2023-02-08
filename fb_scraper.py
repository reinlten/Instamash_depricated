import time
from logging import exception

from facebook_scraper import *
import gender_guesser.detector as gender

d = gender.Detector()

s = "/christof.hofmann.7"

print(s[1:])

try:
    profile = get_profile("christof.hofmann.7", cookies="/Users/felix/Downloads/facebook.com_cookies.txt", friends=True)
except exceptions.TemporarilyBanned:
    print("banned")


print(profile)

print(profile["profile_picture"])

print(profile["Friends"])

friends = profile["Friends"]

print("attempting to get more images")

images = []

#for friend in friends:
#    print(friend["name"] +"      "+ d.get_gender(friend["name"].split()[0]))

k = 0
for friend in friends:
    if d.get_gender(friend["name"].split()[0]) == "female":
        print(friend["name"] + "  " + friend["link"])
        k = k + 1
        temp = get_profile(friend["link"][1:], cookies="/Users/felix/Downloads/facebook.com_cookies.txt")
        print(temp["profile_picture"])
        time.sleep(2)

print(k)

print(len(friends))