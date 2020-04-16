"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from app.forms import ProfileForm
from app.models import UserProfile

path = app.config['UPLOAD_FOLDER']

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET','POST'])
def add_profile():
    """GET provides the profile form while POST stores profile"""
    profileform = ProfileForm()
    if request.method == 'POST' and profileform.validate_on_submit():
        # Get values from form
        fname = request.form['first_name']
        lname = request.form['last_name']
        gender = request.form['gender']
        email = request.form['email']
        location = request.form['location']
        bio = request.form['bio']

        file = profileform.photo.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))
        
        try:
            profile = UserProfile(fname, lname, gender, email, location, bio, filename)
            db.session.add(profile)
            db.session.commit()
            flash('Profile Saved', 'success')
            return redirect(url_for('view_profiles'))
        except:
            flash("Profile failed to save", 'danger')
    return render_template('add_profile.html', form = profileform)


@app.route('/profiles')
def view_profiles():
    """Retrieve all profiles from the database."""
    profiles = db.session.query(UserProfile).all()
    return render_template("view_profiles.html", profiles = profiles)


@app.route('/profile/<userid>')
def view_profile(userid):
    """Fetch the user information for a profile that matches the id"""
    user = db.session.query(UserProfile).get(userid)
    return render_template("view_profile.html", user=user)


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
