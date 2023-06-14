from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from .models import Mouse
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user, loggeduser=current_user.username)

@views.route('/add-mouse', methods=['GET', 'POST'])
@login_required
def add_mouse():
    if request.method == "POST":
        mousename = request.form.get("mouseName")
        mouseimg = request.form.get("mouseImg")
        mousecat = request.form.get("mouseCat")
        mousesubcat = request.form.get("mouseSubCat")
        powertype = request.form.get("powerType")
        
        # Add mouse to database
        new_mouse = Mouse(mouseName=mousename, mouseImg=mouseimg, mouseCat=mousecat, mouseSubCat=mousesubcat, powerType=powertype)
        db.session.add(new_mouse)
        db.session.commit()
        flash("Mouse added!", category='success')

    return render_template("add-mouse.html", user=current_user, loggeduser=current_user.username)

@views.route('/seasonal', methods=['GET', 'POST'])
@login_required
def seasonal():
    mousedb = db.session.query(Mouse)
    return render_template("seasonal-soldiers.html", user=current_user, loggeduser=current_user.username, mousedb=mousedb)

@views.route('/foreword', methods=['GET', 'POST'])
@login_required
def foreword():
    return render_template("foreword-farmers.html", user=current_user, loggeduser=current_user.username)

@views.route('/prologue', methods=['GET', 'POST'])
@login_required
def prologue():
    return render_template("prologue-pond.html", user=current_user, loggeduser=current_user.username)

@views.route('/storytellers', methods=['GET', 'POST'])
@login_required
def storytellers():
    return render_template("storytellers.html", user=current_user, loggeduser=current_user.username)

@views.route('/floating', methods=['GET', 'POST'])
@login_required
def floating():
    return render_template("floating-islanders.html", user=current_user, loggeduser=current_user.username)

@views.route('/mythweaver', methods=['GET', 'POST'])
@login_required
def mythweaver():
    return render_template("mythweaver.html", user=current_user, loggeduser=current_user.username)