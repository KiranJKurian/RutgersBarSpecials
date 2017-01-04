from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/bar/')
@app.route('/bar/<name>')
def bar(name=None):
	from dummyData import bars
	from dummyData import specials
	barsAr = [None] * 8
	for x in range(0,8):
		barsAr[x] = bars[x]
	specialsAr = [None] * 15
	for x in range (0,15):
		specialsAr[x] = specials[x]
	return render_template('bar.html', barsAr = barsAr, specialsAr = specialsAr)


if __name__ == '__main__':
	app.run()
