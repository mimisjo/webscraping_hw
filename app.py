# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app
app = Flask(__name__)

#Use flask_pymongo to set up connection through mLab
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.scrape()
    mars_info.update({}, mars_info_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
