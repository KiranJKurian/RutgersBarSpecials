from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bars.sqlite3'
app.config['SECRET_KEY'] = "Questlove-Magic"

db = SQLAlchemy(app)

class bars(db.Model):
   id = db.Column('bar_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   zip = db.Column(db.String(10))
   specials= db.relationship('special', backref='bar',lazy='dynamic')

   def __init__(self, name, city, addr, zip, specials):
      self.name = name
      self.city = city
      self.addr = addr
      self.zip = zip
      self.specials = specials

class special(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   mon= db.Column(db.String(240))
   tues= db.Column(db.String(240))
   weds= db.Column(db.String(240))
   thurs= db.Column(db.String(240))
   fri= db.Column(db.String(240))
   sat= db.Column(db.String(240))
   sun= db.Column(db.String(240))
   bar_id= db.Column(db.Integer, db.ForeignKey(bar.id))

   def __init__(self, mon, tues, weds, thurs, fri, sat, sun):
      self.mon = mon
      self.tues = tues
      self.weds = weds
      self.thurs = thurs
      self.fri = fri
      self.sat = sat
      self.sun = sun

   
@app.route('/')
def show_all():
   return render_template('show_all.html', bars = bars.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         bar = bars(request.form['name'], request.form['city'], request.form['addr'], request.form['zip'])
         
         db.session.add(bar)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)