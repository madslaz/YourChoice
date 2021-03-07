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

@app.route('/alaska')
def alabama():
    state = {'statename': 'Alaska'}
    info = {
        'information': "<strong> Accessible: </strong>" 
                       "\n Abortion is legal in this state, there are few to no restrictions and abortion is accessible. "
                       "\n \n  <strong> Restrictions: </strong>"
                       "\n <i> Abortion Counseling </i> \n A patient must receive state-directed counseling that includes information on the "
                       "designed to discourage the patient from having an abortion."
    email = {'address': "mailto?subject=Concern%20about%20Reproductive%20Rights%20in%20the%20US&body=Dear%20Representative%2C%20%0D%0A%0D%0AThe%20rhetoric%20around%20reproductive%20rights%20needs%20to%20change.%20Those%20who%20seek%20abortions%20may%20face%20physical%20or%20verbal%20abuse.%20Many%20have%20also%20reported%20being%20shamed%20by%20various%20medical%20personnel.%20%20Abortions%20are%20a%20basic%20healthcare%20necessity%20for%20millions%20worldwide.%20Limiting%20or%20banning%20access%20does%20not%20encourage%20citizens%20to%20carry%20out%20their%20pregnancies.%20Instead%2C%20when%20access%20to%20abortion%20is%20restricted%2C%20patients%20are%20forced%20to%20seek%20out%20unsafe%20procedures%20which%20could%20result%20in%20injury%20or%20death.%20Worldwide%2C%20unsafe%20abortion%20procedures%20are%20the%20third%20leading%20cause%20of%20maternal%20deaths.%20%0D%0A%0D%0AAlong%20with%20the%20existing%20negative%20rhetoric%2C%20proposals%20defunding%20Planned%20Parenthood%20threaten%20reproductive%20rights%20for%20millions.%20Planned%20Parenthood%20assists%20millions%20of%20patients%20yearly%20and%20is%20supported%20by%2075%25%20of%20Americans.%20Not%20only%20do%20they%20provide%20the%20essential%20service%20of%20abortion%2C%20but%20they%20also%20offer%20a%20plethora%20of%20reproductive%20health%20services%20such%20as%20counseling%2C%20cancer%20screenings%2C%20prenatal%20care%2C%20transgender%20health%20services%2C%20wellness%20exams%2C%20and%20much%20more.%20Defunding%20this%20essential%20resource%20will%20cause%20millions%20of%20Americans%20to%20lose%20access%20to%20quality%20health%20care%2C%20especially%20considering%2075%25%20of%20Planned%20Parenthood%20patients%20are%20below%20the%20federal%20poverty%20level.%20%0D%0A%0D%0AWe%20urge%20you%20to%20emphasize%20the%20importance%20of%20reproductive%20rights%20in%20future%20legislation.%20%0D%0A%0D%0AThank%20you%20for%20your%20time%20and%20consideration%2C%0D%0AAn%20Alabama%20constituent%0D%0A"} }
    map = {'gmap' : "https://www.google.com/maps/d/embed?mid=1IKihfJojab5tbwp4-Vv_ZW8A262K70Psn"}
    return render_template('statestyle.html', state=state, info=info, email=email, map=map)
