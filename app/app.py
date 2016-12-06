from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bars.sqlite3'
app.config['SECRET_KEY'] = "Questlove-Magic"

db = SQLAlchemy(app)

class bars(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   zip = db.Column(db.String(10))
   mon = db.Column(db.String(240))
   tues = db.Column(db.String(240))
   weds = db.Column(db.String(240))
   thurs = db.Column(db.String(240))
   fri = db.Column(db.String(240))
   sat = db.Column(db.String(240))
   sun = db.Column(db.String(240))

   def __init__(self, name, city, addr, zip, mon, tues, weds, thurs, fri, sat, sun):
      self.name = name
      self.city = city
      self.addr = addr
      self.zip = zip
      self.mon = mon
      self.tues = tues
      self.weds = weds
      self.thurs = thurs
      self.fri = fri
      self.sat = sat
      self.sun = sun
      # How would you define the "specials" variable because if it's not defined, the program throws an error ("specials not defined")?
      # I tried to debug using the following and resulted in "[specials]". I am not sure if it's right.
      # http://stackoverflow.com/questions/19606745/flask-sqlalchemy-error-typeerror-incompatible-collection-type-model-is-not
      # http://stackoverflow.com/questions/11796934/flask-sqlalchemy-typeerror-class-object-is-not-iterable


      #self.specials = specials
     
@app.route('/')
def show_all():
   return render_template('show_all.html', bars = bars.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['zip']:
         flash('Please enter all the fields', 'error')
      else:
         
         bar = bars(request.form['name'], request.form['city'], request.form['addr'], request.form['zip'], request.form['special_mon'], request.form['special_tues'], request.form['special_weds'], request.form['special_thurs'], request.form['special_fri'], request.form['special_sat'], request.form['special_sun']) 
                    
         db.session.add(bar)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)