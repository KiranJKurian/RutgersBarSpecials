from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists    


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bars.sqlite3'
app.config['SECRET_KEY'] = "Questlove-Magic"

db = SQLAlchemy(app)

class bar(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.Text)
   addr = db.Column(db.Text) 
   city = db.Column(db.Text)
   zip = db.Column(db.Text)
   specials = db.relationship('special', backref='bar')
   
   def __repr__(self):
      return '<bar:{}>'.format(self.name)
      
class special(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   day = db.Column(db.Text)
   special_name = db.Column(db.Text)
   price = db.Column(db.Text)
   bar_id = db.Column(db.Integer, db.ForeignKey('bar.id'))

   def __repr__(self):
      return '<special:{}>'.format(self.special_name)


@app.route('/')
def show_all():
   return render_template('show_all2.html', bars = bar.query.all(), specials = special.query.all() )

@app.route('/newBar', methods = ['GET', 'POST'])
def newBar():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['zip']:
         flash('Please enter all the fields', 'error')
      bar_form= request.form['name']
      if db.session.query(db.exists().where(bar.name == bar_form)).scalar() == 1: 
         flash('The bar already exists!', 'error')
      else:         
         new_bar = bar(name=request.form['name'], addr=request.form['addr'], city=request.form['city'], zip=request.form['zip'])
         db.session.add(new_bar)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new2.html')
@app.route('/newSpecial', methods = ['GET', 'POST'])
def newSpecial():
   if request.method == 'POST':
      if not request.form['day'] or not request.form['special'] or not request.form['price'] or not request.form['bar']:
         flash('Please enter all the fields', 'error')
      else:
         bar_form= request.form['bar']
         if db.session.query(db.exists().where(bar.name == bar_form)).scalar() == 1: 
            
            get_parent_id = bar.query.filter_by(name= bar_form).first()
            # special_paren = db.session.query(bar).filter(bar.name == bar_form)
            special_parent= get_parent_id.id
            #special_parent = bar.query.filter_by(bar.name == bar_form).id
            new_special = special(day=request.form['day'], special_name=request.form['special'], price=request.form['price'], bar_id= special_parent )
            # q = session.query(bar).filter(bar.name == bar_form).first()
            # bars_query = bar.query.filter_by(name= bar_form)
            # if bars_query.func.count() 
            # if session.query(q.exists()):
            # exists = db.session.query(db.exists().where(bar.name == bar_form)).scalar() 
         
            # q = session.query(User).join(User.addresses)
            # Author.query.join(Author.books).filter(Book.categories.contains(scifi)).all()
            # bar.query.filter(bar.name==bar_form).specials = [new_special]
            # db.session.add(bar.query.filter(bar.name==bar_form))
            db.session.add(new_special)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
         else:
            flash('Please add the bar first! You can add specials after that!', 'error')
            
   return render_template('new3.html')
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)