from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/bar/')
@app.route('/bar/<name>')
def bar(name=None):
	from dummyData import bars
	name = bars[0]['name']
	barOne = bars[0]
	return render_template('bar.html', name=name, barOne = barOne)


if __name__ == '__main__':
	app.run()
