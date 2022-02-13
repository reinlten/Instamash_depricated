#!/usr/bin/python

import sys
sys.path.insert(0,"/var/www/Instamash/") #Dadurch findet Python die App im PATH

from website import create_app

application = create_app()