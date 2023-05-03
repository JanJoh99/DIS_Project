from flask import Blueprint, render_template

views = Blueprint('views',__name__)

# Das hier ist die hauptseite, Der Route node des Programs
# Quasi ist das die frontseite der Homepage
@views.route('/')
def home():
    return render_template("home.html")

