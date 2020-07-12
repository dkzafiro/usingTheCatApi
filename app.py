from flask import Flask, request, render_template
from connect import getApiRest

app = Flask(__name__)
api = getApiRest()

@app.route("/")
def home():
	url = api.getUrl()
	text = api.getCatFact()
	return render_template("index.html", urlCat = url, textFact = text)

@app.route("/randomcat")
def getCat():
	url = api.getUrl()
	text = api.getCatFact()
	return render_template("index.html", urlCat = url , textFact = text)


if __name__ == "__main__":
	app.run(debug=True)