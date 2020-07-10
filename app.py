from flask import Flask, request, render_template
from connect import getApiRest

app = Flask(__name__)
api = getApiRest()

@app.route("/")
def home():
	url = api.getUrl()
	return render_template("index.html", urlCat = url)

@app.route("/randomcat")
def getCat():
	url = api.getUrl()
	return render_template("index.html", urlCat = url)


if __name__ == "__main__":
	app.run(debug=True)