from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/bar/')
@app.route('/bar/<name>')
def bar(name=None):
	return render_template('bar.html', name=name)

if __name__ == '__main__':	
	app.run()