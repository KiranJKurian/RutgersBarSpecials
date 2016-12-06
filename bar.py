from flask import Flask
from flask import render_template
import sqlite3
app = Flask(__name__)

@app.route('/bar/')
@app.route('/bar/<name>')
def bar(name=None):
	
	return render_template('bar.html', name=name)
	sqlite_file = '/Users/Johanna/Documents/GitHub/RutgersBarSpecials/app/bars.sqlite3'
	table_name= 'bars'
	connection = sqlite3.connect(sqlite_file)
	c = connection.cursor()
	c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
	names = [tup[1] for tup in c.fetchall()]
	print(names)
	connection.close()

if __name__ == '__main__':	
	app.run()