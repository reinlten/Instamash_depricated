from website import create_app

app = create_app()

if __name__ == '__main__':
   app.run(debug=True)

#from flask import Flask, render_template, url_for

#app = Flask(__name__)


#@app.route('/')
#def index():
#    return render_template("Instamash.html", image="static/img/nat2.png")


#@app.route('/about')
#def about():
#    pass


#if __name__ == '__main__':
#    app.run(debug=True)
