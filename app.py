
import os
import requests
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

  


@app.route("/google47e5f3d143b3c670.html")
def google_verification():
    return send_from_directory(
        "/home/SreeNidhiSolutions",
        "google47e5f3d143b3c670.html"
    )
@app.route("/robots.txt")
def robots():
    return send_from_directory(
        "/home/SreeNidhiSolutions",
        "robots.txt",
        mimetype="text/plain"
    )


@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(
        "/home/SreeNidhiSolutions",
        "sitemap.xml",
        mimetype="application/xml"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
