from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1> Web App with Flask </h1>"

app.run()