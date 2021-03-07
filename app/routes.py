from flask import render_template
from app import app


@app.route('/')
@app.route('/map')
def map():
    user = {'username': 'Map'}
    return render_template('Mapstyle.html', title='Map', user=user)


@app.route('/faq')
def faq():
    user = {'username': 'FAQ'}
    return render_template('FAQstyle.html', title='FAQ', user=user)


@app.route('/about')
def about():
    user = {'username': 'About'}
    return render_template('Aboutstyle.html', title='About', user=user)


@app.route('/alabama')
def alabama():
    state = {'statename': 'Alabama'}
    info = {
        'information': "<strong> Severely Restricted: </strong>" 
                       "\n Abortion is legal in this state, but there are severe state restrictions that make it very "
                       "difficult to access abortion. "
                       "\n \n  <strong> Restrictions: </strong>"
                       "\n <i> 20 Week Abortion Ban </i> \n Abortion is banned on or around 20 weeks. Depending on the "
                       "circumstances "
                       "there may be certain limited exceptions. \n \n "
                       " <i> Parental Consent Required </i> \n Parental consent "
                       "means that a parent or parents must give permission (usually written) to the minor to have an "
                       "abortion. \n \n "
                       "<i> Judicial Bypass Available: </i> \n Minors who cxan't tell their parent about their "
                       "decision to have an abortion can file a petition to excuse them from required parental "
                       "consent and/or notification requirements. \n \n <i> 48 Hours Waiting Period </i> \n Patient must wait "
                       "48 hours between receiving state-mandated abortion counseling and obtaining an abortion."}
    email = {'address': "mailto:lazas@usc.edu?subject=Test%20Subject&body=Test%20Body"}
    map = {'gmap' : "https://www.google.com/maps/d/embed?mid=1beFm-TLJ5wE0ND_wgKLSpVN2MSy6_bFc&hl=en"}
    return render_template('statestyle.html', state=state, info=info, email=email, map=map)
