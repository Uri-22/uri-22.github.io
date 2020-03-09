from flask import Flask, request, render_template
import requests


API_HOST = "https://api.yelp.com/v3/businesses/search?"
TOKEN = "QN_uM4CAc1AbjmqtBpQBA_2ZR2J46EGpHSznTbPsWzljGUPuOZV1XjAHwrzrhru4sHHWi4u14PJ-vEF1UcG3QFKD232RiW7HsNMIzqMYe-wSlnONbJWZ-92EQKxdXnYx"


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/restaurants", methods=["GET", "POST"])
def restaurant():
    if request.method == "GET":
        return render_template("page1.html")
    else:
        terms = request.form['term']
        zipcode = request.form['location']
        response = requests.get(API_HOST+"term={}&location={}".format(terms, zipcode), headers={"Authorization": "Bearer {}".format(TOKEN)}).json()
        bus_num = []

        for i in range(4):
            bus_num.append(response['businesses'][i])
        return render_template("page1.html", places=bus_num)



#returns top restaurants around you.
@app.route("/top", methods=['GET','POST'])
def top():
    if request.method == "GET":
        return render_template("top.html")
    else:
        lat = request.form['lat']
        long = request.form['long']
        response = requests.get(API_HOST+"term=restaurant&latitude={}&longitude={}".format(lat, long), headers={"Authorization": "Bearer {}".format(TOKEN)}).json()

        businesses = response['businesses']

        sortedBusiness = sorted(businesses, key=lambda k: k['rating'])

        num_bus = []

        for i in range(3):
            num_bus.append(sortedBusiness[i])

        return render_template("top.html", places=num_bus)





if __name__ == "__main__":
    app.run(debug=True)