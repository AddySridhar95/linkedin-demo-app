from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/linkedin_authenticate")
def linkedin_authenticate():
	print("authenticated")
	print(request.url)
	url = request.url
	authentication_code = url.split("=")[1].split("&")[0]
	print(authentication_code)
	return render_template('index.html')
if __name__ == "__main__":
    app.run()