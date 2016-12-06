from flask import Flask
from flask import render_template
from flask import pypyodbc
app = Flask(__name__)

@app.route('/bar/')
@app.route('/bar/<name>')
def bar(name=None):
	connection = pypyodbc.connect('Server=bars3.sqlite;''uid=Questlove-Magic;')
	cursor = connection.cursor()
	SQLCommand = ("SELECT name")
	results = cursor.fetchall()
	print("The bar's name is " + results[0])
	connection.close()
	return render_template('bar.html', name=name)

if __name__ == '__main__':	
	app.run()