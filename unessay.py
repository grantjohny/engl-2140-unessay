from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/AfricanAmericanAuthors")
def aaauthors():
	return render_template("aaauthors.html")

@app.route("/PuritanAuthors")
def pauthors():
	return render_template("pauthors.html")

@app.route("/About")
def about():
	return render_template("about.html")

@app.route("/Comparison")
def comparison():
	return render_template("comparison.html")
	
if __name__ == "__main__":
	app.run(debug=True)